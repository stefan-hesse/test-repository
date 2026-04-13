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
# Terms DeepL must always translate in a specific way.
# Keys are lowercase English source terms.
# Values are the exact target-language strings to use.
#
# Product names that must never be translated are in PROTECTED_TERMS
# and are injected into every glossary automatically.

PROTECTED_TERMS = [
    "SuperFreeze",
    "Avatour",
]

GLOSSARIES = {
    "DE": {
        "asset":          "Asset",
        "assets":         "Assets",
        "history":        "Verlauf",
        "analytics":      "Analysen",
        "volume":         "Lautstärke",
        "exit":           "Beenden",
        "filters":        "Filter",
        "play":           "Wiedergabe",
        "cancel":         "Abbrechen",
        "change":         "Ändern",
        "host":           "Host",
        "hosts":          "Hosts",
        "meeting":        "Meeting",
        "meetings":       "Meetings",
        "chat":           "Chat",
        "desktop":        "Desktop",
        "feedback":       "Feedback",
        "layout":         "Layout",
        "account":        "Konto",
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
        "asset":          "asset",
        "assets":         "asset",
        "history":        "cronologia",
        "host":           "host",
        "hosts":          "host",
        "exit":           "Esci",
        "play":           "Riproduci",
        "cancel":         "Annulla",
        "change":         "Cambia",
        "account":        "account",
        "chat":           "chat",
        "desktop":        "desktop",
        "feedback":       "feedback",
        "layout":         "layout",
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
        "volume":         "volume",
    },
}

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


# -- DeepL Glossary API --------------------------------------------------------

def build_glossary_tsv(lang_code):
    """Build TSV content for the glossary, including protected terms."""
    entries = dict(GLOSSARIES.get(lang_code, {}))
    for term in PROTECTED_TERMS:
        entries[term] = term
    return "\n".join(f"{src}\t{tgt}" for src, tgt in entries.items()), len(entries)


def create_glossary(lang_code):
    """
    Create a DeepL glossary using form-encoded data (required by v2 API).
    Returns glossary ID or None on failure.
    """
    if not DEEPL_API_KEY:
        raise ValueError("DEEPL_API_KEY environment variable is not set.")

    tsv_content, term_count = build_glossary_tsv(lang_code)
    if not tsv_content:
        print(f"  No glossary entries for {lang_code}, skipping.")
        return None

    # Delete any existing Avatour glossaries for this language pair
    auth_headers = {"Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}"}
    resp = requests.get(DEEPL_GLOSSARY_URL, headers=auth_headers, timeout=15)
    if resp.status_code == 200:
        for g in resp.json().get("glossaries", []):
            if (g.get("name", "").startswith("avatour-ui-")
                    and g.get("target_lang", "").upper() == lang_code.upper()):
                del_resp = requests.delete(
                    f"{DEEPL_GLOSSARY_URL}/{g['glossary_id']}",
                    headers=auth_headers, timeout=15
                )
                print(f"  Deleted old glossary: {g['name']} "
                      f"(status {del_resp.status_code})")
    else:
        print(f"  Warning: Could not list glossaries ({resp.status_code}): {resp.text}")

    # Create glossary using form-encoded data (NOT JSON — DeepL v2 requirement)
    resp = requests.post(
        DEEPL_GLOSSARY_URL,
        headers=auth_headers,   # no Content-Type — requests sets it for data=
        data={
            "name":           f"avatour-ui-{lang_code.lower()}",
            "source_lang":    "EN",
            "target_lang":    lang_code,
            "entries":        tsv_content,
            "entries_format": "tsv",
        },
        timeout=15
    )

    print(f"  Glossary create response: {resp.status_code}")
    if resp.status_code not in (200, 201):
        print(f"  WARNING: Could not create glossary: {resp.text}")
        print(f"  Continuing without glossary — manual review recommended.")
        return None

    result = resp.json()
    glossary_id = result["glossary_id"]
    ready = result.get("ready", False)
    print(f"  Glossary created: avatour-ui-{lang_code.lower()} "
          f"({term_count} terms, id={glossary_id}, ready={ready})")

    # Wait for glossary to be ready if needed
    if not ready:
        print("  Waiting for glossary to become ready...")
        for _ in range(10):
            time.sleep(2)
            check = requests.get(
                f"{DEEPL_GLOSSARY_URL}/{glossary_id}",
                headers=auth_headers, timeout=15
            )
            if check.status_code == 200 and check.json().get("ready"):
                print("  Glossary is ready.")
                break
        else:
            print("  Warning: Glossary may not be ready yet, proceeding anyway.")

    return glossary_id


def delete_glossary(glossary_id):
    """Remove a glossary from DeepL after use."""
    if not glossary_id:
        return
    headers = {"Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}"}
    resp = requests.delete(
        f"{DEEPL_GLOSSARY_URL}/{glossary_id}",
        headers=headers, timeout=15
    )
    print(f"  Glossary deleted: {glossary_id} (status {resp.status_code})")


# -- DeepL Translation API -----------------------------------------------------

def translate_batch(texts, target_lang, glossary_id=None):
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
    """Translate all values, skipping pure $t() refs and protecting placeholders."""
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

    with open(SOURCE_FILE, encoding="utf-8") as f:
        en_dict = json.load(f)

    print(f"Loaded {len(en_dict)} strings from en.json")
    DIST_DIR.mkdir(exist_ok=True)

    all_translations = {}

    for lang_code, lang_name in LANGUAGES.items():
        print(f"\nTranslating to {lang_name} ({lang_code})...")

        print("  Setting up glossary...")
        glossary_id = create_glossary(lang_code)
        if glossary_id:
            print(f"  Using glossary: {glossary_id}")
        else:
            print("  No glossary in use — terms may be inconsistent.")

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
