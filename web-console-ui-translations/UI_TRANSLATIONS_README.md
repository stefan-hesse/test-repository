# Web Console UI Translations

Automated translation pipeline for the Avatour web console UI strings.

Translates `en.json` (English source) into Italian and German using the DeepL API Pro,
with post-processing to correct known mistranslations and enforce Avatour terminology.

---

## Folder structure

```
web-console-ui-translations/
├── en.json                   ← English source strings (from Prasad / Avatour app)
├── translate.py              ← Translation script
├── UI_TRANSLATIONS_README.md ← This file
└── dist/
    ├── it.json               ← Italian output
    ├── de.json               ← German output
    ├── en-prev.json          ← English snapshot from last run (delta detection)
    └── translations.xlsx     ← Combined review file (EN / IT / DE)
```

---

## How it works

1. `translate.py` reads `en.json` and compares it against `dist/en-prev.json`
   (the English snapshot from the previous run) to find which keys have changed
2. Only changed or new keys are sent to DeepL — existing translations are preserved
3. For ~15 known problem keys per language, values are set directly via
   `PRE_TRANSLATIONS`, bypassing DeepL entirely
4. A DeepL glossary enforces key terminology — notably `meeting → Meeting` and
   `meetings → Meetings` in German, preventing incorrect pluralisation
5. Placeholders (`$t(key)`, `{{variable}}`, `<0>`, `</1>` etc.) are masked before
   translation and restored afterwards — so they are never translated or reordered
6. Post-processing fixes (`FIXES` and `SUBSTRING_FIXES`) correct any remaining
   known mistranslations, including removing stray `@` characters that DeepL
   occasionally inserts after placeholder tags
7. Output is merged with existing translations and written to `dist/it.json`,
   `dist/de.json`, and `dist/translations.xlsx`
8. `dist/en-prev.json` is updated as a snapshot for the next run

**First run** (no `en-prev.json` exists): all keys are translated.
**Subsequent runs**: only keys whose English value changed are re-translated.
**Manual edits** to `it.json` or `de.json` are preserved as long as their
corresponding English key has not changed.

---

## Running the pipeline

### Automatic (GitHub Actions)

The workflow `translate-web-console-ui.yml` runs automatically when:
- `en.json` is updated on the `main` branch, **or**
- Triggered manually from the GitHub Actions tab

To trigger manually:
1. Go to the repository on GitHub.com
2. Click the **Actions** tab
3. Click **Translate Web Console UI** in the left sidebar
4. Click **Run workflow** → **Run workflow**

### Forcing a full re-translation

Normally the script only translates changed keys. To force a complete
re-translation of all strings (e.g. after a major script update):

Delete `dist/en-prev.json` from the `dist/` folder in Finder, commit the
deletion in GitHub Desktop, push, then trigger the workflow manually.
Without `en-prev.json` the script treats all keys as new and translates
everything from scratch.

---

## Making manual corrections

You can edit `dist/it.json` or `dist/de.json` directly in a text editor to fix
any translation. Your edits will be preserved on future runs as long as the
corresponding English key has not changed in `en.json`.

**Workflow:**
1. Open `dist/de.json` or `dist/it.json` in a text editor
2. Find the key and correct the value
3. Save, commit and push in GitHub Desktop

The next time the workflow runs, your correction will be kept — only keys with
new or changed English values will be re-translated by DeepL.

---

## Environment variables

| Variable | Where set | Description |
|---|---|---|
| `DEEPL_API_KEY` | GitHub repository secret | DeepL API Pro key (no `:fx` suffix) |

---

## Adding or correcting a translation at the source

For systematic corrections (same term always wrong), fix it in `translate.py`
rather than manually editing the output files each time.

### If DeepL produces a wrong single-word translation

Add the key to `PRE_TRANSLATIONS` in `translate.py`. The value will be used
directly, bypassing DeepL entirely for that key.

```python
PRE_TRANSLATIONS = {
    "DE": {
        "my_key": "Mein Wert",   ← add here
        ...
    },
```

### If DeepL produces a wrong multi-word or sentence translation

Add a tuple to `FIXES` in `translate.py`. The first element is the wrong DeepL
output (case-insensitive exact match), the second is the correct translation.

```python
FIXES = {
    "DE": [
        ("falsche Übersetzung", "richtige Übersetzung"),   ← add here
        ...
    ],
```

For corrections within longer strings (not the full value), add to
`SUBSTRING_FIXES` instead.

### If a new language is needed

1. Add the language to `LANGUAGES`:
   ```python
   LANGUAGES = {
       "IT": "Italian",
       "DE": "German",
       "FR": "French",   ← add here
   }
   ```
2. Add a `PRE_TRANSLATIONS["FR"]` dictionary with known problem terms
3. Add a `FIXES["FR"]` list (can start empty)
4. Add a `SUBSTRING_FIXES["FR"]` list (can start empty)
5. Delete `dist/en-prev.json`, commit, push, and trigger the workflow —
   `dist/fr.json` will be produced automatically

---

## Delivering translations to Prasad

After the workflow runs successfully:

1. Pull the latest changes in GitHub Desktop to get the updated `dist/` files
2. Share `dist/it.json` and `dist/de.json` with Prasad
3. Ask Prasad to confirm the target file locations in the app codebase
4. The `dist/translations.xlsx` file is for internal review only

---

## Known limitations

- **Placeholder protection**: The `<1>`, `</0>` style tags used by i18next are
  masked before translation. This prevents DeepL from reordering them, but the
  surrounding text may still be reordered slightly in complex sentences. Review
  `roi_title` and similar multi-placeholder strings carefully.
- **Formal register**: All translations use `formality: prefer_more` (formal Sie /
  Lei). If informal register is ever needed, change this in `translate_batch()`.
- **First-letter capitalisation**: All translated values have their first letter
  capitalised for DE and IT. This ensures German nouns are correctly capitalised
  and Italian labels look consistent. If the app applies CSS `text-transform` that
  conflicts, this can be removed by deleting the capitalisation block in
  `apply_fixes()`. Note that short words like conjunctions (`und`, `e`) and
  prepositions also get capitalised — add exceptions to `PRE_TRANSLATIONS` if any
  are problematic in context.
- **DeepL glossary**: The German glossary enforces `meeting → Meeting` /
  `meetings → Meetings`. Glossaries are immutable once created — to update,
  the script deletes and recreates the glossary on each run automatically.

---

## Key terminology decisions

| English | German | Italian | Rationale |
|---|---|---|---|
| assets | Assets | asset | Keep English — financial translation ("Vermögen") would confuse users |
| host | Host | host | Keep English — standard in both languages for software/meeting context |
| meeting | Meeting | riunione | German keeps English; Italian uses native word |
| history | Verlauf | cronologia | Navigation/app history, not world history |
| analytics | Analysen | analisi | Standard UI term |
| SuperFreeze | SuperFreeze | SuperFreeze | Product name — never translated |
| submit | einreichen | Invia | Italian pre-translated to avoid "Presente" (wrong) |

---

## Capitalisation

All translated values have their first letter capitalised automatically for both
DE and IT. German requires all nouns to be capitalised; Italian benefits from
consistent title-style capitalisation for UI labels.

The rule is simple: if the first character of a translated value is a lowercase
letter, it is uppercased. This means:
- Short labels: `passwort → Passwort`, `kamera → Kamera`, `filtri → Filtri`
- Sentences already starting with a capital are unaffected
- `$t()` references and `{{placeholders}}` starting with special characters are unaffected

Known minor side effects for native speaker review:
- Conjunctions (`und → Und`, `e → E`) and prepositions (`auf → Auf`, `su → Su`)
  get capitalised — these are rarely standalone labels but worth checking in context
- German `"on": "Auf"` was already a mistranslation (should be "Ein" for toggle);
  Italian `"on": "Su"` similarly
