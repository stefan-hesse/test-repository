# Avatour User Guide — README

This document covers everything you need to know to edit, build, and publish the Avatour User & Best Practices Guide.

---

## Repository structure

```
test-repository/
  dist/
    avatour-guide.html              ← Standalone HTML — English (share with customers)
    avatour-guide-embed.html        ← Embedded on avatour.com/user-guide via iframe
    avatour-guide-print.html        ← Open in Chrome → Save as PDF — English
    avatour-guide-it.html           ← Standalone HTML — Italian
    avatour-guide-embed-it.html     ← Embedded on avatour.com/user-guide-it via iframe
    avatour-guide-print-it.html     ← PDF-ready — Italian
    avatour-guide-es.html           ← Standalone HTML — Spanish
    avatour-guide-embed-es.html     ← Embedded on avatour.com/user-guide-es via iframe
    avatour-guide-print-es.html     ← PDF-ready — Spanish
  guide-source/
    Avatour User and Best Practices Guide.md      ← English source — edit this
    Avatour User and Best Practices Guide - IT.md ← Italian source — edit this
    Avatour User and Best Practices Guide - ES.md ← Spanish source — edit this
    GUIDE_README.md                 ← This document
    build.py                        ← Build script — do not edit unless needed
  .github/
    workflows/
      build-guide.yml               ← GitHub Actions workflow — do not edit
```

> **Note:** Never edit files in `dist/` manually. They are rebuilt automatically on every push. GitHub Desktop may show `dist/` files as changed after a build — just ignore this. The only files you ever need to edit are the three Markdown source files.

---

## The tools

| Tool | Purpose |
|------|---------|
| **MacDown** (Mac app) | Writing and editing the guide source files |
| **GitHub Desktop** (Mac app) | Committing and pushing changes to GitHub |
| **GitHub** (github.com) | Stores the files, runs the automated build |
| **GitHub Actions** | Builds all nine HTML outputs automatically on every push |
| **GitHub Pages** | Hosts the embed files so Webflow can load them via iframe |
| **Cloudinary** | Hosts all screenshots used in the guide |

---

## The editing workflow (every time)

1. **Edit** the relevant Markdown source file in MacDown and save
2. **Open GitHub Desktop** — your changes appear highlighted in green/red
3. **Type a short summary** in the Summary field (e.g. `Update onsite operator section`)
4. **Click Commit to main**
5. **Click Push origin**
6. **Go to github.com → your test-repository → Actions tab** — a build starts automatically within seconds
7. You will see two types of runs in the list:
   - **Build Avatour Guide** — this is your build (the one that matters)
   - **pages build and deployment** — GitHub's own deployment process (ignore this one)
8. Click the most recent **Build Avatour Guide** run — wait for the green checkmark
9. Scroll to the bottom of the run page → **Artifacts** → click the zip file to download
10. Unzip → you have all nine updated HTML files

**The Webflow pages update automatically** — no action needed in Webflow after the build completes.

Total time from saving in MacDown to the website updating: about 2 minutes.

---

## Multi-language setup

The build script automatically detects which source files exist and builds only those languages. If a source file is missing, that language is silently skipped.

| Language | Source file | Webflow page |
|----------|------------|--------------|
| English | `Avatour User and Best Practices Guide.md` | `avatour.com/user-guide` |
| Italian | `Avatour User and Best Practices Guide - IT.md` | `avatour.com/user-guide-it` |
| Spanish | `Avatour User and Best Practices Guide - ES.md` | `avatour.com/user-guide-es` |

The language switcher (EN / IT / ES buttons) is a separate HTML embed above the iframe on each Webflow page — it is **not** part of the built HTML files.

---

## How the Webflow embed works

Each language has a dedicated Webflow page. The page contains two HTML embeds:

**Embed 1 — Language switcher** (above the iframe):
```html
<div style="display:flex; gap:8px; padding:8px 0;">
  <a href="/user-guide" style="...">EN</a>
  <a href="/user-guide-it" style="...">IT</a>
  <a href="/user-guide-es" style="...">ES</a>
</div>
```

**Embed 2 — The guide iframe:**
```html
<iframe
  src="https://stefan-hesse.github.io/test-repository/dist/avatour-guide-embed.html"
  width="100%"
  style="border:none; height:calc(100vh - 120px);"
  scrolling="yes">
</iframe>
```

> **Important:** The iframe height is `calc(100vh - 120px)` — this accounts for the Webflow navigation bars (~120px total) so the iframe fills exactly the visible area below the nav. The iframe scrolls internally; the guide's left sidebar ("Guide Sections") stays sticky within the iframe viewport.

For Italian use `avatour-guide-embed-it.html`, for Spanish use `avatour-guide-embed-es.html`.

**You never need to touch Webflow when updating the guide content.** Every push triggers a build and deploy automatically.

---

## Headings and anchors

### How deep to go with headings

The guide uses h1 through h4 as standard, with h5 acceptable for deeply nested technical specs (such as camera settings in section 5.3). The general rule:

| Level | Use for | Example |
|-------|---------|---------|
| `#` h1 | Page title only — once per file | `# Avatour User and Best Practices Guide` |
| `##` h2 | Main sections | `## 2. Avatour User Types` |
| `###` h3 | Subsections | `### 2.1 Meeting Attendees` |
| `####` h4 | Sub-subsections | `#### 2.1.1 Participant` |
| `#####` h5 | Deeply nested technical specs only | Camera settings sub-items in 5.3 |

**Avoid going deeper than h4 outside of section 5.3.** If you find yourself needing h5 elsewhere, consider restructuring the content instead — the sidebar only shows h2 and h3, so anything deeper is navigation-invisible anyway.

### What anchors are for

Anchors like `{#for-all-avatour-users}` on headings serve two purposes:

1. **Stable sidebar links** — without an anchor, the build script auto-generates one from the heading text. If you rephrase the heading, the auto-generated anchor changes and any existing links to it break. An explicit anchor stays stable regardless of how you rephrase the heading.
2. **Clean deep-link URLs** — lets you share a direct link like `avatour.com/user-guide#for-all-avatour-users` that reliably jumps to the right section.

**Anchors are only needed on h2 and h3 headings** — specifically those you want to link to externally or that appear in the sidebar. H4 and deeper do not need anchors.

Rules for anchor IDs: lowercase only, hyphens instead of spaces, no special characters, unique within the file.

```markdown
## Web Console Overview {#web-console-overview}
### 4.1 Getting Started {#getting-started}
```

---

## Basic Markdown rules

| What you want | What you type |
|---------------|--------------|
| **Bold text** | `**Bold text**` |
| *Italic text* | `*Italic text*` |
| `Code or UI label` | `` `Code or UI label` `` |
| [Link text](URL) | `[Link text](https://example.com)` |
| Heading 1 (page title, once only) | `# Page Title` |
| Heading 2 (main section) | `## Section Name` |
| Heading 3 (subsection) | `### Subsection Name` |
| Heading 4 (sub-subsection) | `#### Sub-subsection` |
| Horizontal rule / divider | `---` |

---

## ⚠️ The three rules that matter most

### 1. Always put a space after `#` in headings

✅ Correct:
```markdown
## For All Avatour Users
### How to Join
```
❌ Wrong — heading not recognised, anchor ID shows as raw text:
```markdown
##For All Avatour Users
###How to Join
```

### 2. Never indent regular text

Any line indented by 4+ spaces or a tab becomes a grey monospace code block.

✅ Correct — all text at the left margin:
```markdown
You can join from any desktop, laptop, or smartphone.

- Item one
- Item two
```
❌ Wrong — indented text becomes a code block:
```markdown
    You can join from any desktop, laptop, or smartphone.
```

**Fix in MacDown:** Select the affected lines and remove the leading spaces or tabs manually.
**How to spot it:** Any unexpected grey monospace box in MacDown's preview = something is indented.

### 3. Blockquotes must start at the left margin

✅ Correct:
```markdown
> **Note:** Do NOT use the Avatour iOS / Android apps for joining meetings.
```
❌ Wrong — indented `>` becomes a code block:
```markdown
    > **Note:** Do NOT use the Avatour iOS / Android apps for joining meetings.
```

---

## Section anchors

The left sidebar ("Guide Sections") is generated automatically from your headings — no manual maintenance needed. Anchors are optional but recommended for clean short URLs:

```markdown
## Web Console Overview {#web-console}
```

Rules: lowercase, hyphens only, no spaces, unique within the file.

---

## Callout boxes

```markdown
> **Note:** Do NOT use the Avatour iOS / Android apps for joining meetings as a participant.
```
```markdown
> **Tip:** Enable Show Bitrate in Settings to diagnose connectivity issues.
```
```markdown
> **Admin only.** This section is only visible to Admin Users.
```

The three standard labels are **Note**, **Tip**, and **Admin only**. They render with an orange left border.

---

## Numbered steps

```markdown
1. Open your preferred browser and go to [avatour.live](https://avatour.live)
2. Enter your name and the meeting code.
3. Click **Join** to enter the meeting.
```

---

## Tables

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Data     | Data     |
| Row 2    | Data     | Data     |
```

Header row renders automatically with the dark blue Avatour background. Only use tables for actual tabular data — never for layout.

---

## Adding a screenshot

Screenshots go BELOW the paragraph that introduces them, with a caption immediately after:

```markdown
Click **Workspaces** in the navigation menu to open the workspace list.

![The Avatour Web Console workspace list](https://res.cloudinary.com/avatour/image/upload/avatour/guide/screenshots/FILENAME.png)
*The workspace list showing all available workspaces*
```

**Cloudinary path:** `avatour/guide/screenshots/`
**Filename rules:** lowercase, hyphens, descriptive — e.g. `web-console-menu.png` not `screenshot1.png`

**To update an existing screenshot — always use Replace, never re-upload:**

If you use the regular Upload button, Cloudinary appends a random suffix (e.g. `web-console-menu_x4rtko.png`) which breaks the link in your guide.

1. Go to Cloudinary → `avatour/guide/screenshots/`
2. Find the existing file
3. Click the **three-dot menu (⋯)** → **Replace**
4. Upload your new screenshot
5. Cloudinary keeps the exact same URL — the guide updates automatically

**Refresh MacDown after replacing:** Press **Cmd+R** to reload — if that doesn't work, close and reopen the file.

---

## What NOT to do

| ❌ Don't | ✅ Do instead |
|---------|--------------|
| `##Heading` without a space | `## Heading` — always a space after `#` |
| Indent text with spaces or Tab | Start all text at the left margin |
| Indent a `>` blockquote | Start `>` at the left margin |
| Use tables for layout | Only use tables for actual tabular data |
| Re-upload a screenshot to Cloudinary | Use the Replace workflow — keeps the URL stable |
| Manually edit the sidebar | It is auto-generated from your headings |
| Edit files in `dist/` | They are rebuilt automatically — changes will be overwritten |

---

## Saving as PDF

Open `avatour-guide-print.html` (or `-it` / `-es`) in **Chrome** (not Safari or Firefox).

Press **Cmd+P**, then set:

| Setting | Value |
|---------|-------|
| Destination | Save as PDF |
| Paper size | A4 |
| Margins | **Default** |
| Headers and footers | **Off** |
| Background graphics | **On** |

> **Note:** Margins must be **Default** — this activates the CSS page margins and page numbers built into the guide.

> **Note:** Turn off Chrome's built-in headers and footers — the guide already has its own running header and page numbers.

---

## Troubleshooting

| Problem | Likely cause | Fix |
|---------|-------------|-----|
| Grey monospace code block (unintended) | Text or `>` is indented | Select in MacDown and remove leading spaces/tabs |
| Anchor ID showing as text in heading | Missing space after `##` | Add space: `## Heading` |
| Blockquote showing as code | `>` is indented | Move `>` to the left margin |
| Screenshot not updating in Typora | Image cache | Cmd+Shift+R, or quit and reopen |
| Build fails in GitHub Actions | Error in MD file | Check Actions log for the error line |
| Sidebar link doesn't jump to section | Anchor mismatch | Check `{#anchor-id}` matches exactly |
| Italian/Spanish page not loading | Wrong filename casing | Must be lowercase: `avatour-guide-embed-it.html` not `-IT.html` |

---

## Updating the Italian and Spanish translations

When you update the English source file, you do not need to re-translate the entire document. Instead:

1. Upload the **updated English MD file** here in Claude
2. Upload the **current Italian MD file** (`Avatour User and Best Practices Guide - IT.md`)
3. Upload the **current Spanish MD file** (`Avatour User and Best Practices Guide - ES.md`)
4. Say: *"Please update the Italian and Spanish translations to match the updated English version"*

Claude will compare the English versions, identify exactly what changed, and apply only those changes to the IT and ES files — leaving everything else untouched. You only need to review the changed sections rather than the whole document.

> **Note:** If you don't have the current IT/ES files to hand, Claude can re-translate the full document from scratch — just upload the updated English file and ask for a full translation.

---

## Production migration — pending (Prasad)

The current setup on Stefan's personal GitHub account (`test-repository`) is a test environment. When ready to move to production:

1. Create a repository in **Bitbucket** (Avatour's company standard)
2. Convert `build-guide.yml` to a **Bitbucket Pipelines** file (`bitbucket-pipelines.yml`) — same logic, different syntax
3. Host the embed files on **AWS S3** instead of GitHub Pages
4. Update the three iframe `src` values in Webflow to point to the new S3 URLs

Everything else — the three MD source files, `build.py`, Typora workflow, and Cloudinary screenshots — moves across unchanged.

**Planned post-migration enhancements:**

- **Automated re-translation** — when the English source changes, IT and ES can be re-translated automatically via the Anthropic API on every build. Requires an Anthropic API account under the Avatour company email and the key added as a Bitbucket Pipelines secret (`ANTHROPIC_API_KEY`). Cost: ~$0.10–0.30 per full build run.
- **Glossary for User Guide** — detailed internal glossary with hover tooltips on terms throughout the guide. Source files from previous work are available.

---

*Questions? Contact Stefan or open an issue in the GitHub repository.*

*This file: `guide-source/GUIDE_README.md`*
