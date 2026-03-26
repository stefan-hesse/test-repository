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

import os, re, json
import urllib.request
import frontmatter
import markdown
from markdown.extensions.toc import TocExtension

# ── AUTO-TRANSLATE ────────────────────────────────────────────────────────
# Called in Step 1 of main(). Requires ANTHROPIC_API_KEY env variable.
# Compares current EN with EN-prev, translates only changed ## sections.

def split_sections(text):
    """Split markdown into list of (heading_line, body_text) tuples."""
    sections, heading, lines = [], '__preamble__', []
    for line in text.splitlines(keepends=True):
        if re.match(r'^## ', line):
            sections.append((heading, ''.join(lines)))
            heading, lines = line, []
        else:
            lines.append(line)
    sections.append((heading, ''.join(lines)))
    return sections

def translate_text(text, target_language, api_key):
    """Send text to Anthropic API and return translation."""
    payload = json.dumps({
        "model": "claude-opus-4-5",
        "max_tokens": 4096,
        "messages": [{"role": "user", "content":
            f"""Translate the following Markdown text to {target_language}.

Rules:
- Preserve ALL Markdown formatting exactly: headings, bold, italic, links, images, code, blockquotes, lists, anchor IDs like {{#anchor}}, horizontal rules
- Translate ONLY readable text — never translate URLs, image paths, anchor IDs, or code
- Return ONLY the translated Markdown — no preamble, no explanation

{text}"""}]
    }).encode('utf-8')
    req = urllib.request.Request(
        'https://api.anthropic.com/v1/messages',
        data=payload,
        headers={
            'Content-Type': 'application/json',
            'x-api-key': api_key,
            'anthropic-version': '2023-06-01',
        }
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())['content'][0]['text']

def auto_translate_lang(en_sections, en_prev_dict, lang_path, lang_name, api_key):
    """Translate changed EN sections into one language file."""
    # Load existing translation sections
    if os.path.exists(lang_path):
        with open(lang_path, 'r', encoding='utf-8') as f:
            lang_sections = {h: b for h, b in split_sections(f.read())}
    else:
        lang_sections = {}

    changed = 0
    for heading, body in en_sections:
        if en_prev_dict.get(heading, '') != body:
            # Translate heading + body together
            translated = translate_text(heading + body, lang_name, api_key)
            # Split translated result back into heading + body
            lines = translated.splitlines(keepends=True)
            if lines and re.match(r'^## ', lines[0]):
                lang_sections[heading] = (lines[0], ''.join(lines[1:]))
            else:
                lang_sections[heading] = (heading, translated)
            label = heading.strip()[:60] if heading != '__preamble__' else 'preamble'
            print(f"      ✓ {label}")
            changed += 1

    if changed == 0:
        print(f"    [{lang_name}] No changes — skipping")
        return False

    # Reassemble in EN order
    parts = []
    for heading, body in en_sections:
        if heading in lang_sections:
            val = lang_sections[heading]
            if isinstance(val, tuple):
                parts.append(val[0] + val[1])
            else:
                parts.append(heading + val)
        else:
            parts.append(heading + body)

    with open(lang_path, 'w', encoding='utf-8') as f:
        f.write(''.join(parts))
    print(f"    [{lang_name}] ✓ Written to {lang_path}")
    return True

def run_auto_translate():
    """Step 1: detect changed EN sections and translate to IT and ES."""
    api_key = os.environ.get('ANTHROPIC_API_KEY', '')
    if not api_key:
        print("  [TRANSLATE] No ANTHROPIC_API_KEY — skipping")
        return

    en_path      = "guide-source/Avatour User and Best Practices Guide.md"
    en_prev_path = "guide-source/Avatour User and Best Practices Guide - EN-prev.md"

    with open(en_path, 'r', encoding='utf-8') as f:
        en_text = f.read()

    en_sections  = split_sections(en_text)
    en_prev_dict = {}
    if os.path.exists(en_prev_path):
        with open(en_prev_path, 'r', encoding='utf-8') as f:
            en_prev_dict = {h: b for h, b in split_sections(f.read())}
    else:
        print("  [TRANSLATE] No EN-prev found — translating full document")

    total_changed = sum(1 for h, b in en_sections if en_prev_dict.get(h, '') != b)
    print(f"  [TRANSLATE] {total_changed} section(s) changed")

    if total_changed > 0:
        print("  [TRANSLATE] → Italian")
        auto_translate_lang(en_sections, en_prev_dict,
            "guide-source/Avatour User and Best Practices Guide - IT.md",
            "Italian", api_key)
        print("  [TRANSLATE] → Spanish")
        auto_translate_lang(en_sections, en_prev_dict,
            "guide-source/Avatour User and Best Practices Guide - ES.md",
            "Spanish", api_key)

    # Save current EN as new EN-prev
    import shutil
    shutil.copy2(en_path, en_prev_path)
    print(f"  [TRANSLATE] ✓ EN-prev updated")

DIST_DIR = "dist"

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

    print("\n── Step 1: Auto-translate ──────────────────────────────")
    run_auto_translate()

    print("\n── Step 2: Build HTML ──────────────────────────────────")
    for lang in LANGUAGES:
        build_outputs_for_lang(lang)
    print(f"\n  PDF: open any avatour-guide-print*.html in Chrome → Cmd+P → Save as PDF")


if __name__ == "__main__":
    print("\nAvatour Guide Builder")
    print("─" * 40)
    main()
    print("─" * 40)
    print("Done.\n")
