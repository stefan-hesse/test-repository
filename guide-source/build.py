#!/usr/bin/env python3
"""
Avatour User Guide — Build Script
==================================
Builds three HTML outputs for each language from separate source files:

  Source files (in guide-source/):
    Avatour User and Best Practices Guide.md        → EN
    Avatour User and Best Practices Guide - IT.md   → IT
    Avatour User and Best Practices Guide - ES.md   → ES

  Outputs (in dist/):
    avatour-guide.html / -it.html / -es.html        → Standalone HTML
    avatour-guide-embed.html / -embed-it.html / -embed-es.html → Webflow embed
    avatour-guide-print.html / -print-it.html / -print-es.html → PDF-ready

Usage:
  python guide-source/build.py

Requirements:
  pip install markdown pymdown-extensions python-frontmatter --break-system-packages
"""

import os, re, json
import frontmatter
import markdown
from markdown.extensions.toc import TocExtension

# ── CONFIG ────────────────────────────────────────────────────────────────
DIST_DIR = "dist"

LANGUAGES = {
    "en": {
        "label":       "EN",
        "full":        "English",
        "suffix":      "",
        "source":      "guide-source/Avatour User and Best Practices Guide.md",
        "webflow_url": "https://avatour.com/user-guide",
    },
    "it": {
        "label":       "IT",
        "full":        "Italiano",
        "suffix":      "-it",
        "source":      "guide-source/Avatour User and Best Practices Guide - IT.md",
        "webflow_url": "https://avatour.com/user-guide-it",
    },
    "es": {
        "label":       "ES",
        "full":        "Español",
        "suffix":      "-es",
        "source":      "guide-source/Avatour User and Best Practices Guide - ES.md",
        "webflow_url": "https://avatour.com/user-guide-es",
    },
}

BRAND = {
    "blue":   "#132A39",
    "orange": "#FF4E00",
    "slate":  "#5A6875",
    "light":  "#E8EEF2",
    "border": "#DDE5EA",
    "text":   "#1A2A34",
    "muted":  "#7A8A95",
}

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
  font-family: 'Titillium Web', sans-serif;
  font-size: 17px; font-weight: 700;
  color: #fff; text-decoration: none; flex-shrink: 0;
}
.guide-logo svg { width: 26px; height: 26px; }
.hd { width:1px; height:20px; background:rgba(255,255,255,.2); flex-shrink:0; }
.hlabel {
  font-family:'Titillium Web',sans-serif; font-size:12px; font-weight:600;
  color:rgba(255,255,255,.5); letter-spacing:.09em; text-transform:uppercase;
}
.hright { margin-left:auto; display:flex; gap:12px; align-items:center; }

/* LANGUAGE SWITCHER */
.lang-switcher { display:flex; gap:4px; align-items:center; }
.lang-btn {
  font-family:'Titillium Web',sans-serif; font-size:11px; font-weight:700;
  letter-spacing:.06em; padding:4px 8px; border-radius:4px;
  border:1px solid rgba(255,255,255,.25); background:transparent;
  color:rgba(255,255,255,.6); cursor:pointer; text-decoration:none;
  transition:all .15s;
}
.lang-btn:hover { background:rgba(255,255,255,.1); color:#fff; }
.lang-btn.active { background:var(--orange); border-color:var(--orange); color:#fff; }
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
.guide-meta a { color: var(--orange); text-decoration: none; }

/* HEADINGS */
.guide-article h2 {
  font-family: 'Titillium Web', sans-serif;
  font-size: 20px; font-weight: 700; color: var(--blue);
  margin: 40px 0 12px;
  padding-top: 8px;
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
  font-size: 13px; font-weight: 700; color: var(--slate);
  text-transform: uppercase; letter-spacing: .07em;
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

/* BLOCKQUOTES (used for notes and tips) */
.guide-article blockquote {
  border-left: 3px solid var(--orange);
  background: #fff8f5;
  margin: 16px 0; padding: 11px 16px;
  border-radius: 0 6px 6px 0;
  font-size: 13.5px;
}
.guide-article blockquote p { margin-bottom: 0; color: #2a3a44; }
.guide-article blockquote strong { color: var(--orange); }

/* INLINE SCREENSHOTS */
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

/* ADMIN BADGE (inline in headings) */
.admin-badge {
  display: inline-block;
  font-size: 10px; font-weight: 700;
  font-family: 'Titillium Web', sans-serif;
  letter-spacing: .06em; text-transform: uppercase;
  padding: 2px 7px; border-radius: 3px;
  background: #fff0e8; color: #b83a00;
  vertical-align: middle; margin-left: 6px;
}

/* GLOSSARY TOOLTIPS */
.gloss-term {
  border-bottom: 1px dashed var(--orange);
  cursor: help; position: relative;
  color: inherit;
}
.gloss-term .gloss-tip {
  display: none;
  position: absolute; bottom: calc(100% + 6px); left: 50%;
  transform: translateX(-50%);
  background: var(--blue); color: #fff;
  font-size: 12px; line-height: 1.5;
  padding: 8px 12px; border-radius: 5px;
  width: 260px; z-index: 300;
  box-shadow: 0 4px 16px rgba(0,0,0,.2);
  pointer-events: none;
  font-family: 'Roboto', sans-serif;
  font-weight: 400;
  text-decoration: none;
}
.gloss-term .gloss-tip::after {
  content: '';
  position: absolute; top: 100%; left: 50%;
  transform: translateX(-50%);
  border: 5px solid transparent;
  border-top-color: var(--blue);
}
.gloss-term:hover .gloss-tip { display: block; }
.gloss-link {
  display: block; font-size: 11px; margin-top: 4px;
  color: var(--orange); text-decoration: none;
}

/* GLOSSARY SECTION */
.glossary-grid {
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 1px; background: var(--border);
  border: 1px solid var(--border); border-radius: 6px;
  overflow: hidden; margin: 16px 0;
}
.glossary-item {
  background: #fff; padding: 14px 16px;
}
.glossary-item:hover { background: #fafbfc; }
.glossary-term {
  font-family: 'Titillium Web', sans-serif;
  font-size: 13px; font-weight: 700; color: var(--blue);
  margin-bottom: 4px;
}
.glossary-def { font-size: 13px; color: var(--slate); line-height: 1.55; }

/* FAQS */
.faq-item {
  border-bottom: 1px solid var(--border);
}
.faq-item:last-child { border-bottom: none; }
.faq-q {
  font-family: 'Titillium Web', sans-serif;
  font-size: 14px; font-weight: 700; color: var(--blue);
  padding: 14px 0 14px 0;
  cursor: pointer;
  display: flex; justify-content: space-between; align-items: center;
  gap: 12px;
  list-style: none;
}
.faq-q::-webkit-details-marker { display: none; }
.faq-q::after {
  content: '+'; color: var(--orange); font-size: 20px;
  font-weight: 300; flex-shrink: 0; transition: transform .15s;
}
details[open] .faq-q::after { transform: rotate(45deg); }
.faq-a {
  padding: 0 0 14px 0;
  font-size: 13.5px; color: #2a3a44; line-height: 1.7;
}
.faq-section-title {
  font-family: 'Titillium Web', sans-serif;
  font-size: 11px; font-weight: 700;
  text-transform: uppercase; letter-spacing: .1em;
  color: var(--muted); margin: 24px 0 8px;
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



/* RELATED */


/* PRINT STYLES */
@media print {
  .guide-header, .guide-sidenav, .guide-toc,
  .guide-feedback, .guide-related { display: none !important; }
  .guide-main { margin-left: 0; padding-right: 0; }
  .guide-article { padding: 0; max-width: 100%; }
  .guide-article img { max-width: 80%; margin: 12px auto; }
  .gloss-term { border-bottom: none; }
  .gloss-term .gloss-tip { display: none !important; }
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
  .glossary-grid { grid-template-columns: 1fr; }
}

/* PDF / PRINT MODE */
body.print-mode .guide-header,
body.print-mode .guide-sidenav,
body.print-mode .guide-toc,
body.print-mode .guide-feedback,
body.print-mode .guide-related { display: none; }
body.print-mode { background: white; }
body.print-mode .guide-layout { padding-top: 0; }
body.print-mode .guide-main { margin-left: 0; padding-right: 0; }
body.print-mode body {
  font-size: 10.5pt;
  line-height: 1.5;
}
body.print-mode .guide-article {
  max-width: 100%;
  padding: 0;
  margin: 0;
  font-size: 10.5pt;
  line-height: 1.5;
}
body.print-mode .guide-article p { margin-bottom: 8px; }
body.print-mode .guide-article h1 { font-size: 20pt; margin-bottom: 6px; }
body.print-mode .guide-article h2 { font-size: 14pt; margin: 20px 0 8px; }
body.print-mode .guide-article h3 { font-size: 12pt; margin: 14px 0 6px; }
body.print-mode .guide-article h4 { font-size: 10pt; margin: 10px 0 4px; }
body.print-mode .guide-article li { margin-bottom: 3px; }
body.print-mode .guide-article table { font-size: 9.5pt; }
body.print-mode .guide-article blockquote { font-size: 10pt; padding: 8px 12px; margin: 10px 0; }
body.print-mode .glossary-def { font-size: 9.5pt; line-height: 1.45; }
body.print-mode .faq-q { font-size: 10.5pt; padding: 8px 0; }
body.print-mode .faq-a { font-size: 10pt; line-height: 1.5; }

/* Page setup: margins, running header/footer with page numbers */
@page {
  size: A4;
  margin: 20mm 18mm 22mm 18mm;
  @top-center {
    content: "Avatour User and Best Practices Guide";
    font-family: 'Titillium Web', sans-serif;
    font-size: 9pt;
    color: #7A8A95;
  }
  @bottom-left {
    content: "avatour.com";
    font-family: 'Titillium Web', sans-serif;
    font-size: 9pt;
    color: #7A8A95;
  }
  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
    font-family: 'Titillium Web', sans-serif;
    font-size: 9pt;
    color: #7A8A95;
  }
}

/* Avoid page breaks inside key elements */
body.print-mode .guide-article li,
body.print-mode .guide-article p,
body.print-mode .guide-article blockquote,
body.print-mode .guide-article tr { page-break-inside: avoid; }

/* Keep headings with the content that follows */
body.print-mode .guide-article h2,
body.print-mode .guide-article h3,
body.print-mode .guide-article h4 { page-break-after: avoid; }

/* Start each H2 section on a new page — but not the very first one */
body.print-mode .guide-article h2 ~ h2 { page-break-before: always; }

/* Images: never break, centered, max 90% width */
body.print-mode .guide-article img {
  max-width: 90%;
  display: block;
  margin: 12px auto;
  page-break-inside: avoid;
}

/* Tables: keep together where possible */
body.print-mode .guide-article table { page-break-inside: avoid; }

/* Glossary grid: single column for print */
body.print-mode .glossary-grid { grid-template-columns: 1fr 1fr; }

/* Remove orange dashed underlines from glossary terms in print */
body.print-mode .gloss-term { border-bottom: none; }
body.print-mode .gloss-term .gloss-tip { display: none !important; }

/* FAQ accordions: show all answers open in print */
body.print-mode details { display: block; }
body.print-mode details summary::after { display: none; }
body.print-mode .faq-a { display: block !important; padding-bottom: 10px; }
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

// FAQ feedback buttons
document.querySelectorAll('.fb-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const feedback = btn.closest('.guide-feedback');
    feedback.innerHTML = '<span style="color:var(--orange);font-weight:500">Thank you for your feedback!</span>';
  });
});
"""

# ── GLOSSARY DATA ─────────────────────────────────────────────────────────
def extract_glossary(md_text):
    """Extract glossary terms and definitions from the Markdown source."""
    glossary = {}
    in_glossary = False
    current_term = None
    current_def = []

    for line in md_text.splitlines():
        if "GLOSSARY_START" in line:
            in_glossary = True
            continue
        if "GLOSSARY_END" in line:
            if current_term:
                glossary[current_term] = " ".join(current_def).strip()
            in_glossary = False
            continue
        if not in_glossary:
            continue

        # Bold term on its own line
        term_match = re.match(r'^\*\*(.+?)\*\*\s*$', line.strip())
        if term_match:
            if current_term:
                glossary[current_term] = " ".join(current_def).strip()
            current_term = term_match.group(1)
            current_def = []
        elif current_term and line.strip():
            current_def.append(line.strip())

    return glossary


def extract_faqs(md_text):
    """Extract FAQ sections and Q&A pairs from the Markdown source."""
    faqs = []
    in_faqs = False
    current_section = None
    current_q = None
    current_a = []

    for line in md_text.splitlines():
        if "FAQS_START" in line:
            in_faqs = True
            continue
        if "FAQS_END" in line:
            if current_q:
                faqs.append((current_section, current_q, " ".join(current_a).strip()))
            in_faqs = False
            continue
        if not in_faqs:
            continue

        # Section heading (###)
        sec_match = re.match(r'^### (.+)$', line)
        if sec_match:
            if current_q:
                faqs.append((current_section, current_q, " ".join(current_a).strip()))
                current_q = None
                current_a = []
            current_section = sec_match.group(1)
            continue

        # Question (bold, starts with **)
        q_match = re.match(r'^\*\*(.+?)\*\*\s*$', line.strip())
        if q_match:
            if current_q:
                faqs.append((current_section, current_q, " ".join(current_a).strip()))
            current_q = q_match.group(1)
            current_a = []
        elif current_q and line.strip():
            current_a.append(line.strip())

    return faqs


def build_glossary_html(glossary):
    """Build the two-column glossary grid HTML."""
    items = ""
    for term, defn in sorted(glossary.items()):
        term_id = "gloss-" + re.sub(r'[^a-z0-9]', '-', term.lower())
        items += f"""
        <div class="glossary-item" id="{term_id}">
          <div class="glossary-term">{term}</div>
          <div class="glossary-def">{defn}</div>
        </div>"""
    return f'<div class="glossary-grid">{items}</div>'


def build_faq_html(faqs):
    """Build the FAQ accordion HTML."""
    html = ""
    current_section = None
    for section, question, answer in faqs:
        if section != current_section:
            current_section = section
            html += f'<div class="faq-section-title">{section}</div>\n'
        # Convert inline markdown links in answer
        answer = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', answer)
        html += f"""
        <details class="faq-item">
          <summary class="faq-q">{question}</summary>
          <div class="faq-a">{answer}</div>
        </details>"""
    return html


def auto_tag_glossary(html_content, glossary):
    """
    Scan body text and wrap glossary terms with tooltip spans.
    Skips headings, existing tags, image alt text, and the glossary section itself.
    Each term is tagged only on its FIRST occurrence to avoid clutter.
    """
    tagged = set()

    def replace_term(match, term, defn, term_id):
        word = match.group(0)
        if term in tagged:
            return word
        tagged.add(term)
        short_def = defn[:120] + "…" if len(defn) > 120 else defn
        return (
            f'<span class="gloss-term">{word}'
            f'<span class="gloss-tip">{short_def}'
            f'<a class="gloss-link" href="#{term_id}">See full definition →</a>'
            f'</span></span>'
        )

    # Sort longest terms first to avoid partial matches
    sorted_terms = sorted(glossary.keys(), key=len, reverse=True)

    # Process only paragraph and list content — skip headings and the glossary/FAQ sections
    # Split into segments: taggable vs non-taggable
    def process_segment(seg):
        for term in sorted_terms:
            if term in tagged:
                continue
            term_id = "gloss-" + re.sub(r'[^a-z0-9]', '-', term.lower())
            defn = glossary[term]
            pattern = r'(?<![a-zA-Z])' + re.escape(term) + r'(?![a-zA-Z])'
            seg = re.sub(
                pattern,
                lambda m, t=term, d=defn, tid=term_id: replace_term(m, t, d, tid),
                seg,
                count=1
            )
        return seg

    # Split HTML into taggable (<p>, <li>) and non-taggable (headings, code, glossary section)
    # Simple approach: process text between tags, skip heading tags and the glossary/faq divs
    result = []
    pos = 0
    # Find the glossary section start to avoid tagging there
    gloss_start = html_content.find('id="glossary"')
    tag_pattern = re.compile(r'<[^>]+>|[^<]+')

    in_skip = False
    skip_depth = 0
    in_heading = False

    for m in tag_pattern.finditer(html_content):
        chunk = m.group(0)
        if chunk.startswith('<'):
            tag_lower = chunk.lower()
            # Detect start of glossary/FAQ section — stop tagging after this
            if m.start() >= gloss_start and gloss_start > 0:
                result.append(chunk)
                continue
            # Skip headings
            if re.match(r'<h[1-6][\s>]', tag_lower):
                in_heading = True
            elif re.match(r'</h[1-6]>', tag_lower):
                in_heading = False
            result.append(chunk)
        else:
            if in_heading or (m.start() >= gloss_start > 0):
                result.append(chunk)
            else:
                result.append(process_segment(chunk))

    return ''.join(result)


def extract_headings(md_text):
    """
    Extract all H2/H3 headings from the Markdown source.
    Handles both explicit anchors {#anchor} and auto-generated slugs.
    Returns list of (level, title, anchor_id) tuples.
    Stops before Glossary/FAQs (always appended as fixed reference links).
    """
    headings = []
    stop_ids = {"glossary", "faqs"}

    for line in md_text.splitlines():
        m = re.match(r"^(#{2,3})\s+(.+)", line)
        if not m:
            continue
        level = len(m.group(1))
        raw = m.group(2).strip()

        # Extract explicit anchor {#anchor-id}
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
    """Build the right-side TOC automatically from MD headings."""
    headings = extract_headings(md_text)
    items = ""
    for level, title, anchor_id in headings:
        css = ' class="toc2"' if level == 3 else ""
        items += f'  <li{css}><a href="#{anchor_id}">{title}</a></li>\n'

    items += '  <li><a href="#glossary">Glossary</a></li>\n'
    items += '  <li><a href="#faqs">FAQs</a></li>\n'

    return f'<div class="toc-label">On this page</div>\n<ul>\n{items}</ul>'


def build_sidenav_html(md_text):
    """Build the left sidebar navigation automatically from MD headings."""
    headings = extract_headings(md_text)
    html = '<div class="sidenav-section">Guide sections</div>\n'

    for level, title, anchor_id in headings:
        css = ' class="sub"' if level == 3 else ""
        html += f'<a href="#{anchor_id}"{css}>{title}</a>\n'

    html += '<div class="sidenav-section">Reference</div>\n'
    html += '<a href="#glossary">Glossary</a>\n'
    html += '<a href="#faqs">FAQs</a>\n'
    html += '<a href="https://avatour.live/test">Network Test ↗</a>\n'
    html += '<a href="mailto:support@avatour.live">Open Support Ticket ↗</a>\n'

    return html


def md_to_html(md_text):
    """Convert Markdown to HTML using Python-Markdown with extensions."""
    # sane_lists: fixes mixed list handling
    # mdx_truly_sane_lists not available in all envs, so we pre-process
    # indentation instead: normalise 2-space indent → 4-space so Python-
    # Markdown recognises nested lists (Typora saves with 2-space indent)
    def normalise_list_indent(text):
        lines = text.split('\n')
        out = []
        for line in lines:
            # Count leading spaces
            stripped = line.lstrip(' ')
            spaces = len(line) - len(stripped)
            # If this looks like a list item (starts with - or * or digit.)
            # and has indentation, double the indent to convert 2→4, 4→8 etc.
            if spaces > 0 and stripped and stripped[0] in '-*' or (spaces > 0 and stripped and stripped[0].isdigit() and len(stripped) > 1 and stripped[1] in '.) '):
                line = ' ' * (spaces * 2) + stripped
            out.append(line)
        return '\n'.join(out)

    md_text = normalise_list_indent(md_text)

    md = markdown.Markdown(extensions=[
        TocExtension(slugify=lambda value, separator: re.sub(r'[^\w-]', '', value.lower().replace(' ', separator))),
        'tables',
        'fenced_code',
        'attr_list',
        'md_in_html',
        'sane_lists',
    ])
    return md.convert(md_text)


def replace_glossary_section(html, glossary_html):
    """Replace the auto-generated glossary section with the styled grid."""
    # The markdown renders ** terms as bold paragraphs — replace the whole section
    # with the pre-built grid between the h2#glossary and the next h2
    pattern = r'(<h2[^>]*id="glossary"[^>]*>.*?</h2>)(.*?)(<h2|$)'
    replacement = r'\1' + '\n' + glossary_html + '\n' + r'\3'
    result = re.sub(pattern, replacement, html, flags=re.DOTALL)
    return result


def replace_faq_section(html, faq_html):
    """Replace the auto-generated FAQ section with the accordion."""
    pattern = r'(<h2[^>]*id="faqs"[^>]*>.*?</h2>)(.*?)$'
    replacement = r'\1' + '\n' + faq_html + '\n'
    result = re.sub(pattern, replacement, html, flags=re.DOTALL)
    return result


LOGO_SVG = """<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="45" fill="#FF4E00"/>
  <ellipse cx="50" cy="50" rx="30" ry="20" stroke="white" stroke-width="5" fill="none"/>
  <circle cx="50" cy="50" r="8" fill="white"/>
</svg>"""


def build_full_html(article_html, toc_html, sidenav_html, meta, body_class=""):
    lang_code = meta.get('lang', 'en')
    lang_switcher = build_lang_switcher_html(lang_code, embed=False)
    return f"""<!DOCTYPE html>
<html lang="{lang_code}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{meta['title']} — Avatour</title>
<style>{CSS}</style>
</head>
<body{' class="' + body_class + '"' if body_class else ''}>

<header class="guide-header">
  <a class="guide-logo" href="#">
    {LOGO_SVG}
    AVATOUR
  </a>
  <div class="hd"></div>
  <span class="hlabel">User Guide</span>
  <div class="hright">
    {lang_switcher}
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
    """
    Webflow-compatible embed version.
    Fixes three Webflow-specific issues:
      1. Sidebar: shown but non-fixed (scrolls with page)
      2. FAQs: <details>/<summary> replaced with JS accordion (Webflow strips these)
      3. Glossary tooltips: CSS :hover replaced with JS mouseenter (more reliable in iframes)
    """
    # Fix 1: make all fixed/sticky positions work inside an iframe/embed
    embed_css = CSS.replace("position: fixed;", "position: sticky;")

    EMBED_EXTRA_CSS = """
/* WEBFLOW EMBED OVERRIDES */
.guide-header { display: none; }

/* Reset the standalone layout (which assumes fixed sidebars) */
.guide-layout {
  padding-top: 0;
  display: flex;
  align-items: flex-start;
  gap: 0;
}
.guide-sidenav { display: none !important; }
.guide-main {
  margin-left: 0 !important;
  padding-right: 0 !important;
  flex: 1;
  min-width: 0;
  display: flex;
  justify-content: flex-start;
  gap: 32px;
}
.guide-article {
  width: 100%;
  max-width: 780px;
  flex: 1;
}

/* TOC: JS-driven fixed position (CSS sticky breaks in Webflow embeds) */
.guide-toc {
  position: fixed;
  top: 20px;
  max-height: calc(100vh - 40px);
  overflow-y: auto;
  flex-shrink: 0;
  width: 190px;
  padding: 0 0 0 8px;
  right: 16px;
  z-index: 100;
}
/* Spacer so article column doesn't go under the fixed TOC */
.guide-main {
  padding-right: 220px !important;
}

/* Fix 2: JS-powered FAQ accordion (replaces <details>/<summary>) */
.faq-item { border-bottom: 1px solid var(--border); }
.faq-item:last-child { border-bottom: none; }
.faq-q {
  font-family: 'Titillium Web', sans-serif;
  font-size: 14px; font-weight: 700; color: var(--blue);
  padding: 14px 0; cursor: pointer;
  display: flex; justify-content: space-between; align-items: center;
  gap: 12px; list-style: none; border: none; background: none;
  width: 100%; text-align: left;
}
.faq-q .faq-icon {
  color: var(--orange); font-size: 20px; font-weight: 300;
  flex-shrink: 0; transition: transform .15s; line-height: 1;
}
.faq-q.open .faq-icon { transform: rotate(45deg); }
.faq-a {
  display: none; padding: 0 0 14px 0;
  font-size: 13.5px; color: #2a3a44; line-height: 1.7;
}
.faq-a.open { display: block; }
.faq-section-title {
  font-family: 'Titillium Web', sans-serif;
  font-size: 11px; font-weight: 700;
  text-transform: uppercase; letter-spacing: .1em;
  color: var(--muted); margin: 24px 0 8px;
}

/* Fix 3: JS-powered glossary tooltips */
.gloss-tip {
  display: none;
  position: absolute;
  background: var(--blue); color: #fff;
  font-size: 12px; line-height: 1.5;
  padding: 8px 12px; border-radius: 5px;
  width: 260px; z-index: 9999;
  box-shadow: 0 4px 16px rgba(0,0,0,.2);
  pointer-events: none;
  font-family: 'Roboto', sans-serif;
  top: 0; left: 0;
}
.gloss-tip::after {
  content: '';
  position: absolute; top: 100%; left: 20px;
  border: 5px solid transparent;
  border-top-color: var(--blue);
}
.gloss-tip.visible { display: block; }
.gloss-term {
  border-bottom: 1px dashed var(--orange);
  cursor: help;
}
"""

    # Fix 2: replace <details>/<summary> FAQ markup with plain div/button markup
    faq_html_fixed = article_html
    import re as _re
    # Replace <details class="faq-item"> ... </details> blocks with div+button pattern
    def replace_faq_block(m):
        inner = m.group(1)
        # Extract question from <summary class="faq-q">...</summary>
        q_match = _re.search(r'<summary[^>]*>(.*?)</summary>', inner, _re.DOTALL)
        # Extract answer from <div class="faq-a">...</div>
        a_match = _re.search(r'<div class="faq-a">(.*?)</div>', inner, _re.DOTALL)
        if not q_match or not a_match:
            return m.group(0)
        question = q_match.group(1).strip()
        answer = a_match.group(1).strip()
        return (
            f'<div class="faq-item">'
            f'<button class="faq-q"><span>{question}</span><span class="faq-icon">+</span></button>'
            f'<div class="faq-a">{answer}</div>'
            f'</div>'
        )
    faq_html_fixed = _re.sub(
        r'<details class="faq-item">(.*?)</details>',
        replace_faq_block,
        faq_html_fixed,
        flags=_re.DOTALL
    )

    EMBED_JS = """
// ── POST HEIGHT TO PARENT (so Webflow iframe resizes to content) ───────
function postHeight() {
  var h = document.body.scrollHeight;
  if (window.parent !== window) {
    window.parent.postMessage({ iframeHeight: h }, '*');
  }
}
// Post on load and after a short delay for images/fonts
window.addEventListener('load', function() {
  postHeight();
  setTimeout(postHeight, 800);
  setTimeout(postHeight, 2000);
});

// ── FAQ ACCORDION ──────────────────────────────────────────────────────
document.querySelectorAll('.faq-q').forEach(btn => {
  btn.addEventListener('click', () => {
    const answer = btn.nextElementSibling;
    const isOpen = btn.classList.contains('open');
    // Close all
    document.querySelectorAll('.faq-q').forEach(b => {
      b.classList.remove('open');
      b.nextElementSibling.classList.remove('open');
    });
    // Open this one if it was closed
    if (!isOpen) {
      btn.classList.add('open');
      answer.classList.add('open');
    }
  });
});

// ── GLOSSARY TOOLTIPS ──────────────────────────────────────────────────
const guideContainer = document.querySelector('.guide-layout') || document.body;
guideContainer.style.position = 'relative';
const tip = document.createElement('div');
tip.className = 'gloss-tip';
guideContainer.appendChild(tip);

document.querySelectorAll('.gloss-term').forEach(term => {
  const defn = term.getAttribute('data-def') || '';
  const href = term.getAttribute('data-href') || '#glossary';

  term.addEventListener('mouseenter', e => {
    tip.innerHTML = defn + '<a style="color:#FF4E00;font-size:11px;display:block;margin-top:6px;" href="' + href + '">See full definition →</a>';
    tip.style.display = 'block';
    positionTip(e);
  });
  term.addEventListener('mousemove', positionTip);
  term.addEventListener('mouseleave', () => { tip.style.display = 'none'; });
});

function positionTip(e) {
  const pad = 14;
  const w = tip.offsetWidth || 260;
  const h = tip.offsetHeight || 80;
  const rect = guideContainer.getBoundingClientRect();
  let x = e.clientX - rect.left + pad;
  let y = e.clientY - rect.top + window.scrollY - h - pad;
  if (x + w > guideContainer.offsetWidth) x = e.clientX - rect.left - w - pad;
  if (y - window.scrollY < 0) y = e.clientY - rect.top + window.scrollY + pad;
  tip.style.left = x + 'px';
  tip.style.top  = y + 'px';
}

// ── TOC: JS-DRIVEN POSITIONING (CSS sticky breaks in Webflow embeds) ──
const tocEl = document.querySelector('.guide-toc');
if (tocEl) {
  function positionTOC() {
    const rect = guideContainer.getBoundingClientRect();
    const rightGap = 16;
    // Position TOC fixed relative to viewport, aligned to right of guide container
    tocEl.style.right = Math.max(rightGap, window.innerWidth - rect.right + rightGap) + 'px';
    tocEl.style.top = Math.max(20, rect.top + 20) + 'px';
  }
  positionTOC();
  window.addEventListener('scroll', positionTOC, { passive: true });
  window.addEventListener('resize', positionTOC, { passive: true });
}

// ── ACTIVE TOC + SIDENAV ───────────────────────────────────────────────
const headings = document.querySelectorAll('.guide-article h2, .guide-article h3');
const tocLinks = document.querySelectorAll('.guide-toc a');
const sideLinks = document.querySelectorAll('.guide-sidenav a');
if (headings.length) {
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        const id = e.target.id;
        tocLinks.forEach(l => l.classList.toggle('active', l.getAttribute('href') === '#' + id));
        sideLinks.forEach(l => l.classList.toggle('active', l.getAttribute('href') === '#' + id));
      }
    });
  }, { rootMargin: '-10% 0px -80% 0px' });
  headings.forEach(h => { if (h.id) obs.observe(h); });
}


"""

    # Strip Glossary and FAQ sections entirely from the embed
    # (both live in the website footer as separate pages)
    import re as _re2
    faq_html_fixed = _re2.sub(
        r'<h2[^>]*id="glossary"[^>]*>.*',
        '',
        faq_html_fixed,
        flags=_re2.DOTALL
    )

    # Fix 3: rewrite gloss-term spans to use data attributes instead of nested HTML
    # (Webflow can mangle nested spans; data attributes are safer)
    def replace_gloss_span(m):
        # Extract the visible term text and the tooltip content
        full = m.group(0)
        term_text_m = _re2.search(r'^<span class="gloss-term">(.+?)<span class="gloss-tip">', full, _re2.DOTALL)
        tip_m = _re2.search(r'<span class="gloss-tip">(.*?)<a class="gloss-link"[^>]*href="([^"]+)"', full, _re2.DOTALL)
        if not term_text_m or not tip_m:
            return full
        term_text = term_text_m.group(1).strip()
        defn = tip_m.group(1).strip()
        href = tip_m.group(2)
        # Escape for data attribute
        defn_safe = defn.replace('"', '&quot;').replace("'", '&#39;')
        return f'<span class="gloss-term" data-def="{defn_safe}" data-href="{href}">{term_text}</span>'

    faq_html_fixed = _re2.sub(
        r'<span class="gloss-term">.*?</span></span>',
        replace_gloss_span,
        faq_html_fixed,
        flags=_re2.DOTALL
    )

    # Strip glossary/FAQ/reference links from sidenav for embed version
    embed_sidenav = _re2.sub(
        r'<div class="sidenav-section">Reference</div>.*',
        '',
        sidenav_html,
        flags=_re2.DOTALL
    )
    # Strip glossary/FAQ from TOC for embed version
    embed_toc = _re2.sub(
        r'<li><a href="#glossary">.*',
        '',
        toc_html,
        flags=_re2.DOTALL
    )

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
  <div class="guide-main">
    <article class="guide-article" style="padding-top: 24px;">
      {faq_html_fixed}
    </article>
    <aside class="guide-toc">
      {embed_toc}
    </aside>
  </div>
</div>
<script>{EMBED_JS}</script>
</body>
</html>"""


# ── MAIN ──────────────────────────────────────────────────────────────────
# Base URL for embed absolute links (GitHub Pages — update when migrating to S3)
EMBED_BASE_URL = "https://stefan-hesse.github.io/test-repository/dist"

def build_lang_switcher_html(active_lang, embed=False):
    """Build EN / IT / ES switcher buttons.
    Standalone: relative links between local HTML files.
    Embed: links to Webflow pages via window.top.location (breaks out of iframe).
    """
    buttons = []
    for code, info in LANGUAGES.items():
        suffix = info['suffix']
        active = ' active' if code == active_lang else ''
        if embed:
            # Navigate the parent Webflow page, not just the iframe
            webflow_url = info.get('webflow_url', '#')
            buttons.append(
                f'<a class="lang-btn{active}" href="{webflow_url}" '
                f'onclick="window.top.location.href=\'{ webflow_url }\'; return false;">'
                f'{info["label"]}</a>'
            )
        else:
            href = f"avatour-guide{suffix}.html"
            buttons.append(f'<a class="lang-btn{active}" href="{href}">{info["label"]}</a>')
    return f'<div class="lang-switcher">{"".join(buttons)}</div>'


def build_outputs_for_lang(md_text, meta, lang_code):
    """Run the full build pipeline for one language and write 3 output files."""
    info   = LANGUAGES[lang_code]
    suffix = info['suffix']

    lang_meta = dict(meta)
    lang_meta['lang'] = lang_code

    # Extract glossary and FAQs
    glossary = extract_glossary(md_text)
    faqs     = extract_faqs(md_text)

    # Convert Markdown → HTML
    article_html = md_to_html(md_text)

    # Replace raw glossary/FAQ sections with styled components
    glossary_html = build_glossary_html(glossary)
    faq_html      = build_faq_html(faqs)
    article_html  = replace_glossary_section(article_html, glossary_html)
    article_html  = replace_faq_section(article_html, faq_html)

    # Auto-tag glossary terms
    article_html = auto_tag_glossary(article_html, glossary)

    # Build navigation
    toc_html     = build_toc_html(md_text)
    sidenav_html = build_sidenav_html(md_text)

    # Output 1: Standalone HTML
    standalone = build_full_html(article_html, toc_html, sidenav_html, lang_meta)
    out1 = os.path.join(DIST_DIR, f"avatour-guide{suffix}.html")
    with open(out1, 'w', encoding='utf-8') as f:
        f.write(standalone)
    print(f"  ✓ Standalone  → {out1}")

    # Output 2: Embed HTML
    embed = build_embed_html(article_html, toc_html, sidenav_html, lang_meta)
    out2 = os.path.join(DIST_DIR, f"avatour-guide-embed{suffix}.html")
    with open(out2, 'w', encoding='utf-8') as f:
        f.write(embed)
    print(f"  ✓ Embed       → {out2}")

    # Output 3: Print/PDF HTML
    print_html = build_full_html(article_html, toc_html, sidenav_html, lang_meta, body_class="print-mode")
    out3 = os.path.join(DIST_DIR, f"avatour-guide-print{suffix}.html")
    with open(out3, 'w', encoding='utf-8') as f:
        f.write(print_html)
    print(f"  ✓ Print/PDF   → {out3}")


def main():
    os.makedirs(DIST_DIR, exist_ok=True)

    for lang_code, info in LANGUAGES.items():
        source_file = info['source']

        # Skip if source file doesn't exist yet
        if not os.path.exists(source_file):
            print(f"\n  [{lang_code.upper()}] Skipping — source file not found: {source_file}")
            continue

        post = frontmatter.load(source_file)
        meta = {
            'title':   post.get('title', 'Avatour User Guide'),
            'version': post.get('version', '2.0'),
            'updated': post.get('updated', '2026'),
        }

        print(f"\n  [{lang_code.upper()}] {info['full']} — building from {source_file}")
        build_outputs_for_lang(post.content, meta, lang_code)

    print(f"\n  To generate PDFs: open each avatour-guide-print*.html in Chrome → Cmd+P → Save as PDF")


if __name__ == "__main__":
    print("\nAvatour Guide Builder")
    print("─" * 40)
    main()
    print("─" * 40)
    print("Done.\n")
