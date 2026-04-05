# Avatour Webflow Translation — README

This document covers everything you need to know to run, maintain, and expand the German translation of avatour.com.

---

## Repository structure

```
test-repository/
  guide-source/
    translate_webflow_de.py        ← Translation script — edit to add pages
    WEBFLOW_TRANSLATION_README.md  ← This document
  .github/
    workflows/
      translate-webflow-de.yml     ← GitHub Actions workflow — do not edit
```

---

## The tools

| Tool | Purpose |
|------|---------|
| **GitHub Desktop** (Mac app) | Committing and pushing script changes to GitHub |
| **GitHub** (github.com) | Stores the script, runs the workflow on demand |
| **GitHub Actions** | Manually triggered workflow that runs the translation |
| **Webflow Localization** | Stores EN and DE text nodes per page; serves `avatour.com/de/` when published |
| **Webflow Designer** | Used to preview DE pages and manually refine individual translations |
| **DeepL API** | Powers automatic EN → DE translation (free tier, 500,000 chars/month) |

---

## How it works

The script connects two APIs:

1. **Webflow API** — fetches the English text nodes for a page, then fetches the current German text nodes for the same page
2. **DeepL API** — translates each English node to German

Before translating, the script compares the current DE text against the EN text for each node:

- If DE text **equals** EN text → the node is still showing the English fallback → **translate it**
- If DE text **differs** from EN text → the node has been manually edited in Webflow → **skip it**

This means the workflow is **safe to re-run at any time** without overwriting manual edits. Only newly added or untouched nodes are ever translated automatically.

---

## Key IDs and secrets

| Item | Value |
|------|-------|
| Webflow Site ID | `6578f6bdfadb289687b7a7ad` |
| German Locale ID | `69d235ac4ced97b0b3403524` |
| German subdirectory | `avatour.com/de/` |
| GitHub secret: Webflow token | `WEBFLOW_API_TOKEN` |
| GitHub secret: DeepL key | `DEEPL_API_KEY` |

The Webflow API token requires **Pages: read/write** and **Sites: read** permissions. It was generated in Webflow → Site Settings → API access.

---

## Pages in scope

| Page | Page ID | Status |
|------|---------|--------|
| Homepage | `6578f6bdfadb289687b7a7d6` | ✅ Active |

To add a page to the pilot, add a line to the `PAGES` dict in `translate_webflow_de.py`:

```python
PAGES = {
    "Homepage":   "6578f6bdfadb289687b7a7d6",
    "Platform":   "YOUR_PAGE_ID_HERE",
}
```

Find any page's ID in the Webflow Designer URL bar when that page is open, or via the Webflow Pages API.

---

## Running the workflow

1. Go to **github.com/stefan-hesse/test-repository → Actions**
2. Click **"Translate Webflow to German (DE)"** in the left sidebar
3. Click **"Run workflow"**
4. Set the options:

| Option | Values | When to use |
|--------|--------|-------------|
| Page ID | blank = all pages; or paste a specific page ID | Leave blank for normal runs |
| dry_run | `false` (default) / `true` | Use `true` to test without pushing to Webflow |
| force | `false` (default) / `true` | Use `true` to re-translate everything, including manually edited nodes |

5. Click the green **Run workflow** button
6. Click the running job to watch the log

A successful run shows:
```
✓ 1/39: <h1 ...>See Every Site...
✓ 2/39: <h2 ...>Avatour is the 360°...
...
Translated: 39, Errors: 0
✓ Pushed 39 translated nodes to Webflow DE locale
✅ Done.
```

---

## Editing workflow

### For new or updated English content

When you update English copy on a page in Webflow:

1. Run the workflow (dry_run = `false`, force = `false`)
2. The script detects the new/changed nodes (still showing EN fallback) and translates them
3. Existing manually refined German nodes are left untouched
4. Preview the result in the Webflow Designer by switching to the DE locale

### For manually refining a translation

1. Open the Webflow Designer
2. Switch to the **DE locale** using the locale switcher in the top bar (EN → DE)
3. Click the text element you want to edit
4. Type your refined German text directly
5. Save — this node will now be skipped on all future translation runs

### To force a full re-translation (e.g. after a major copy refresh)

Run the workflow with **force = `true`**. This overwrites all nodes including manually edited ones. Use with care.

---

## Previewing the German site

The German locale is **not published** to `avatour.com/de/` during the pilot — it is only visible in the Webflow Designer.

To preview:

1. Open the Webflow Designer: [avatours-supercool-site.design.webflow.com](https://avatours-supercool-site.design.webflow.com)
2. Switch to **DE** in the locale switcher (top bar, shows "EN" by default)
3. Browse the pages to review translations

The staging subdomain (`avatours-supercool-site.webflow.io`) can also be used for a more realistic browser preview once the German locale is published to the staging domain.

---

## Publishing German to production

When the translation quality is satisfactory and you are ready to go live:

1. In Webflow Designer → Settings → Localization
2. Find **German** in the Supported locales table
3. Toggle **Enable publishing to the subdirectory** → On
4. Click **Save changes**
5. Add the Localization Essential plan ($9/month) when prompted
6. Publish the site — German pages will be live at `avatour.com/de/`

> **Note:** URL routing (auto-redirecting German-browser visitors to `/de/`) is currently **Off**. Enable this in Localization settings only after the translation has been reviewed and is ready for all German visitors.

---

## Localization setup (reference)

| Setting | Value |
|---------|-------|
| Primary locale | English (`en`) |
| German locale | `de` (no country) |
| German subdirectory | `/de` → `avatour.com/de/` |
| Publishing | Disabled during pilot |
| URL routing | Off |
| hreflang tags | Enabled (auto-generated) |

---

## What is and isn't translated automatically

| Content type | Translated by script? | Notes |
|---|---|---|
| Static page text nodes | ✅ Yes | All headings, body text, button labels |
| Navigation (TopBar component) | ❌ No | Component — requires separate handling |
| Footer component | ❌ No | Component — requires separate handling |
| CMS content (blog, articles) | ❌ No | Requires CSV export/import workflow |
| Images and alt text | ❌ No | Handled manually in Designer |
| SEO title and description | ❌ No | Update manually per page in Designer |
| Forms and form labels | ❌ No | Update manually in Designer |

Components (TopBar, Footer) require a different API call (`/components/{id}/dom`) — not yet implemented in the script. For the pilot, nav and footer remain in English.

---

## Cost

**DeepL:** Free tier includes 500,000 characters per month. A full homepage translation uses approximately 3,000 characters. Even translating 20 pages monthly stays well within the free limit.

**Webflow Localization:** $9/month per locale (Essential plan) — only required when publishing German to `avatour.com/de/`. Free during the pilot/preview phase.

---

## Troubleshooting

| Problem | Likely cause | Fix |
|---------|-------------|-----|
| `403 Forbidden` from DeepL | Wrong API endpoint | Free keys (ending `:fx`) must use `api-free.deepl.com` — already handled in script |
| `400 Validation Error` from Webflow | `localeId` not passed as query param | Already fixed — `localeId` is in the URL params, not the body |
| `No such file or directory` | Script not found at expected path | Confirm `translate_webflow_de.py` is in `guide-source/` |
| All nodes show `Already localised (skipped)` | Nodes were previously translated | Normal — run with `force=true` if you want to re-translate |
| `0` nodes fetched | Wrong page ID | Check page ID in `PAGES` dict matches the Webflow page |
| German text appears in English in Designer | Locale not switched | Click EN in top bar → switch to DE |
| Translation runs but Designer still shows EN | Page needs refresh | Close and reopen the page in Designer |
| Pages build and deployment also triggered | Normal GitHub Pages behaviour | Ignore — it always runs on push, unrelated to translation |

---

## Production migration — pending (Prasad)

The current setup on Stefan's personal GitHub account (`test-repository`) is a test environment. When ready to move to production:

1. Move the script to a repository in **Bitbucket** (Avatour's company standard)
2. Convert `translate-webflow-de.yml` to a **Bitbucket Pipelines** file (`bitbucket-pipelines.yml`) — same logic, different syntax
3. Add `WEBFLOW_API_TOKEN` and `DEEPL_API_KEY` as Bitbucket Pipelines secrets

The script itself (`translate_webflow_de.py`) moves across unchanged.

---

*Questions? Contact Stefan or open an issue in the GitHub repository.*

*This file: `guide-source/WEBFLOW_TRANSLATION_README.md`*
