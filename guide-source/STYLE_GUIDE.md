# Avatour Guide — Editing Style Guide

This document explains how to edit and maintain the Avatour User & Best Practices Guide.

---

## Repository structure

```
test-repository/
  dist/
    avatour-guide.html           ← Standalone HTML (share with customers)
    avatour-guide-embed.html     ← Embedded on avatour.com via iframe
    avatour-guide-print.html     ← Open in Chrome → Save as PDF
    avatour-business-benefits.html  ← Separate page (not built by build.py)
  guide-source/
    Avatour User and Best Practices Guide.md  ← THE SOURCE FILE — edit this
    STYLE_GUIDE.md               ← This document
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
   - **pages build and deployment** — this is GitHub's own deployment process (ignore this one)
8. Click the most recent **Build Avatour Guide** run — wait for the green checkmark
9. Scroll to the bottom of the run page → **Artifacts** → click the zip file to download
10. Unzip → you have all three updated HTML files: `avatour-guide.html`, `avatour-guide-embed.html`, `avatour-guide-print.html`

**The Webflow embed updates automatically** — no action needed in Webflow.

Total time from saving in Typora to the website updating: about 2 minutes.

**Do you need to copy the downloaded files into your local `dist/` folder?**

No. The `dist/` folder in your local repository is just a local copy — the Actions bot commits the freshly built files back to GitHub automatically after every build. GitHub Desktop may show the `dist/` files as changed after a build; you can safely ignore this or pull the latest changes if you want your local copy to be current. The authoritative versions always live in the GitHub repository and are served from GitHub Pages.

---

## Production migration — pending (Prasad)

The current setup on Stefan's personal GitHub account is a test environment. When ready to move to production:

1. Create a repository in **Bitbucket** (Avatour's company standard)
2. Convert `build-guide.yml` to a **Bitbucket Pipelines** file (`bitbucket-pipelines.yml`) — same logic, different syntax
3. Host the embed file on **AWS S3** instead of GitHub Pages
4. Update the iframe `src` in Webflow once to point to the new S3 URL

Everything else — the MD source file, `build.py`, Typora workflow, and Cloudinary screenshots — moves across unchanged.

**Italian and Spanish translation — activate at migration time:**

Updated `build.py` and `build-guide.yml` files are already prepared in the Claude outputs folder. To activate:

1. Replace the current `build.py` and `build-guide.yml` with the prepared versions
2. Set up an Anthropic API account at **console.anthropic.com** using the Avatour company email
3. Add initial credits — set a monthly spend limit of ~$10 (a full translation run costs ~$0.10–0.30)
4. Add the API key as a Bitbucket Pipelines secret named `ANTHROPIC_API_KEY`
5. The build will then produce 9 output files: standalone, embed, and print for EN, IT, and ES
6. The guide header will show an EN / IT / ES language switcher

Until the API key is configured the build produces English only — no errors.

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

Without an explicit anchor the build auto-generates one from the heading text. Rules: lowercase, hyphens only, no spaces, unique within the file.

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

## Glossary

The Glossary section lives between these comments:

```
<!-- GLOSSARY_START — do not remove this comment -->
...
<!-- GLOSSARY_END — do not remove this comment -->
```

To add a term:
```markdown
**Your New Term**
The definition goes here. Keep it to 2-3 sentences.

*See also: Related Term*
```

The build script automatically adds hover tooltips wherever glossary terms appear in the body text — no manual tagging needed.

---

## FAQs

The FAQs section lives between these comments:

```
<!-- FAQS_START — do not remove this comment -->
...
<!-- FAQS_END — do not remove this comment -->
```

Structure:
```markdown
### Section Name

**Question goes here?**
Answer goes here on the next line. Can include [links](https://example.com).

**Another question?**
Another answer.
```

---

## What NOT to do

| ❌ Don't | ✅ Do instead |
|---------|--------------|
| `##Heading` without a space | `## Heading` — always a space after `#` |
| Indent text with spaces or Tab | Start all text at the left margin |
| Indent a `>` blockquote | Start `>` at the left margin |
| Use tables for layout | Only use tables for actual tabular data |
| Re-upload a screenshot to Cloudinary | Use the Replace workflow — keeps the URL stable |
| Delete `<!-- GLOSSARY_START -->` or `<!-- GLOSSARY_END -->` | Required by the build script |
| Delete `<!-- FAQS_START -->` or `<!-- FAQS_END -->` | Required by the build script |
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

> **Note:** Margins must be **Default** — this activates the CSS page margins and page numbers. Any other setting overrides them.

> **Note:** Turn off Chrome's built-in headers and footers — the guide already has its own running header and page numbers built in.

---

## How the Webflow embed works

The guide is embedded on avatour.com using a single iframe pointing to GitHub Pages:

```
https://stefan-hesse.github.io/test-repository/dist/avatour-guide-embed.html
```

The Webflow page contains only:
```html
<iframe src="https://stefan-hesse.github.io/test-repository/dist/avatour-guide-embed.html"
        width="100%"
        style="border:none; min-height:100vh;">
</iframe>
```

**You never need to touch Webflow when updating the guide.** Every push triggers a build and deploy automatically.

---

## Monthly update checklist

- [ ] Update the `updated:` date in the front matter at the top of the MD file
- [ ] Update any changed feature descriptions
- [ ] Add new features to the relevant section
- [ ] Update screenshots in Cloudinary using **Replace**
- [ ] Add new Glossary terms if needed
- [ ] Add new FAQs if needed
- [ ] Commit and push in GitHub Desktop — everything updates automatically

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

---

*Questions? Contact Stefan or open an issue in the GitHub repository.*
