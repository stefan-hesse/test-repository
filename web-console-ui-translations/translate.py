#!/usr/bin/env python3
"""
Avatour Web Console UI Translation Script
==========================================
Translates en.json to target languages using the DeepL API.

- Preserves all placeholders: $t(...), {{variable}}, <0>...</0>, <1>...</1> etc.
- Outputs one JSON file per language into dist/
- Also produces dist/translations.xlsx for human review

Usage:
    python translate.py

Environment variables:
    DEEPL_API_KEY   Your DeepL API key (set as GitHub Actions secret)

Languages translated:
    IT  Italian
    DE  German
"""

import json
import os
import re
import sys
import time
from pathlib import Path

# ── Dependencies ──────────────────────────────────────────────────────────────
try:
    import requests
except ImportError:
    print("Installing requests...")
    os.system(f"{sys.executable} -m pip install requests --quiet")
    import requests

try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment
except ImportError:
    print("Installing openpyxl...")
    os.system(f"{sys.executable} -m pip install openpyxl --quiet")
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment

# ── Configuration ─────────────────────────────────────────────────────────────

DEEPL_API_KEY = os.environ.get("DEEPL_API_KEY", "")
DEEPL_API_URL = "https://api.deepl.com/v2/translate"

SOURCE_FILE = Path(__file__).parent / "en.json"
DIST_DIR    = Path(__file__).parent / "dist"

LANGUAGES = {
    "IT": "Italian",
    "DE": "German",
}

# Strings whose values should NOT be translated (they are pure references or
# brand names that DeepL would mangle)
SKIP_TRANSLATION_PATTERN = re.compile(
    r"^\$t\([^)]+\)$"          # entire value is a single $t(...) reference
    r"|^\$t\([^)]+\)\s+\$t\([^)]+\)$"  # two $t(...) references
)

# ── Placeholder protection ─────────────────────────────────────────────────────
# These patterns must survive translation untouched.
PLACEHOLDER_PATTERNS = [
    re.compile(r"\$t\([^)]+\)"),          # $t(key)
    re.compile(r"\{\{[^}]+\}\}"),          # {{variable}}
    re.compile(r"<\d+>[^<]*</\d+>"),       # <0>text</0>
    re.compile(r"<\d+></\d+>"),            # <1></1>
    re.compile(r"<\d+>"),                  # <0>
    re.compile(r"</\d+>"),                 # </0>
    re.compile(r"<[a-zA-Z]\w*>[^<]*</[a-zA-Z]\w*>"),  # <tag>text</tag>
    re.compile(r"<[a-zA-Z]\w*>"),          # <tag>
    re.compile(r"</[a-zA-Z]\w*>"),         # </tag>
    re.compile(r"support@avatour\.live"),  # email address
]

def mask_placeholders(text):
    """
    Replace all placeholder tokens with numbered markers like @@PH0@@,
    returning the masked text and a list of original placeholder values.
    """
    placeholders = []
    masked = text

    # Find all placeholder positions in order
    matches = []
    for pattern in PLACEHOLDER_PATTERNS:
        for m in pattern.finditer(masked):
            matches.append((m.start(), m.end(), m.group()))

    # Sort by position, deduplicate overlapping matches (keep longest)
    matches.sort(key=lambda x: x[0])
    non_overlapping = []
    last_end = -1
    for start, end, value in matches:
        if start >= last_end:
            non_overlapping.append((start, end, value))
            last_end = end

    # Replace from right to left so positions stay valid
    for start, end, value in reversed(non_overlapping):
        idx = len(placeholders)
        placeholders.insert(0, value)
        marker = f"@@PH{len(placeholders)-1}@@"
        masked = masked[:start] + marker + masked[end:]

    # Renumber markers to match placeholders list order
    # (after reversal the indices are already correct)
    return masked, placeholders


def restore_placeholders(text, placeholders):
    """Replace @@PHn@@ markers back with original placeholder values."""
    result = text
    for i, value in enumerate(placeholders):
        result = result.replace(f"@@PH{i}@@", value)
    return result


# ── DeepL API ─────────────────────────────────────────────────────────────────

def translate_batch(texts, target_lang):
    """
    Send a batch of strings to DeepL and return translated strings.
    Uses formality=prefer_more for professional/formal tone.
    """
    if not DEEPL_API_KEY:
        raise ValueError("DEEPL_API_KEY environment variable is not set.")

    headers = {
        "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}",
        "Content-Type": "application/json",
    }

    # Formality is supported for IT and DE
    payload = {
        "text": texts,
        "source_lang": "EN",
        "target_lang": target_lang,
        "formality": "prefer_more",
        "preserve_formatting": True,
    }

    response = requests.post(DEEPL_API_URL, headers=headers, json=payload, timeout=30)

    if response.status_code != 200:
        raise RuntimeError(
            f"DeepL API error {response.status_code}: {response.text}"
        )

    data = response.json()
    return [t["text"] for t in data["translations"]]


def translate_all(strings_dict, target_lang):
    """
    Translate all values in strings_dict to target_lang.
    Skips pure $t(...) references and protects placeholders in all others.
    Returns a new dict with translated values.
    """
    keys = list(strings_dict.keys())
    values = list(strings_dict.values())

    # Separate keys that need translation from those that don't
    to_translate_indices = []
    to_translate_masked  = []
    placeholders_map     = {}

    for i, value in enumerate(values):
        if SKIP_TRANSLATION_PATTERN.match(value):
            # Pure reference — keep as-is
            continue
        masked, placeholders = mask_placeholders(value)
        to_translate_indices.append(i)
        to_translate_masked.append(masked)
        placeholders_map[i] = placeholders

    print(f"  Translating {len(to_translate_indices)} strings to {target_lang} "
          f"({len(values) - len(to_translate_indices)} skipped as pure references)...")

    # Send in batches of 50 to stay well within API limits
    BATCH_SIZE = 50
    translated_masked = []

    for batch_start in range(0, len(to_translate_masked), BATCH_SIZE):
        batch = to_translate_masked[batch_start:batch_start + BATCH_SIZE]
        batch_num = batch_start // BATCH_SIZE + 1
        total_batches = (len(to_translate_masked) + BATCH_SIZE - 1) // BATCH_SIZE
        print(f"    Batch {batch_num}/{total_batches} ({len(batch)} strings)...")
        translated_batch = translate_batch(batch, target_lang)
        translated_masked.extend(translated_batch)
        if batch_start + BATCH_SIZE < len(to_translate_masked):
            time.sleep(0.2)  # Be polite to the API

    # Rebuild the full values list
    result = list(values)  # start with originals
    for j, i in enumerate(to_translate_indices):
        restored = restore_placeholders(translated_masked[j], placeholders_map[i])
        result[i] = restored

    return dict(zip(keys, result))


# ── Excel output ──────────────────────────────────────────────────────────────

def write_excel(en_dict, translations, output_path):
    """
    Write a review Excel file with columns: Key | English | Italian | German
    """
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Translations"

    # Header style
    header_fill = PatternFill("solid", fgColor="132A39")  # Avatour navy
    header_font = Font(bold=True, color="FFFFFF")

    lang_names = ["English"] + [LANGUAGES[lang] for lang in translations.keys()]
    headers = ["Key"] + lang_names

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="left", vertical="center")

    ws.row_dimensions[1].height = 20

    # Column widths
    ws.column_dimensions["A"].width = 40
    ws.column_dimensions["B"].width = 50
    for col_letter in ["C", "D", "E"]:
        ws.column_dimensions[col_letter].width = 50

    # Data rows
    alt_fill = PatternFill("solid", fgColor="F7F8F9")  # Avatour off-white

    for row_idx, key in enumerate(en_dict.keys(), 2):
        fill = alt_fill if row_idx % 2 == 0 else PatternFill()

        ws.cell(row=row_idx, column=1, value=key).fill = fill

        en_cell = ws.cell(row=row_idx, column=2, value=en_dict[key])
        en_cell.fill = fill
        en_cell.alignment = Alignment(wrap_text=True)

        for col_idx, (lang_code, lang_dict) in enumerate(translations.items(), 3):
            cell = ws.cell(row=row_idx, column=col_idx, value=lang_dict.get(key, ""))
            cell.fill = fill
            cell.alignment = Alignment(wrap_text=True)

    # Freeze header row
    ws.freeze_panes = "A2"

    wb.save(output_path)
    print(f"  Excel review file written: {output_path.name}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("Avatour Web Console UI Translation")
    print("====================================")

    # Load source
    if not SOURCE_FILE.exists():
        print(f"ERROR: Source file not found: {SOURCE_FILE}")
        sys.exit(1)

    with open(SOURCE_FILE, encoding="utf-8") as f:
        en_dict = json.load(f)

    print(f"Loaded {len(en_dict)} strings from en.json")

    DIST_DIR.mkdir(exist_ok=True)

    all_translations = {}

    for lang_code, lang_name in LANGUAGES.items():
        print(f"\nTranslating to {lang_name} ({lang_code})...")
        translated = translate_all(en_dict, lang_code)
        all_translations[lang_code] = translated

        # Write JSON output
        out_path = DIST_DIR / f"{lang_code.lower()}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(translated, f, ensure_ascii=False, indent=2)
        print(f"  JSON written: {out_path.name}")

    # Write combined Excel review file
    print("\nWriting Excel review file...")
    excel_path = DIST_DIR / "translations.xlsx"
    write_excel(en_dict, all_translations, excel_path)

    print("\nDone!")
    print(f"  dist/it.json         — Italian translations")
    print(f"  dist/de.json         — German translations")
    print(f"  dist/translations.xlsx — Combined review file (EN / IT / DE)")


if __name__ == "__main__":
    main()
