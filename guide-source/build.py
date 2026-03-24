#!/usr/bin/env python3
"""
Avatour User Guide — Build Script
==================================
Converts guide-source/Avatour User and Best Practices Guide.md into three outputs:
  1. standalone HTML  → dist/avatour-guide.html
  2. embed HTML       → dist/avatour-guide-embed.html  (for Webflow iframe)
  3. PDF-ready HTML   → dist/avatour-guide-print.html  (open in Chrome → Cmd+P → Save as PDF)

Usage:
  python guide-source/build.py

Requirements:
  pip install markdown pymdown-extensions python-frontmatter
"""

import os, re
import frontmatter
import markdown
from markdown.extensions.toc import TocExtension

# ── CONFIG ────────────────────────────────────────────────────────────────
SOURCE_FILE = "guide-source/Avatour User and Best Practices Guide.md"
DIST_DIR    = "dist"

# ── CSS ───────────────────────────────────────────────────────────────────
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Titillium+Web:wght@300;400;600;700&family=Roboto:wght@300;400;500&display=swap');

:root {
  --blue:   #132A39;
  --orange: #FF4E00;
  --slate:  #5A6875;
  --light:  #E8EEF2;
  --border: #DDE5EA;
  --text:   #1A2A34;
  --muted:  #7A8A95;
  --sidebar-w: 240px;
  --toc-w:     220px;
  --header-h:  60px;
  --content-max: 680px;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Roboto', sans-serif;
  font-size: 15px; line-height: 1.8;
  color: var(--text); background: #fff;
}

/* HEADER */
.guide-header {
  position: fixed; top: 0; left: 0; right: 0;
  height: var(--header-h);
  background: var(--blue);
  display: flex; align-items: center;
  padding: 0 24px; z-index: 200; gap: 16px;
}
.guide-logo {
  display: flex; align-items: center; gap: 10px;
  text-decoration: none; flex-shrink: 0;
}
.hd { width:1px; height:20px; background:rgba(255,255,255,.2); flex-shrink:0; }
.hlabel {
  font-family:'Titillium Web',sans-serif; font-size:12px; font-weight:600;
  color:rgba(255,255,255,.5); letter-spacing:.09em; text-transform:uppercase;
}
.hright { margin-left:auto; display:flex; gap:12px; align-items:center; }
.hbtn {
  font-family:'Titillium Web',sans-serif; font-size:12px; font-weight:700;
  color:var(--blue); background:var(--orange);
  padding:6px 16px; border-radius:4px; text-decoration:none; flex-shrink:0;
}
.hversion {
  font-size:11px; color:rgba(255,255,255,.4);
  font-family:'Titillium Web',sans-serif; letter-spacing:.05em;
}

/* LAYOUT */
.guide-layout {
  display: flex; padding-top: var(--header-h); min-height: 100vh;
}

/* LEFT NAV */
.guide-sidenav {
  width: var(--sidebar-w); flex-shrink: 0;
  position: fixed; top: var(--header-h); left: 0; bottom: 0;
  background: #fafbfc; border-right: 1px solid var(--border);
  overflow-y: auto; padding: 20px 0 40px;
}
.sidenav-section {
  font-family: 'Titillium Web', sans-serif;
  font-size: 10px; font-weight: 700; letter-spacing: .12em;
  text-transform: uppercase; color: var(--muted);
  padding: 0 16px; margin: 20px 0 5px;
}
.sidenav-section:first-child { margin-top: 0; }
.guide-sidenav a {
  display: block; padding: 6px 16px;
  font-size: 13px; color: var(--slate);
  text-decoration: none; border-left: 3px solid transparent;
  transition: all .1s; line-height: 1.4;
}
.guide-sidenav a.sub { padding-left: 28px; font-size: 12.5px; }
.guide-sidenav a:hover,
.guide-sidenav a.active {
  color: var(--blue); background: var(--light);
  border-left-color: var(--orange);
}
.guide-sidenav a.active { font-weight: 500; }

/* MAIN WRAPPER */
.guide-main {
  margin-left: var(--sidebar-w); flex: 1;
  display: flex; justify-content: center;
  padding-right: var(--toc-w);
}

/* ARTICLE */
.guide-article {
  width: 100%; max-width: var(--content-max);
  padding: 44px 40px 80px;
}

/* BREADCRUMB */
.guide-bc {
  font-size: 12px; color: var(--muted);
  margin-bottom: 10px;
  display: flex; align-items: center; gap: 6px;
}
.guide-bc a { color: var(--muted); text-decoration: none; }
.guide-bc a:hover { color: var(--orange); }
.guide-bc span { opacity: .5; }

/* TITLE */
.guide-article h1 {
  font-family: 'Titillium Web', sans-serif;
  font-size: 28px; font-weight: 700; color: var(--blue);
  margin-bottom: 6px; line-height: 1.2;
}
.guide-meta {
  font-size: 12px; color: var(--muted);
  margin-bottom: 28px; padding-bottom: 20px;
  border-bottom: 1px solid var(--border);
}

/* HEADINGS */
.guide-article h2 {
  font-family: 'Titillium Web', sans-serif;
  font-size: 20px; font-weight: 700; color: var(--blue);
  margin: 40px 0 12px; padding-top: 8px;
  border-top: 2px solid var(--border);
  scroll-margin-top: calc(var(--header-h) + 16px);
}
.guide-article h3 {
  font-family: 'Titillium Web', sans-serif;
  font-size: 16px; font-weight: 700; color: var(--blue);
  margin: 28px 0 10px;
  scroll-margin-top: calc(var(--header-h) + 16px);
}
.guide-article h4 {
  font-family: 'Titillium Web', sans-serif;
  font-size: 30px; font-weight: 700; color: var(--slate);
  text-transform: none; letter-spacing: 0;
  margin: 20px 0 8px;
}

/* BODY */
.guide-article p { margin-bottom: 14px; }
.guide-article a { color: var(--orange); text-decoration: none; }
.guide-article a:hover { text-decoration: underline; }
.guide-article ul, .guide-article ol {
  padding-left: 22px; margin-bottom: 16px;
}
.guide-article li { margin-bottom: 6px; }
.guide-article li strong { color: var(--blue); }
.guide-article strong { color: var(--blue); }

/* TABLES */
.guide-article table {
  width: 100%; border-collapse: collapse;
  margin: 16px 0 20px; font-size: 13.5px;
  border: 1px solid var(--border); border-radius: 6px;
  overflow: hidden;
}
.guide-article th {
  background: var(--blue); color: #fff;
  font-family: 'Titillium Web', sans-serif;
  font-size: 12px; font-weight: 700;
  letter-spacing: .07em; text-transform: uppercase;
  padding: 9px 14px; text-align: left;
}
.guide-article td {
  padding: 9px 14px; border-bottom: 1px solid var(--border);
  vertical-align: top;
}
.guide-article tr:last-child td { border-bottom: none; }
.guide-article tr:nth-child(even) td { background: #f9fbfc; }

/* BLOCKQUOTES */
.guide-article blockquote {
  border-left: 3px solid var(--orange);
  background: #fff8f5;
  margin: 16px 0; padding: 11px 16px;
  border-radius: 0 6px 6px 0;
  font-size: 13.5px;
}
.guide-article blockquote p { margin-bottom: 0; color: #2a3a44; }
.guide-article blockquote strong { color: var(--orange); }

/* SCREENSHOTS */
.guide-article img {
  width: 100%; display: block;
  border: 1px solid var(--border);
  border-radius: 6px; margin: 20px 0 4px;
}
.guide-article img + em {
  display: block; font-size: 12px;
  color: var(--muted); text-align: center;
  margin-bottom: 20px; font-style: italic;
}

/* DIVIDER */
.guide-article hr {
  border: none; border-top: 1px solid var(--border); margin: 40px 0;
}

/* RIGHT TOC */
.guide-toc {
  width: var(--toc-w); flex-shrink: 0;
  position: fixed; top: calc(var(--header-h) + 44px); right: 0;
  padding: 0 20px;
  max-height: calc(100vh - var(--header-h) - 44px);
  overflow-y: auto;
}
.toc-label {
  font-family: 'Titillium Web', sans-serif;
  font-size: 10px; font-weight: 700; letter-spacing: .12em;
  text-transform: uppercase; color: var(--muted); margin-bottom: 10px;
}
.guide-toc ul { list-style: none; padding: 0; border-left: 2px solid var(--border); }
.guide-toc li a {
  display: block; padding: 4px 0 4px 12px;
  font-size: 12.5px; color: var(--slate); text-decoration: none;
  line-height: 1.4; border-left: 2px solid transparent; margin-left: -2px;
  transition: all .1s;
}
.guide-toc li a:hover { color: var(--blue); }
.guide-toc li a.active { color: var(--orange); border-left-color: var(--orange); font-weight: 500; }
.guide-toc li.toc2 a { padding-left: 22px; font-size: 12px; }

/* PRINT STYLES */
@media print {
  .guide-header, .guide-sidenav, .guide-toc { display: none !important; }
  .guide-main { margin-left: 0; padding-right: 0; }
  .guide-article { padding: 0; max-width: 100%; }
  .guide-article img { max-width: 100%; width: auto; display: block; margin: 12px auto; box-sizing: border-box; }
}

/* RESPONSIVE */
@media (max-width: 1100px) {
  .guide-toc { display: none; }
  .guide-main { padding-right: 0; }
}
@media (max-width: 780px) {
  .guide-sidenav { display: none; }
  .guide-main { margin-left: 0; }
  .guide-article { padding: 28px 20px 60px; }
}

/* PDF / PRINT MODE */
body.print-mode .guide-header,
body.print-mode .guide-sidenav,
body.print-mode .guide-toc { display: none; }
body.print-mode { background: white; }
body.print-mode .guide-layout { padding-top: 0; }
body.print-mode .guide-main {
  margin-left: 0 !important;
  padding-right: 0 !important;
  width: 100% !important;
  max-width: 100% !important;
  display: block !important;
}
body.print-mode .guide-article {
  width: 100%; max-width: 100%; padding: 0; margin: 0;
  font-size: 10.5pt; line-height: 1.5;
  overflow: hidden; box-sizing: border-box;
}
body.print-mode .guide-article p { margin-bottom: 8px; }
body.print-mode .guide-article h1 { font-size: 20pt; margin-bottom: 6px; }
body.print-mode .guide-article h2 { font-size: 14pt; margin: 20px 0 8px; }
body.print-mode .guide-article h3 { font-size: 12pt; margin: 14px 0 6px; }
body.print-mode .guide-article h4 { font-size: 10pt; margin: 10px 0 4px; }
body.print-mode .guide-article li { margin-bottom: 3px; }
body.print-mode .guide-article table { font-size: 9.5pt; }
body.print-mode .guide-article blockquote { font-size: 10pt; padding: 8px 12px; margin: 10px 0; }

@page {
  size: A4;
  margin: 20mm 18mm 22mm 18mm;
  @top-center {
    content: "Avatour User and Best Practices Guide";
    font-family: 'Titillium Web', sans-serif;
    font-size: 9pt; color: #7A8A95;
  }
  @bottom-left {
    content: "avatour.com";
    font-family: 'Titillium Web', sans-serif;
    font-size: 9pt; color: #7A8A95;
  }
  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
    font-family: 'Titillium Web', sans-serif;
    font-size: 9pt; color: #7A8A95;
  }
}

body.print-mode .guide-article li,
body.print-mode .guide-article p,
body.print-mode .guide-article blockquote,
body.print-mode .guide-article tr { page-break-inside: avoid; }
body.print-mode .guide-article h2,
body.print-mode .guide-article h3,
body.print-mode .guide-article h4 { page-break-after: avoid; }
body.print-mode .guide-article h2 ~ h2 { page-break-before: always; }
body.print-mode .guide-article img {
  max-width: 100%; width: auto; display: block;
  margin: 12px auto; page-break-inside: avoid;
  box-sizing: border-box; height: auto;
}
body.print-mode .guide-article table { page-break-inside: avoid; }
"""

# ── JAVASCRIPT ────────────────────────────────────────────────────────────
JS = """
// Active TOC highlighting
const headings = document.querySelectorAll('.guide-article h2, .guide-article h3');
const tocLinks = document.querySelectorAll('.guide-toc a');
if (headings.length && tocLinks.length) {
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        tocLinks.forEach(l => l.classList.remove('active'));
        const a = document.querySelector(`.guide-toc a[href="#${e.target.id}"]`);
        if (a) a.classList.add('active');
      }
    });
  }, { rootMargin: '-10% 0px -80% 0px' });
  headings.forEach(h => { if (h.id) obs.observe(h); });
}

// Active sidenav highlighting
const sideLinks = document.querySelectorAll('.guide-sidenav a');
const allH = document.querySelectorAll('.guide-article h2, .guide-article h3');
if (allH.length && sideLinks.length) {
  const obs2 = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        sideLinks.forEach(l => l.classList.remove('active'));
        const a = document.querySelector(`.guide-sidenav a[href="#${e.target.id}"]`);
        if (a) a.classList.add('active');
      }
    });
  }, { rootMargin: '-10% 0px -80% 0px' });
  allH.forEach(h => { if (h.id) obs2.observe(h); });
}
"""

# ── LOGO ──────────────────────────────────────────────────────────────────
LOGO_IMG = '<img src="https://res.cloudinary.com/avatour/image/upload/v1772627129/avatour-name-logo-whiteontransparent_zwfsxa.svg" alt="Avatour" style="height:22px; width:auto; display:block;">'


# ── HEADING EXTRACTION ────────────────────────────────────────────────────
def extract_headings(md_text):
    """Extract H2/H3 headings, return list of (level, title, anchor_id)."""
    headings = []
    stop_ids = {"glossary", "faqs"}

    for line in md_text.splitlines():
        m = re.match(r"^(#{2,3})\s+(.+)", line)
        if not m:
            continue
        level = len(m.group(1))
        raw = m.group(2).strip()

        anchor_match = re.search(r"\{#([\w-]+)\}", raw)
        if anchor_match:
            anchor_id = anchor_match.group(1)
            title = re.sub(r"\s*\{#[\w-]+\}", "", raw).strip()
        else:
            title = raw
            anchor_id = re.sub(r"[^\w\s-]", "", raw.lower())
            anchor_id = re.sub(r"\s+", "-", anchor_id.strip())
            anchor_id = re.sub(r"-+", "-", anchor_id)

        if anchor_id in stop_ids:
            break

        headings.append((level, title, anchor_id))

    return headings


def build_toc_html(md_text):
    """Build right-side TOC from headings."""
    headings = extract_headings(md_text)
    items = ""
    for level, title, anchor_id in headings:
        css = ' class="toc2"' if level == 3 else ""
        items += f'  <li{css}><a href="#{anchor_id}">{title}</a></li>\n'
    return f'<div class="toc-label">On this page</div>\n<ul>\n{items}</ul>'


def build_sidenav_html(md_text):
    """Build left sidebar from headings."""
    headings = extract_headings(md_text)
    html = '<div class="sidenav-section">Guide sections</div>\n'
    for level, title, anchor_id in headings:
        css = ' class="sub"' if level == 3 else ""
        html += f'<a href="#{anchor_id}"{css}>{title}</a>\n'
    html += '<div class="sidenav-section">Reference</div>\n'
    html += '<a href="https://avatour.com/glossary" target="_blank" rel="noopener">Glossary ↗</a>\n'
    html += '<a href="https://avatour.com/faqs" target="_blank" rel="noopener">FAQs ↗</a>\n'
    html += '<a href="https://avatour.live/test" target="_blank" rel="noopener">Network Test ↗</a>\n'
    return html


# ── MARKDOWN → HTML ───────────────────────────────────────────────────────
def md_to_html(md_text):
    """Convert Markdown to HTML. Normalises 2-space list indent to 4-space."""
    def normalise_list_indent(text):
        lines = text.split('\n')
        out = []
        for line in lines:
            stripped = line.lstrip(' ')
            spaces = len(line) - len(stripped)
            if spaces > 0 and stripped and (
                stripped[0] in '-*' or
                (stripped[0].isdigit() and len(stripped) > 1 and stripped[1] in '.) ')
            ):
                line = ' ' * (spaces * 2) + stripped
            out.append(line)
        return '\n'.join(out)

    md_text = normalise_list_indent(md_text)
    md = markdown.Markdown(extensions=[
        TocExtension(slugify=lambda value, separator: re.sub(r'[^\w-]', '', value.lower().replace(' ', separator))),
        'tables', 'fenced_code', 'attr_list', 'md_in_html', 'sane_lists',
    ])
    return md.convert(md_text)


# ── OPEN LINKS IN NEW TAB ─────────────────────────────────────────────────
def open_links_in_new_tab(html):
    """Add target=_blank to all external links."""
    def add_target(m):
        tag = m.group(0)
        href_m = re.search(r'href=["\']([^"\']*)["\']', tag)
        if href_m:
            url = href_m.group(1)
            if (url.startswith('http') or url.startswith('mailto')) and 'target=' not in tag:
                tag = tag[:-1] + ' target="_blank" rel="noopener">'
        return tag
    return re.sub(r'<a [^>]+>', add_target, html)


# ── HTML BUILDERS ─────────────────────────────────────────────────────────
def build_full_html(article_html, toc_html, sidenav_html, meta, body_class=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{meta['title']} — Avatour</title>
<style>{CSS}</style>
</head>
<body{' class="' + body_class + '"' if body_class else ''}>

<header class="guide-header">
  <a class="guide-logo" href="https://avatour.com" target="_blank" rel="noopener">
    {LOGO_IMG}
  </a>
  <div class="hd"></div>
  <span class="hlabel">User Guide</span>
  <div class="hright">
    <span class="hversion">v{meta.get('version','2.0')} · Updated {meta.get('updated','2026')}</span>
    <a class="hbtn" href="https://avatour.live">Log in to Avatour</a>
  </div>
</header>

<div class="guide-layout">

  <nav class="guide-sidenav">
    {sidenav_html}
  </nav>

  <div class="guide-main">
    <article class="guide-article">

      <div class="guide-bc">
        <a href="#">User Guide</a>
        <span>›</span>
        {meta['title']}
      </div>

      {article_html}

    </article>

    <aside class="guide-toc">
      {toc_html}
    </aside>
  </div>

</div>

<script>{JS}</script>
</body>
</html>"""


def build_embed_html(article_html, toc_html, sidenav_html, meta):
    """Webflow-compatible embed — no header, TOC only, iframe height reporting."""
    embed_css = CSS  # unchanged — fixed positioning works in the fixed-height iframe

    EMBED_EXTRA_CSS = """
/* ── WEBFLOW EMBED OVERRIDES ─────────────────────────────────────────── */

/* Hide the guide header and remove the space reserved for it */
.guide-header   { display: none !important; }
.guide-layout   { padding-top: 0 !important; }
.guide-toc      { display: none !important; }

/* Sidenav: fixed from top (no header), left:0 within the iframe.
   height uses calc to subtract top+bottom padding so all items are reachable */
.guide-sidenav {
  top: 0 !important;
  height: 100vh !important;
  max-height: 100vh !important;
  overflow-y: scroll !important;
  padding-bottom: 120px !important;
}

/* Main: margin accounts for the sidenav width */
.guide-main {
  margin-left: var(--sidebar-w) !important;
  padding-right: 40px !important;
  /* Prevent content overflowing the iframe width */
  max-width: calc(100% - var(--sidebar-w)) !important;
  box-sizing: border-box !important;
  overflow-x: hidden !important;
}

/* Article: constrained to its container */
.guide-article {
  max-width: 100% !important;
  box-sizing: border-box !important;
}

/* Layout: no horizontal overflow */
.guide-layout {
  overflow-x: hidden !important;
}

/* Scroll offset for anchor links */
.guide-article h2, .guide-article h3, .guide-article h4 {
  scroll-margin-top: 20px;
}
"""

    EMBED_JS = """
// ── ANCHOR LINKS ───────────────────────────────────────────────────────
// iframe has fixed height (100vh) set in Webflow and scrolls internally.
// postHeight is intentionally removed — auto-expanding the iframe height
// destroys internal scrolling and breaks position:sticky.
document.querySelectorAll('.guide-toc a[href^="#"]').forEach(function(link) {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    var id = this.getAttribute('href').slice(1);
    var target = document.getElementById(id);
    if (!target) return;
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});

// ── ACTIVE TOC HIGHLIGHTING ────────────────────────────────────────────
var headings = document.querySelectorAll('.guide-article h2, .guide-article h3');
var tocLinks = document.querySelectorAll('.guide-toc a');
if (headings.length) {
  var obs = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
      if (e.isIntersecting) {
        var id = e.target.id;
        tocLinks.forEach(function(l) {
          l.classList.toggle('active', l.getAttribute('href') === '#' + id);
        });
      }
    });
  }, { rootMargin: '-10% 0px -80% 0px' });
  headings.forEach(function(h) { if (h.id) obs.observe(h); });
}
"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{meta['title']} — Avatour</title>
<style>
{embed_css}
{EMBED_EXTRA_CSS}
</style>
</head>
<body>
<div class="guide-layout">
  <nav class="guide-sidenav">
    {sidenav_html}
  </nav>
  <div class="guide-main">
    <article class="guide-article" style="padding-top: 24px;">
      {article_html}
    </article>
  </div>
</div>
<script>{EMBED_JS}</script>
</body>
</html>"""


# ── MAIN ──────────────────────────────────────────────────────────────────
# ── LANGUAGE CONFIG ──────────────────────────────────────────────────────
# Add or remove languages here. 'suffix' is appended to output filenames.
# Source file is optional — if missing the language is skipped silently.
LANGUAGES = [
    {
        "code":    "en",
        "suffix":  "",
        "source":  "guide-source/Avatour User and Best Practices Guide.md",
        "webflow": "https://avatour.com/user-guide",
    },
    {
        "code":    "it",
        "suffix":  "-it",
        "source":  "guide-source/Avatour User and Best Practices Guide - IT.md",
        "webflow": "https://avatour.com/user-guide-it",
    },
    {
        "code":    "es",
        "suffix":  "-es",
        "source":  "guide-source/Avatour User and Best Practices Guide - ES.md",
        "webflow": "https://avatour.com/user-guide-es",
    },
]


def build_outputs_for_lang(lang):
    """Build all three outputs for one language. Skips if source missing."""
    source = lang["source"]
    suffix = lang["suffix"]
    code   = lang["code"]

    if not os.path.exists(source):
        print(f"  [{code.upper()}] Skipping — source not found: {source}")
        return

    post = frontmatter.load(source)
    md_text = post.content
    meta = {
        'title':   post.get('title', 'Avatour User Guide'),
        'version': post.get('version', '2.0'),
        'updated': post.get('updated', '2026'),
        'lang':    code,
    }

    print(f"  [{code.upper()}] Building from {source}")

    article_html = md_to_html(md_text)
    article_html = open_links_in_new_tab(article_html)
    toc_html     = build_toc_html(md_text)
    sidenav_html = build_sidenav_html(md_text)

    # Standalone
    out1 = os.path.join(DIST_DIR, f"avatour-guide{suffix}.html")
    with open(out1, 'w', encoding='utf-8') as f:
        f.write(build_full_html(article_html, toc_html, sidenav_html, meta))
    print(f"    ✓ Standalone  → {out1}")

    # Embed
    out2 = os.path.join(DIST_DIR, f"avatour-guide-embed{suffix}.html")
    with open(out2, 'w', encoding='utf-8') as f:
        f.write(build_embed_html(article_html, toc_html, sidenav_html, meta))
    print(f"    ✓ Embed       → {out2}")

    # Print/PDF
    out3 = os.path.join(DIST_DIR, f"avatour-guide-print{suffix}.html")
    with open(out3, 'w', encoding='utf-8') as f:
        f.write(build_full_html(article_html, toc_html, sidenav_html, meta, body_class="print-mode"))
    print(f"    ✓ Print/PDF   → {out3}")


def main():
    os.makedirs(DIST_DIR, exist_ok=True)
    for lang in LANGUAGES:
        build_outputs_for_lang(lang)
    print(f"\n  PDF: open any avatour-guide-print*.html in Chrome → Cmd+P → Save as PDF")


if __name__ == "__main__":
    print("\nAvatour Guide Builder")
    print("─" * 40)
    main()
    print("─" * 40)
    print("Done.\n")
