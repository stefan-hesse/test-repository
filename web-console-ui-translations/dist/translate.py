#!/usr/bin/env python3
"""
Avatour Web Console UI Translation Script
==========================================
Translates en.json to target languages using the DeepL API.

- Preserves all placeholders: $t(...), {{variable}}, <0>...</0>, <1>...</1> etc.
- Glossary ensures consistent UI vocabulary per language
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

# -- Dependencies --------------------------------------------------------------
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

# -- Configuration -------------------------------------------------------------

DEEPL_API_KEY      = os.environ.get("DEEPL_API_KEY", "")
DEEPL_API_URL      = "https://api-free.deepl.com/v2/translate"
DEEPL_GLOSSARY_URL = "https://api-free.deepl.com/v2/glossaries"

SOURCE_FILE = Path(__file__).parent / "en.json"
DIST_DIR    = Path(__file__).parent / "dist"

LANGUAGES = {
    "IT": "Italian",
    "DE": "German",
}

# -- Glossaries ----------------------------------------------------------------
# Terms DeepL must translate in a specific way.
# Keys are lowercase English source terms (DeepL matching is case-insensitive).
# Values are the exact target-language strings to use.
#
# Product names / branded terms that must never be translated are listed in
# PROTECTED_TERMS below and injected into every glossary automatically.

PROTECTED_TERMS = [
    # These are kept identical in all languages
    "SuperFreeze",
    "Avatour",
]

GLOSSARIES = {
    "DE": {
        # Core UI vocabulary fixes
        "asset":          "Asset",           # not "Vermögen" (financial asset)
        "assets":         "Assets",          # not "Vermögenswerte"
        "history":        "Verlauf",         # not "Geschichte" (world history)
        "analytics":      "Analysen",        # not "Analytik"
        "volume":         "Lautstärke",      # not "Band" (music band)
        "exit":           "Beenden",         # not "Ausgang" (physical door)
        "filters":        "Filter",          # not "filtert"
        "play":           "Wiedergabe",      # not "Spielen" (play a game)
        "cancel":         "Abbrechen",       # verb form for buttons
        "change":         "Ändern",          # verb form for buttons
        # Terms to keep in English
        "host":           "Host",
        "hosts":          "Hosts",
        "meeting":        "Meeting",
        "meetings":       "Meetings",
        "chat":           "Chat",
        "desktop":        "Desktop",
        "feedback":       "Feedback",
        "layout":         "Layout",
        "account":        "Konto",
        # Standard German UI terms
        "guest":          "Gast",
        "guests":         "Gäste",
        "workspace":      "Arbeitsbereich",
        "workspaces":     "Arbeitsbereiche",
        "library":        "Bibliothek",
        "profile":        "Profil",
        "settings":       "Einstellungen",
        "license":        "Lizenz",
        "licenses":       "Lizenzen",
        "preview":        "Vorschau",
        "recording":      "Aufzeichnung",
        "snapshot":       "Schnappschuss",
        "capture":        "Aufnahme",
        "upload":         "Hochladen",
        "download":       "Herunterladen",
        "overview":       "Übersicht",
        "status":         "Status",
        "details":        "Details",
        "description":    "Beschreibung",
        "schedule":       "Zeitplan",
        "transfer":       "Übertragen",
        "location":       "Standort",
        "efficiency":     "Effizienz",
        "customization":  "Anpassung",
        "notifications":  "Benachrichtigungen",
        "device":         "Gerät",
        "devices":        "Geräte",
    },
    "IT": {
        # Core UI vocabulary fixes
        "asset":          "asset",           # not "attività" or "patrimonio"
        "assets":         "asset",           # not "patrimonio"
        "history":        "cronologia",      # not "storia" (world history)
        "host":           "host",            # not "ospite" (same word as guest = confusion)
        "hosts":          "host",
        "exit":           "Esci",            # verb form, not "uscita" (noun/door)
        "play":           "Riproduci",       # media player, not "giocare" (play a game)
        "cancel":         "Annulla",         # verb form for buttons
        "change":         "Cambia",          # verb form, not "Cambiamento" (noun)
        "account":        "account",         # keep English (standard in Italian software)
        # Terms to keep in English
        "chat":           "chat",
        "desktop":        "desktop",
        "feedback":       "feedback",
        "layout":         "layout",
        # Standard Italian UI terms
        "guest":          "ospite",
        "guests":         "ospiti",
        "workspace":      "area di lavoro",
        "workspaces":     "aree di lavoro",
        "library":        "libreria",
        "profile":        "profilo",
        "settings":       "impostazioni",
        "filters":        "filtri",
        "license":        "licenza",
        "licenses":       "licenze",
        "preview":        "anteprima",
        "recording":      "registrazione",
        "snapshot":       "istantanea",
        "capture":        "acquisizione",
        "upload":         "carica",
        "download":       "scarica",
        "overview":       "panoramica",
        "status":         "stato",
        "details":        "dettagli",
        "description":    "descrizione",
        "schedule":       "pianificazione",
        "transfer":       "trasferimento",
        "location":       "posizione",
        "efficiency":     "efficienza",
        "customization":  "personalizzazione",
        "notifications":  "notifiche",
        "analytics":      "analisi",
        "device":         "dispositivo",
        "devices":        "dispositivi",
        "meeting":        "riunione",
        "meetings":       "riunioni",
    },
}

# -- Skip pattern --------------------------------------------------------------
# Values that are pure $t() references — nothing to translate
SKIP_TRANSLATION_PATTERN = re.compile(
    r"^\$t\([^)]+\)$"
    r"|^\$t\([^)]+\)\s+\$t\([^)]+\)$"
)

# -- Placeholder protection ----------------------------------------------------
# Order matters: more specific patterns before general ones.
# Numbered HTML-style tags are the main reordering risk — listed first.
PLACEHOLDER_PATTERNS = [
    re.compile(r"\$t\([^)]+\)"),                       # $t(key)
    re.compile(r"\{\{[^}]+\}\}"),                      # {{variable}}
    re.compile(r"<\d+>[^<]*</\d+>"),                   # <0>text</0>  full pair
    re.compile(r"<\d+></\d+>"),                        # <1></1>      empty pair
    re.compile(r"<\d+>"),                              # <0>          opening tag
    re.compile(r"</\d+>"),                             # </0>         closing tag
    re.compile(r"<[a-zA-Z]\w*>[^<]*</[a-zA-Z]\w*>"),  # <tag>text</tag>
    re.compile(r"<[a-zA-Z]\w*>"),                      # <tag>
    re.compile(r"</[a-zA-Z]\w*>"),                     # </tag>
    re.compile(r"support@avatour\.live"),              # email address
    re.compile(r"SuperFreeze"),                        # product name
]


def mask_placeholders(text):
    """
    Replace all placeholder tokens with positional markers @@PH0@@, @@PH1@@...
    Returns (masked_text, [original_placeholder_values]).
    """
    matches = []
    for pattern in PLACEHOLDER_PATTERNS:
        for m in pattern.finditer(text):
            matches.append((m.start(), m.end(), m.group()))

    # Sort by position; discard overlapping matches (keep first/longest)
    matches.sort(key=lambda x: x[0])
    non_overlapping = []
    last_end = -1
    for start, end, value in matches:
        if start >= last_end:
            non_overlapping.append((start, end, value))
            last_end = end

    placeholders = [v for _, _, v in non_overlapping]

    # Replace right-to-left so earlier positions stay valid
    masked = text
    for i, (start, end, _) in enumerate(reversed(non_overlapping)):
        idx = len(non_overlapping) - 1 - i
        masked = masked[:start] + f"@@PH{idx}@@" + masked[end:]

    return masked, placeholders


def restore_placeholders(text, placeholders):
    """Replace @@PHn@@ markers back with original placeholder values."""
    result = text
    for i, value in enumerate(placeholders):
        result = result.replace(f"@@PH{i}@@", value)
    return result


# -- DeepL Glossary API --------------------------------------------------------

def build_glossary_entries(lang_code):
    """
    Combine language-specific terms with protected product names.
    Returns a dict of { english_term: target_term }.
    """
    entries = dict(GLOSSARIES.get(lang_code, {}))
    # Protected terms map to themselves (kept identical in all languages)
    for term in PROTECTED_TERMS:
        entries[term] = term
    return entries


def create_glossary(lang_code):
    """
    Create a DeepL glossary for lang_code. Returns glossary ID or None.
    Deletes any pre-existing Avatour glossary for this language pair first.
    """
    if not DEEPL_API_KEY:
        raise ValueError("DEEPL_API_KEY environment variable is not set.")

    entries = build_glossary_entries(lang_code)
    if not entries:
        print(f"  No glossary entries for {lang_code}, skipping.")
        return None

    headers = {
        "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}",
        "Content-Type": "application/json",
    }

    # Remove any existing Avatour glossaries for this language pair
    resp = requests.get(DEEPL_GLOSSARY_URL, headers=headers, timeout=15)
    if resp.status_code == 200:
        for g in resp.json().get("glossaries", []):
            if (g.get("name", "").startswith("avatour-ui-")
                    and g.get("target_lang", "").upper() == lang_code.upper()):
                requests.delete(
                    f"{DEEPL_GLOSSARY_URL}/{g['glossary_id']}",
                    headers=headers, timeout=15
                )
                print(f"  Deleted old glossary: {g['name']}")

    # Create new glossary
    tsv_entries = "\n".join(f"{src}\t{tgt}" for src, tgt in entries.items())
    payload = {
        "name":           f"avatour-ui-{lang_code.lower()}",
        "source_lang":    "EN",
        "target_lang":    lang_code,
        "entries":        tsv_entries,
        "entries_format": "tsv",
    }

    resp = requests.post(DEEPL_GLOSSARY_URL, headers=headers,
                         json=payload, timeout=15)
    if resp.status_code not in (200, 201):
        print(f"  WARNING: Could not create glossary "
              f"({resp.status_code}): {resp.text}")
        print(f"  Continuing without glossary — manual review recommended.")
        return None

    glossary_id = resp.json()["glossary_id"]
    print(f"  Glossary created: avatour-ui-{lang_code.lower()} "
          f"({len(entries)} terms, id={glossary_id})")
    return glossary_id


def delete_glossary(glossary_id):
    """Remove a glossary from DeepL after use."""
    if not glossary_id:
        return
    headers = {"Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}"}
    requests.delete(f"{DEEPL_GLOSSARY_URL}/{glossary_id}",
                    headers=headers, timeout=15)
    print(f"  Glossary deleted: {glossary_id}")


# -- DeepL Translation API -----------------------------------------------------

def translate_batch(texts, target_lang, glossary_id=None):
    """
    Translate a list of strings via DeepL.
    Uses formal register (Sie / Lei) and attaches glossary when available.
    """
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
    if glossary_id:
        payload["glossary_id"] = glossary_id

    response = requests.post(DEEPL_API_URL, headers=headers,
                             json=payload, timeout=30)
    if response.status_code != 200:
        raise RuntimeError(
            f"DeepL API error {response.status_code}: {response.text}"
        )
    return [t["text"] for t in response.json()["translations"]]


def translate_all(strings_dict, target_lang, glossary_id=None):
    """
    Translate all values in strings_dict to target_lang.
    Pure $t() references are skipped. All placeholders are masked/restored.
    """
    keys   = list(strings_dict.keys())
    values = list(strings_dict.values())

    to_translate_indices = []
    to_translate_masked  = []
    placeholders_map     = {}

    for i, value in enumerate(values):
        if SKIP_TRANSLATION_PATTERN.match(value):
            continue
        masked, placeholders = mask_placeholders(value)
        to_translate_indices.append(i)
        to_translate_masked.append(masked)
        placeholders_map[i] = placeholders

    print(f"  Translating {len(to_translate_indices)} strings to {target_lang} "
          f"({len(values) - len(to_translate_indices)} skipped as pure references)...")

    BATCH_SIZE = 50
    translated_masked = []

    for batch_start in range(0, len(to_translate_masked), BATCH_SIZE):
        batch         = to_translate_masked[batch_start:batch_start + BATCH_SIZE]
        batch_num     = batch_start // BATCH_SIZE + 1
        total_batches = (len(to_translate_masked) + BATCH_SIZE - 1) // BATCH_SIZE
        print(f"    Batch {batch_num}/{total_batches} ({len(batch)} strings)...")
        translated_batch = translate_batch(batch, target_lang, glossary_id)
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
    """Write review spreadsheet: Key | English | Italian | German"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Translations"

    header_fill = PatternFill("solid", fgColor="132A39")  # Avatour navy
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

    alt_fill = PatternFill("solid", fgColor="F7F8F9")  # Avatour off-white

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

    with open(SOURCE_FILE, encoding="utf-8") as f:
        en_dict = json.load(f)

    print(f"Loaded {len(en_dict)} strings from en.json")
    DIST_DIR.mkdir(exist_ok=True)

    all_translations = {}

    for lang_code, lang_name in LANGUAGES.items():
        print(f"\nTranslating to {lang_name} ({lang_code})...")

        print("  Setting up glossary...")
        glossary_id = create_glossary(lang_code)

        translated = translate_all(en_dict, lang_code, glossary_id)
        all_translations[lang_code] = translated

        out_path = DIST_DIR / f"{lang_code.lower()}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(translated, f, ensure_ascii=False, indent=2)
        print(f"  JSON written: {out_path.name}")

        delete_glossary(glossary_id)

    print("\nWriting Excel review file...")
    write_excel(en_dict, all_translations, DIST_DIR / "translations.xlsx")

    print("\nDone!")
    print("  dist/it.json           — Italian translations")
    print("  dist/de.json           — German translations")
    print("  dist/translations.xlsx — Combined review file (EN / IT / DE)")


if __name__ == "__main__":
    main()
