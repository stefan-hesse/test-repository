#!/usr/bin/env python3
"""
Avatour Web Console UI Translation Script
==========================================
Translates en.json to Italian and German using the DeepL API.

Approach:
  1. Mask all placeholders ($t(), {{var}}, <0>, SuperFreeze etc.) before
     sending to DeepL so they are never translated or reordered.
  2. Translate via DeepL with formal register (Sie / Lei).
  3. Apply post-processing fixes for known bad translations — this is more
     reliable than the DeepL glossary API which requires a paid plan to
     work consistently.
  4. Output it.json, de.json, and translations.xlsx for review.

Usage:
    python translate.py

Environment variables:
    DEEPL_API_KEY   DeepL API key (set as GitHub Actions secret)
"""

import json
import os
import re
import sys
import time
from pathlib import Path

# -- Dependencies --------------------------------------------------------------
try:
    import requests
except ImportError:
    os.system(f"{sys.executable} -m pip install requests --quiet")
    import requests

try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment
except ImportError:
    os.system(f"{sys.executable} -m pip install openpyxl --quiet")
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment

# -- Configuration -------------------------------------------------------------

DEEPL_API_KEY = os.environ.get("DEEPL_API_KEY", "")
DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"

SOURCE_FILE = Path(__file__).parent / "en.json"
DIST_DIR    = Path(__file__).parent / "dist"

LANGUAGES = {
    "IT": "Italian",
    "DE": "German",
}

# -- Pre-translations ----------------------------------------------------------
# These keys are set BEFORE DeepL runs, bypassing translation entirely.
# Used for single words that DeepL consistently mistranslates.

PRE_TRANSLATIONS = {
    "DE": {
        "volume":    "Lautstärke",
        "assets":    "Assets",
        "asset":     "Asset",
        "history":   "Verlauf",
        "exit":      "Beenden",
        "play":      "Wiedergabe",
        "cancel":    "Abbrechen",
        "analytics": "Analysen",
        "filters":   "Filter",
        "host":      "Host",
        "hosts":     "Hosts",
        "meeting":   "Meeting",
        "session":   "Meeting",
        "change":    "Ändern",
        "deactivate": "Deaktivieren",
        "reactivate": "Reaktivieren",
        "new_meeting": "neues Meeting",
    },
    "IT": {
        "assets":    "asset",
        "asset":     "asset",
        "history":   "cronologia",
        "host":      "host",
        "hosts":     "host",
        "exit":      "Esci",
        "play":      "Riproduci",
        "cancel":    "Annulla",
        "change":    "Cambia",
        "analytics": "analisi",
        "filters":   "filtri",
        "superfreeze": "SuperFreeze",
    },
}

# -- Post-processing fixes -----------------------------------------------------
# Applied after DeepL translation to correct known bad translations.
# Each entry is (wrong_value, correct_value) — exact string match on the
# full translated value only (not substring replacement within longer strings).
#
# To add a new fix: add a tuple ("wrong DeepL output", "correct translation")

FIXES = {
    "DE": [
        # Single-word / short UI labels — exact value fixes
        ("band",             "Lautstärke"),       # volume
        ("vermögenswerte",   "Assets"),            # assets
        ("vermögen",         "Asset"),             # asset
        ("geschichte",       "Verlauf"),           # history
        ("ausgang",          "Beenden"),           # exit
        ("spielen",          "Wiedergabe"),        # play
        ("abbrechen",        "Abbrechen"),         # cancel (already correct casing)
        ("analytik",         "Analysen"),          # analytics
        ("filtert",          "Filter"),            # filters
        ("gastgeber",        "Host"),              # host
        ("treffen",          "Meeting"),           # meeting/session
        ("sitzung",          "Meeting"),           # meeting (alt)
        # Compound fixes — verb forms on buttons
        ("Ändern Sie",       "Ändern"),            # change (verb)
        ("deaktivieren Sie", "Deaktivieren"),      # deactivate
        ("reaktivieren Sie", "Reaktivieren"),      # reactivate
        # Broken asset-related strings
        ("ANZAHL DER VERMÖGENSWERTE", "ANZAHL DER ASSETS"),
        ("lebenslauf ein Vorteil",    "Asset fortsetzen"),
        ("einen Vermögenswert angehalten", "Asset pausiert"),
        ("Möchten Sie das SuperFreeze als Anlage behalten?",
         "Möchten Sie den SuperFreeze als Asset behalten?"),
        # Waiting for guide (Reiseführer = travel guide book)
        ("Warten auf den Reiseführer...", "Warten auf den Host..."),
    ],
    "IT": [
        # Single-word / short UI labels — exact value fixes
        ("patrimonio",   "asset"),          # assets
        ("attività",     "asset"),          # asset
        ("storia",       "cronologia"),     # history
        ("ospite",       "host"),           # host (conflicts with guest=ospite)
        ("padroni di casa", "host"),        # hosts
        ("uscita",       "Esci"),           # exit
        ("giocare",      "Riproduci"),      # play
        ("annullamento", "Annulla"),        # cancel (noun→verb)
        ("presentare",   "Presente"),       # present
        # Compound fixes
        ("Cambiamento",  "Cambia"),         # change (noun→verb)
        ("superGelo",    "SuperFreeze"),    # product name
        ("SuperCongelamento accettato", "SuperFreeze accettato"),
        ("Richiesta di supercongelamento rifiutata",
         "Richiesta SuperFreeze rifiutata"),
        # Asset-related strings
        ("NUMERO DI BENI",   "NUMERO DI ASSET"),
        ("Numero di Attività per tipo", "Numero di asset per tipo"),
        ("il curriculum è una risorsa", "riprende un asset"),
        ("Vuole mantenere il SuperFreeze come risorsa?",
         "Vuole mantenere il SuperFreeze come asset?"),
        ("Tutte le note associate a questo bene saranno cancellate quando il layout viene modificato",
         "Tutte le note associate a questo asset saranno cancellate quando il layout viene modificato"),
        # host/guest confusion — fix strings where "host" was translated as "ospite"
        # These are checked as substrings for longer strings
    ],
}

# Substring fixes — applied within longer string values (not exact match)
# Format: (substring_to_find, replacement) per language
SUBSTRING_FIXES = {
    "DE": [
        ("Gastgeber",  "Host"),        # host within sentences
        ("Treffen",    "Meeting"),     # meeting within sentences
        ("Sitzung",    "Meeting"),     # meeting (alt) within sentences
    ],
    "IT": [
        # In longer strings, "ospite" used for host needs fixing contextually
        # These are specific known strings
    ],
}


def apply_fixes(translated_dict, lang_code):
    """
    Apply post-processing fixes to translated values.
    First applies exact-match fixes, then substring fixes.
    """
    exact_fixes = FIXES.get(lang_code, [])
    substr_fixes = SUBSTRING_FIXES.get(lang_code, [])
    fixed_count = 0
    result = {}

    for key, value in translated_dict.items():
        new_value = value

        # Exact match fixes (case-insensitive comparison, preserve original case of fix)
        for wrong, correct in exact_fixes:
            if new_value.lower() == wrong.lower():
                new_value = correct
                fixed_count += 1
                break

        # Substring fixes (only applied if no exact fix was made)
        if new_value == value:
            for wrong, correct in substr_fixes:
                if wrong in new_value:
                    new_value = new_value.replace(wrong, correct)
                    fixed_count += 1

        result[key] = new_value

    print(f"  Post-processing: {fixed_count} fixes applied.")
    return result


# -- Skip pattern --------------------------------------------------------------
SKIP_TRANSLATION_PATTERN = re.compile(
    r"^\$t\([^)]+\)$"
    r"|^\$t\([^)]+\)\s+\$t\([^)]+\)$"
)

# -- Placeholder protection ----------------------------------------------------
PLACEHOLDER_PATTERNS = [
    re.compile(r"\$t\([^)]+\)"),
    re.compile(r"\{\{[^}]+\}\}"),
    re.compile(r"<\d+>[^<]*</\d+>"),
    re.compile(r"<\d+></\d+>"),
    re.compile(r"<\d+>"),
    re.compile(r"</\d+>"),
    re.compile(r"<[a-zA-Z]\w*>[^<]*</[a-zA-Z]\w*>"),
    re.compile(r"<[a-zA-Z]\w*>"),
    re.compile(r"</[a-zA-Z]\w*>"),
    re.compile(r"support@avatour\.live"),
    re.compile(r"SuperFreeze"),
]


def mask_placeholders(text):
    matches = []
    for pattern in PLACEHOLDER_PATTERNS:
        for m in pattern.finditer(text):
            matches.append((m.start(), m.end(), m.group()))

    matches.sort(key=lambda x: x[0])
    non_overlapping = []
    last_end = -1
    for start, end, value in matches:
        if start >= last_end:
            non_overlapping.append((start, end, value))
            last_end = end

    placeholders = [v for _, _, v in non_overlapping]
    masked = text
    for i, (start, end, _) in enumerate(reversed(non_overlapping)):
        idx = len(non_overlapping) - 1 - i
        masked = masked[:start] + f"@@PH{idx}@@" + masked[end:]

    return masked, placeholders


def restore_placeholders(text, placeholders):
    result = text
    for i, value in enumerate(placeholders):
        result = result.replace(f"@@PH{i}@@", value)
    return result


# -- DeepL Translation API -----------------------------------------------------

def translate_batch(texts, target_lang):
    """Translate a list of strings via DeepL with formal register."""
    if not DEEPL_API_KEY:
        raise ValueError("DEEPL_API_KEY environment variable is not set.")

    headers = {
        "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "text":                texts,
        "source_lang":         "EN",
        "target_lang":         target_lang,
        "formality":           "prefer_more",
        "preserve_formatting": True,
    }

    response = requests.post(DEEPL_API_URL, headers=headers,
                             json=payload, timeout=30)
    if response.status_code != 200:
        raise RuntimeError(
            f"DeepL API error {response.status_code}: {response.text}"
        )
    return [t["text"] for t in response.json()["translations"]]


def translate_all(strings_dict, target_lang):
    """Translate all values, skipping pure $t() refs and protecting placeholders."""
    # Apply pre-translations — these keys bypass DeepL entirely
    pre = PRE_TRANSLATIONS.get(target_lang, {})
    strings_dict = {k: pre[k] if k in pre else v
                    for k, v in strings_dict.items()}
    print(f"  Pre-translated {len(pre)} keys, bypassing DeepL.")

    keys   = list(strings_dict.keys())
    values = list(strings_dict.values())

    to_translate_indices = []
    to_translate_masked  = []
    placeholders_map     = {}

    for i, value in enumerate(values):
        if SKIP_TRANSLATION_PATTERN.match(value):
            continue
        if keys[i] in pre:  # pre-translated — skip DeepL entirely
            continue
        masked, placeholders = mask_placeholders(value)
        to_translate_indices.append(i)
        to_translate_masked.append(masked)
        placeholders_map[i] = placeholders

    print(f"  Translating {len(to_translate_indices)} strings "
          f"({len(values) - len(to_translate_indices)} skipped as pure references)...")

    BATCH_SIZE = 50
    translated_masked = []

    for batch_start in range(0, len(to_translate_masked), BATCH_SIZE):
        batch         = to_translate_masked[batch_start:batch_start + BATCH_SIZE]
        batch_num     = batch_start // BATCH_SIZE + 1
        total_batches = (len(to_translate_masked) + BATCH_SIZE - 1) // BATCH_SIZE
        print(f"    Batch {batch_num}/{total_batches} ({len(batch)} strings)...")
        translated_batch = translate_batch(batch, target_lang)
        translated_masked.extend(translated_batch)
        if batch_start + BATCH_SIZE < len(to_translate_masked):
            time.sleep(0.2)

    result = list(values)
    for j, i in enumerate(to_translate_indices):
        restored = restore_placeholders(translated_masked[j], placeholders_map[i])
        result[i] = restored

    return dict(zip(keys, result))


# -- Excel output --------------------------------------------------------------

def write_excel(en_dict, translations, output_path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Translations"

    header_fill = PatternFill("solid", fgColor="132A39")
    header_font = Font(bold=True, color="FFFFFF")
    headers = ["Key", "English"] + [LANGUAGES[l] for l in translations]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="left", vertical="center")

    ws.row_dimensions[1].height = 20
    ws.column_dimensions["A"].width = 40
    ws.column_dimensions["B"].width = 50
    for letter in ["C", "D", "E"]:
        ws.column_dimensions[letter].width = 50

    alt_fill = PatternFill("solid", fgColor="F7F8F9")

    for row_idx, key in enumerate(en_dict.keys(), 2):
        fill = alt_fill if row_idx % 2 == 0 else PatternFill()
        ws.cell(row=row_idx, column=1, value=key).fill = fill
        en_cell = ws.cell(row=row_idx, column=2, value=en_dict[key])
        en_cell.fill = fill
        en_cell.alignment = Alignment(wrap_text=True)
        for col_idx, (lang_code, lang_dict) in enumerate(translations.items(), 3):
            cell = ws.cell(row=row_idx, column=col_idx,
                           value=lang_dict.get(key, ""))
            cell.fill = fill
            cell.alignment = Alignment(wrap_text=True)

    ws.freeze_panes = "A2"
    wb.save(output_path)
    print(f"  Excel review file written: {output_path.name}")


# -- Main ----------------------------------------------------------------------

def main():
    print("Avatour Web Console UI Translation")
    print("====================================")

    if not SOURCE_FILE.exists():
        print(f"ERROR: Source file not found: {SOURCE_FILE}")
        sys.exit(1)

    with open(SOURCE_FILE, encoding="utf-8-sig") as f:
        en_dict = json.load(f)

    print(f"Loaded {len(en_dict)} strings from en.json")
    DIST_DIR.mkdir(exist_ok=True)

    all_translations = {}

    for lang_code, lang_name in LANGUAGES.items():
        print(f"\nTranslating to {lang_name} ({lang_code})...")
        translated = translate_all(en_dict, lang_code)
        translated = apply_fixes(translated, lang_code)
        all_translations[lang_code] = translated

        out_path = DIST_DIR / f"{lang_code.lower()}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(translated, f, ensure_ascii=False, indent=2)
        print(f"  JSON written: {out_path.name}")

    print("\nWriting Excel review file...")
    write_excel(en_dict, all_translations, DIST_DIR / "translations.xlsx")

    print("\nDone!")
    print("  dist/it.json           — Italian translations")
    print("  dist/de.json           — German translations")
    print("  dist/translations.xlsx — Combined review file (EN / IT / DE)")


if __name__ == "__main__":
    main()
