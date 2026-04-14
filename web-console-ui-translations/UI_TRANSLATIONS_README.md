# Web Console UI Translations

Automated translation pipeline for the Avatour web console UI strings.

Translates `en.json` (English source) into Italian and German using the DeepL API,
with post-processing to correct known mistranslations and enforce Avatour terminology.

---

## Folder structure

```
web-console-ui-translations/
├── en.json          ← English source strings (from Prasad / Avatour app)
├── translate.py     ← Translation script
├── README.md        ← This file
└── dist/
    ├── it.json      ← Italian output (auto-generated, do not edit manually)
    ├── de.json      ← German output (auto-generated, do not edit manually)
    └── translations.xlsx  ← Combined review file (EN / IT / DE)
```

---

## How it works

1. `translate.py` reads `en.json`
2. For ~15 known problem keys per language, values are set directly via `PRE_TRANSLATIONS` — bypassing DeepL entirely
3. All remaining strings are sent to the DeepL API in batches of 50
4. Placeholders (`$t(key)`, `{{variable}}`, `<0>`, `</1>` etc.) are masked before translation and restored afterwards — so they are never translated or reordered
5. Post-processing fixes (`FIXES` and `SUBSTRING_FIXES`) correct any remaining known mistranslations
6. Output is written to `dist/it.json`, `dist/de.json`, and `dist/translations.xlsx`

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

### Important: clearing the cache

GitHub Actions only commits files that have changed. If the translations are
identical to what is already in `dist/`, nothing gets committed. This can happen
when only `translate.py` was updated (not `en.json`).

**To force a fresh run:** delete `dist/it.json`, `dist/de.json`, and
`dist/translations.xlsx` from the `dist/` folder, commit the deletion, push,
then trigger the workflow manually.

---

## Environment variables

| Variable | Where set | Description |
|---|---|---|
| `DEEPL_API_KEY` | GitHub repository secret | DeepL API key (free tier) |

---

## Adding or correcting a translation

### If DeepL produces a wrong single-word translation

Add the key to `PRE_TRANSLATIONS` in `translate.py` for the relevant language.
The key must match exactly the key in `en.json`. The value will be used directly,
bypassing DeepL.

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
5. Run the workflow — `dist/fr.json` will be produced automatically

---

## Delivering translations to Prasad

After the workflow runs successfully:

1. Pull the latest changes in GitHub Desktop to get the updated `dist/` files
2. Share `dist/it.json` and `dist/de.json` with Prasad
3. The `dist/translations.xlsx` file is for internal review only

Ask Prasad to confirm the expected format (JSON key-value, same structure as
`en.json`) and the target file locations in the app codebase.

---

## Known limitations

- **DeepL free tier**: 500,000 characters/month. The full translation of `en.json`
  (~498 strings) uses approximately 50,000–60,000 characters per language. Two
  languages = ~120,000 characters per run. This leaves comfortable headroom for
  monthly runs.
- **Placeholder protection**: The `<1>`, `</0>` style tags used by i18next are
  masked before translation. This prevents DeepL from reordering them, but the
  surrounding text may still be reordered slightly in complex sentences. Review
  `roi_title` and similar multi-placeholder strings carefully.
- **Formal register**: All translations use `formality: prefer_more` (formal Sie /
  Lei). If informal register is ever needed, change this in `translate_batch()`.

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
