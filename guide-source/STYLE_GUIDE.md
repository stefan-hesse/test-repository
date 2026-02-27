# Avatour Guide — Editing Style Guide

This document explains how to edit and maintain the Avatour User & Best Practices Guide source file.

---

## The setup

| Tool | Purpose |
|------|---------|
| **Typora** (Mac app) | Writing and editing the guide |
| **GitHub Desktop** (Mac app) | Syncing changes to GitHub |
| **GitHub** (github.com) | Stores the files, runs the automated build |
| **GitHub Actions** | Builds the three HTML outputs automatically on every push |

The source file is:
```
guide-source/Avatour User and Best Practices Guide.md
```

---

## The editing workflow (every time)

1. **Edit** in Typora — changes save automatically
2. **Open GitHub Desktop** — your changes appear highlighted in green/red
3. **Type a short summary** in the Summary field (e.g. `Updated Web Console section`)
4. **Click Commit to main**
5. **Click Push origin**
6. **Go to github.com → Actions tab** — a build starts automatically within seconds
7. When the green checkmark appears, **click the run → scroll to Artifacts → download the zip**
8. Unzip → open `avatour-guide.html` in your browser

Total time from saving in Typora to having the updated HTML: about 2 minutes.

---

## Basic Markdown syntax

| What you want | What you type |
|---------------|--------------|
| **Bold text** | `**Bold text**` |
| *Italic text* | `*Italic text*` |
| `Code or UI label` | `` `Code or UI label` `` |
| [Link text](URL) | `[Link text](https://example.com)` |
| Heading 1 (page title, use once) | `# Page Title` |
| Heading 2 (main section) | `## Section Name` |
| Heading 3 (subsection) | `### Subsection Name` |
| Heading 4 (sub-subsection) | `#### Sub-subsection` |
| Horizontal rule / divider | `---` |

---

## ⚠️ The most important rules

These are the mistakes most likely to break the HTML output. Check these first if something looks wrong.

### 1. Always put a space after the `#` symbols in headings

✅ Correct:
```markdown
## For All Avatour Users
### How to Join
```

❌ Wrong — the heading will not be recognised and the anchor ID will show as raw text:
```markdown
##For All Avatour Users
###How to Join
```

### 2. Never indent regular text

In Markdown, any line indented by 4 or more spaces (or a tab) becomes a grey monospace code block. This applies to paragraphs, lists, and blockquotes.

✅ Correct — text starts at the very left margin:
```markdown
You can join from any desktop, laptop, or smartphone.

- Item one
- Item two
```

❌ Wrong — indented text becomes an unintended code block:
```markdown
    You can join from any desktop, laptop, or smartphone.

    - Item one
    - Item two
```

**How to fix in Typora:** Select the affected lines and press **Shift+Tab** until they are back at the left margin.

**How to spot the problem in Typora:** Any grey monospace box that is not intentional code means something nearby is indented. Fix the indentation and it will disappear.

### 3. Blockquotes must start at the left margin

✅ Correct:
```markdown
> **Note:** Do NOT use the Avatour iOS / Android apps for joining meetings.
```

❌ Wrong — indented `>` becomes a code block instead of a callout:
```markdown
    > **Note:** Do NOT use the Avatour iOS / Android apps for joining meetings.
```

---

## Section anchors (for TOC links)

The left sidebar and right TOC are **generated automatically** from your headings — you do not need to maintain them manually. Every time you add or rename a heading, both sidebars update automatically on the next build.

Anchors are optional but recommended for clean, short URLs. Add them like this:

```markdown
## Web Console Overview {#web-console}
```

Without an explicit anchor, the build script auto-generates one from the heading text (e.g. `## For All Avatour Users` becomes `#for-all-avatour-users`). Either approach works.

**Rules for anchor IDs:**
- Lowercase letters, numbers, and hyphens only
- No spaces, no special characters
- Must be unique within the file

---

## Callout boxes (notes and tips)

Use blockquotes (`>`) for callout boxes. They render with an orange left border in the HTML output.

```markdown
> **Note:** Do NOT use the Avatour iOS / Android apps for joining meetings as a participant.
```

```markdown
> **Tip:** Enable Show Bitrate in Settings to diagnose connectivity issues.
```

```markdown
> **Admin only.** This section is only visible to Admin Users.
```

The word after `**` sets the label. The three standard labels are **Note**, **Tip**, and **Admin only**.

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

The header row renders automatically with the dark blue Avatour background. Only use tables for actual tabular data — never for layout or indentation.

---

## Adding a screenshot

Screenshots go BELOW the paragraph that introduces them, always with a caption on the line immediately after:

```markdown
Click **Workspaces** in the navigation menu and select the workspace you want.

![Brief description of what the screenshot shows — used as alt text](https://res.cloudinary.com/dxgt3r3bl/image/upload/avatour/guide/screenshots/FILENAME.png)
*This text becomes the visible caption below the image*
```

**Rules for screenshots:**
- Upload to Cloudinary at: `avatour/guide/screenshots/`
- Use a clear, descriptive filename: `web-console-menu.png` not `screenshot1.png`
- Always include alt text (inside `[...]`) — important for accessibility
- Always include a caption (the `*italic text*` on the line immediately after the image)
- To update a screenshot: upload the new file with the **same filename** to Cloudinary — the guide updates automatically, no link change needed

---

## Glossary

The Glossary section lives at the bottom of the file between these two comments:

```
<!-- GLOSSARY_START — do not remove this comment, it is used by the build script -->
...
<!-- GLOSSARY_END — do not remove this comment -->
```

**To add a new term:**

```markdown
**Your New Term**
The definition goes here as a plain paragraph. Keep it to 2-3 sentences.

*See also: Related Term, Another Term*
```

Leave a blank line between each term block.

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

**Question goes here?**
Answer goes here as a plain paragraph on the next line. Can include [links](https://example.com).

**Another question?**
Another answer.
```

Each `### Section Name` creates a collapsible section group. Each `**bold paragraph**` becomes a collapsible question. The paragraph immediately after it becomes the answer.

---

## What NOT to do

| ❌ Don't | ✅ Do instead |
|---------|--------------|
| `##Heading` without a space | `## Heading` — always a space after `#` |
| Indent text with spaces or Tab | Start all text at the left margin |
| Indent a `>` blockquote | Start `>` at the left margin |
| Use tables for layout/indentation | Only use tables for actual tabular data |
| Change a Cloudinary filename when updating a screenshot | Keep the same filename — the link stays valid |
| Delete `<!-- GLOSSARY_START -->` or `<!-- GLOSSARY_END -->` | These are required by the build script |
| Delete `<!-- FAQS_START -->` or `<!-- FAQS_END -->` | These are required by the build script |
| Manually edit the left sidebar or right TOC | Both are auto-generated from your headings |

---

## Build outputs

The build produces three files in the `dist/` folder:

| File | Purpose |
|------|---------|
| `avatour-guide.html` | Standalone file — share with customers to open in browser |
| `avatour-guide-embed.html` | For embedding in the Avatour website via iframe |
| `avatour-guide-print.html` | Open in Chrome → Cmd+P → Save as PDF |

---

## Monthly update checklist

When a new release ships:

- [ ] Update the `updated:` date in the front matter at the top of the MD file
- [ ] Update any changed feature descriptions
- [ ] Add any new features to the relevant section
- [ ] Upload new or updated screenshots to Cloudinary (keep filenames the same if replacing)
- [ ] Add any new terms to the Glossary
- [ ] Add any new FAQs
- [ ] Commit and push in GitHub Desktop — the build runs automatically

---

## Troubleshooting

| Problem in HTML output | Likely cause | Fix |
|------------------------|-------------|-----|
| Grey monospace code block (unintended) | Text or `>` is indented | Select lines in Typora → Shift+Tab |
| Anchor ID showing as text in heading | Missing space after `##` | Add space: `## Heading` |
| TOC link does not jump to section | Anchor mismatch | Check the `{#anchor-id}` matches exactly |
| Blockquote showing as code | `>` is indented | Move `>` to the left margin |
| Build fails in GitHub Actions | Syntax error in MD file | Check the Actions log for the error line |

---

*Questions? Contact Stefan or open an issue in the GitHub repository.*
