# Avatour User Guide — README

This document covers everything you need to know to edit, build, and publish the Avatour User & Best Practices Guide.

---

## Repository structure

```
test-repository/
  dist/
    avatour-guide.html           ← Standalone HTML (share with customers)
    avatour-guide-embed.html     ← Embedded on avatour.com via iframe
    avatour-guide-print.html     ← Open in Chrome → Save as PDF
  guide-source/
    Avatour User and Best Practices Guide.md  ← THE SOURCE FILE — edit this
    GUIDE_README.md              ← This document
    build.py                     ← Build script — do not edit unless needed
  .github/
    workflows/
      build-guide.yml            ← GitHub Actions workflow — do not edit
```

> **Note:** You can ignore the local `dist/` folder entirely. The built HTML files are committed back to GitHub automatically by the Actions bot after every build. GitHub Desktop may show the `dist/` files as changed — just ignore this. Never commit changes to `dist/` manually. The only file you ever need to edit is `Avatour User and Best Practices Guide.md`.

---

## The tools

| Tool | Purpose |
|------|---------|
| **Typora** (Mac app) | Writing and editing the guide |
| **GitHub Desktop** (Mac app) | Committing and pushing changes to GitHub |
| **GitHub** (github.com) | Stores the files, runs the automated build |
| **GitHub Actions** | Builds the three HTML outputs automatically on every push |
| **GitHub Pages** | Hosts the embed file so Webflow can load it via iframe |
| **Cloudinary** | Hosts all screenshots used in the guide |

---

## The editing workflow (every time)

1. **Edit** `Avatour User and Best Practices Guide.md` in Typora — saves automatically
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
10. Unzip → you have all three updated HTML files

**The Webflow embed updates automatically** — no action needed in Webflow.

Total time from saving in Typora to the website updating: about 2 minutes.

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

**Fix in Typora:** Select the affected lines → press **Shift+Tab** until back at the left margin.
**How to spot it:** Any unexpected grey monospace box in Typora = something is indented.

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

The left sidebar and right TOC are generated automatically from your headings — no manual maintenance needed. Anchors are optional but recommended for clean short URLs:

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

**Refresh Typora after replacing:** Press **Cmd+Shift+R** — if that doesn't work, quit Typora and reopen the file.

---

## What NOT to do

| ❌ Don't | ✅ Do instead |
|---------|--------------|
| `##Heading` without a space | `## Heading` — always a space after `#` |
| Indent text with spaces or Tab | Start all text at the left margin |
| Indent a `>` blockquote | Start `>` at the left margin |
| Use tables for layout | Only use tables for actual tabular data |
| Re-upload a screenshot to Cloudinary | Use the Replace workflow — keeps the URL stable |
| Manually edit the sidebar or TOC | Both are auto-generated from your headings |

---

## Saving as PDF

Open `avatour-guide-print.html` in **Chrome** (not Safari or Firefox).

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

## How the Webflow embed works

Pages are hosted on GitHub Pages and embedded on avatour.com via a single iframe per page.

### GitHub Pages setup

GitHub Pages must be enabled on the repository. To check or enable it:

1. Go to **github.com/stefan-hesse/test-repository → Settings → Pages**
2. Under **Source**, select **Deploy from a branch**
3. Set branch to **main** and folder to **/ (root)**
4. Click **Save**

> **Note:** GitHub Pages requires a paid plan for private repositories. The repository is currently on **GitHub Pro** ($4/month). If the plan lapses or the repository visibility changes, Pages will return a 404 and the Webflow embeds will stop working.

### Currently hosted pages

| Page | GitHub Pages URL | Webflow page |
|------|-----------------|--------------|
| User & Best Practices Guide | `dist/avatour-guide-embed.html` | `/user-guide` |
| Business Benefits | `dist/avatour-business-benefits.html` | `/business-benefits` |

Base URL for all: `https://stefan-hesse.github.io/test-repository/`

> **Note — IT/ES translations pending:** Italian and Spanish guide versions are planned but not yet active. They will be added as part of the production migration to Bitbucket + AWS S3, using the Anthropic API for automated translation.

### Adding a new page

To host any additional standalone HTML page:

1. Place the `.html` file in the `dist/` folder of the repository
2. Commit and push via GitHub Desktop
3. GitHub Pages deploys it automatically within ~2 minutes
4. In Webflow, add a Section (zero padding, no container), drop an HTML Embed inside, and paste:

```html
<iframe src="https://stefan-hesse.github.io/test-repository/dist/[filename].html"
        width="100%"
        style="border:none; min-height:[height]px;">
</iframe>
```

Set `min-height` to match the page length — e.g. `100vh` for the guide, `3600px` for the Business Benefits page.

### Webflow page structure for iframe embeds

The iframe must sit directly inside the Section — not inside a container or padding wrapper:

```
Body
└── page-wrapper
    ├── TopBar
    ├── Section  ← zero padding, no max-width
    │   └── Code Embed  ← iframe goes here directly
    └── Footer
```

**You never need to touch Webflow when updating content.** Every push triggers a build and deploy automatically. The iframe picks up the new version within ~2 minutes.

---

## Keeping the repository clean

### .DS_Store files

macOS automatically creates `.DS_Store` files in every folder. A `.gitignore` is already in place to prevent them being committed:

```
.DS_Store
**/.DS_Store
```

If `.DS_Store` appears in the GitHub Desktop Changes panel, simply leave it **unchecked** before committing. If it was accidentally committed previously and keeps reappearing, run this once in Terminal from the repository folder:

```bash
git rm --cached .DS_Store
```

Then commit the removal ("Remove .DS_Store from tracking") and push — it will not reappear.

> **Note:** If Terminal shows `xcrun: error: invalid active developer path`, run `xcode-select --install` first to install the macOS Command Line Tools, then retry.

---

## Troubleshooting

| Problem | Likely cause | Fix |
|---------|-------------|-----|
| Grey monospace code block (unintended) | Text or `>` is indented | Select in Typora → Shift+Tab |
| Anchor ID showing as text in heading | Missing space after `##` | Add space: `## Heading` |
| Blockquote showing as code | `>` is indented | Move `>` to the left margin |
| Screenshot not updating in Typora | Image cache | Cmd+Shift+R, or quit and reopen |
| Build fails in GitHub Actions | Error in MD file | Check Actions log for the error line |
| TOC link doesn't jump to section | Anchor mismatch | Check `{#anchor-id}` matches exactly |
| Webflow page shows 404 | Page unpublished or missing in Webflow | Check Pages panel in Webflow Designer — republish or recreate the page |
| Webflow iframe shows 404 | GitHub Pages disabled or plan lapsed | Go to repo Settings → Pages and re-enable; check GitHub Pro plan is active |
| `.DS_Store` keeps appearing in GitHub Desktop | File was previously committed | Run `git rm --cached .DS_Store` in Terminal, then commit the removal |

---

## Production migration — pending (Prasad)

The current setup on Stefan's personal GitHub account (`test-repository`) is a test environment. When ready to move to production:

1. Create a repository in **Bitbucket** (Avatour's company standard)
2. Convert `build-guide.yml` to a **Bitbucket Pipelines** file (`bitbucket-pipelines.yml`) — same logic, different syntax
3. Host the embed file on **AWS S3** instead of GitHub Pages
4. Update the iframe `src` in Webflow once to point to the new S3 URL

Everything else — the MD source file, `build.py`, Typora workflow, and Cloudinary screenshots — moves across unchanged.

**Planned post-migration enhancements:**

- **Italian and Spanish translations** — automated via Anthropic API on every build. Updated `build.py` and `build-guide.yml` files are ready; requires an Anthropic API account set up under the Avatour company email and the API key added as a Bitbucket Pipelines secret (`ANTHROPIC_API_KEY`). Cost: ~$0.10–0.30 per full translation run. Monthly spend limit of ~$10 recommended.
- **Glossary for User Guide** — detailed internal glossary with hover tooltips on terms throughout the guide. Source files already exist from previous work.

---

*Questions? Contact Stefan or open an issue in the GitHub repository.*

*This file: `guide-source/GUIDE_README.md`*
