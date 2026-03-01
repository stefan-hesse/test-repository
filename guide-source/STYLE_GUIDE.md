# Avatour Guide — Editing Style Guide

This document explains how to edit and maintain the Avatour User & Best Practices Guide source file.

---

## Where the file lives

The source file is `guide-source/web-console.md` in the GitHub repository.

To edit it:
1. Go to the repository on GitHub
2. Click the file
3. Click the pencil icon (Edit this file)
4. Make your changes
5. Click **Commit changes** — the guide rebuilds automatically within 2 minutes

---

## Basic Markdown syntax

| What you want | What you type |
|---------------|--------------|
| **Bold text** | `**Bold text**` |
| *Italic text* | `*Italic text*` |
| `Code or UI label` | `` `Code or UI label` `` |
| [Link text](URL) | `[Link text](https://example.com)` |
| Heading 1 (page title) | `# Page Title` |
| Heading 2 (main section) | `## Section Name` |
| Heading 3 (subsection) | `### Subsection Name` |
| Heading 4 (sub-subsection) | `#### Sub-subsection` |

---

## Section anchors (required for TOC links)

Every heading that appears in the TOC must have an anchor ID. Add it like this:

```markdown
## Web Console Overview {#web-console}
```

The `{#web-console}` part creates the anchor. The TOC link `[Web Console](#web-console)` will then jump to this heading.

**Rule:** Use only lowercase letters, numbers, and hyphens in anchor IDs. No spaces.

---

## Adding a screenshot

Screenshots always go BELOW the paragraph that introduces them, and always have a caption:

```markdown
Click **Workspaces** in the navigation menu and select the workspace you want.

![Brief description of what the screenshot shows — used as alt text](https://res.cloudinary.com/dxgt3r3bl/image/upload/avatour/guide/screenshots/FILENAME.png)
*This text becomes the visible caption below the image*
```

**Rules for screenshots:**
- Upload to Cloudinary at: `avatour/guide/screenshots/`
- Use a clear, descriptive filename: `web-console-menu.png` not `screenshot1.png`
- Always include alt text (the text inside `[...]`) — this is important for accessibility
- Always include a caption (the `*text*` on the line immediately after)

**To update an existing screenshot — always use Replace, never re-upload:**

Do NOT upload the new file via the regular Upload button — Cloudinary will append a random suffix to keep the filename unique (e.g. `web-console-menu_x4rtko.png`), which breaks the link in your guide.

Instead:
1. Go to Cloudinary → navigate to `avatour/guide/screenshots/`
2. Find the existing file
3. Click the **three-dot menu (⋯)** on the file → **Replace**
4. Upload your new screenshot
5. Cloudinary keeps the exact same filename and URL — the guide updates automatically

**After replacing, refresh Typora to see the updated image:**
- Press **Cmd+Shift+R** to reload all images in the document
- If that does not work, quit Typora completely and reopen the file

---

## Callout boxes (notes and tips)

Use blockquotes (`>`) for callout boxes. They render with an orange left border.

```markdown
> **Note:** Do NOT use the Avatour iOS / Android apps for joining meetings as a participant.
```

```markdown
> **Tip:** Enable Show Bitrate in Settings to diagnose connectivity issues.
```

```markdown
> **Admin only.** This section is only visible to Admin Users.
```

The word after `**` sets the label colour — **Note**, **Tip**, and **Admin only** are the three standard labels.

---

## Numbered steps

Use a standard numbered list:

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

The header row (first row) automatically renders with the dark blue Avatour background.

---

## Glossary

The Glossary section lives at the bottom of the file between these two comments:

```
<!-- GLOSSARY_START — do not remove this comment -->
...
<!-- GLOSSARY_END — do not remove this comment -->
```

**To add a new glossary term:**

```markdown
**Your New Term**
The definition of the term goes here as a plain paragraph. Keep it to 2-3 sentences.
```

Leave a blank line between the term name and the next term.

**Important:** The build script automatically scans the body text and adds hover tooltips wherever glossary terms appear. You do NOT need to manually tag terms — just keep the glossary up to date.

---

## FAQs

The FAQs section lives between these two comments:

```
<!-- FAQS_START — do not remove this comment -->
...
<!-- FAQS_END — do not remove this comment -->
```

**Structure:**

```markdown
### Section Name

**Question goes here as a bold paragraph?**
Answer goes here as a plain paragraph on the next line. Can include [links](https://example.com).

**Another question?**
Another answer.
```

Each `### Section Name` creates a section heading in the FAQ list. Each `**bold paragraph**` becomes a collapsible question. The paragraph after it becomes the answer.

---

## What NOT to do

| ❌ Don't | ✅ Do instead |
|---------|--------------|
| Use coloured text in Confluence | Use callout boxes (`> **Note:**`) |
| Use tables for layout/alignment | Only use tables for actual tabular data |
| Skip the `{#anchor}` on headings | Always add anchors to section headings |
| Upload screenshots to Confluence | Always upload to Cloudinary at `avatour/guide/screenshots/` |
| Change the Cloudinary filename when updating a screenshot | Keep the same filename — the link stays valid |
| Delete `<!-- GLOSSARY_START -->` or `<!-- GLOSSARY_END -->` comments | These are required by the build script |
| Delete `<!-- FAQS_START -->` or `<!-- FAQS_END -->` comments | These are required by the build script |

---

## Running the build

From the repository root:

```bash
python guide-source/build.py
```

This produces three files in the `dist/` folder:

| File | Purpose |
|------|---------|
| `avatour-guide.html` | Standalone file — share with customers to open in browser |
| `avatour-guide-embed.html` | For embedding in the Avatour website via iframe |
| `avatour-guide-print.html` | Open in Chrome → Cmd+P → Save as PDF |

The GitHub Actions workflow runs this automatically on every commit to `main`. The built files are committed back to the repository and deployed to GitHub Pages automatically — no manual steps needed.

---

## How the Webflow embed works

The guide is embedded on the Avatour website using a single iframe. The iframe points to the embed file hosted on GitHub Pages:

```
https://stefan-hesse.github.io/test-repository/dist/avatour-guide-embed.html
```

The Webflow page contains only this code in an HTML Embed element:

```html
<iframe src="https://stefan-hesse.github.io/test-repository/dist/avatour-guide-embed.html"
        width="100%"
        style="border:none; min-height:100vh;">
</iframe>
```

**You never need to touch Webflow when updating the guide.** Every time you commit and push a content change, GitHub Actions rebuilds the embed file and deploys it to GitHub Pages automatically. The iframe on the Avatour website picks up the new version within a minute or two.

> **Note:** When the repository moves to the Avatour GitHub account, the GitHub Pages URL will change. At that point the iframe `src` in Webflow will need to be updated once to point to the new URL.

---

## Monthly update checklist

When a new release ships:

- [ ] Update the `updated:` date in the front matter at the top of the MD file
- [ ] Update any changed feature descriptions
- [ ] Add any new features to the relevant section
- [ ] Upload new or updated screenshots to Cloudinary using **Replace** (not re-upload)
- [ ] Add any new terms to the Glossary
- [ ] Add any new FAQs
- [ ] Commit and push in GitHub Desktop — build, deploy, and Webflow update happen automatically

---

*Questions? Contact Stefan or open an issue in the GitHub repository.*

---

## Saving as PDF

Open `avatour-guide-print.html` in **Chrome** (not Safari or Firefox — Chrome gives the best PDF output).

Press **Cmd+P** to open the print dialog, then set the following:

| Setting | Value |
|---------|-------|
| Destination | Save as PDF |
| Paper size | A4 |
| Margins | **Default** |
| Headers and footers | **Off** (untick this) |
| Background graphics | **On** (tick this — needed for coloured table headers) |

Click **Save**.

> **Note:** You must set Margins to **Default** — not None, not Custom. "Default" is what activates the CSS page margins defined in the build script, which give the correct spacing and room for the running page numbers. Any other margin setting will override them.

> **Note:** Turn off Chrome's built-in Headers and footers. The guide already has its own running header (guide title) and footer (page numbers + avatour.com) built into the CSS — if you leave Chrome's on, you will get both overlapping.
