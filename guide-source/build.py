#!/usr/bin/env python3
"""
Avatour User Guide — Build Script
==================================
Converts guide-source/Avatour User and Best Practices Guide.md into three outputs:
  1. standalone HTML  → dist/avatour-guide.html
  2. embed HTML       → dist/avatour-guide-embed.html  (for Webflow iframe)
  3. PDF-ready HTML   → dist/avatour-guide-print.html  (open in Chrome → Cmd+P → Save as PDF)

Translation uses the DeepL API. Brand names and agreed terms are kept consistent with a DeepL
glossary that is built from guide-source/deepl-glossary.csv (see GUIDE_README.md).

Usage:
  python guide-source/build.py

Requirements:
  pip install markdown pymdown-extensions python-frontmatter
"""

import os, re, json, time, csv, hashlib
import urllib.request
import urllib.parse
import urllib.error
import frontmatter
import markdown
from markdown.extensions.toc import TocExtension

# ── AUTO-TRANSLATE ────────────────────────────────────────────────────────
# Called in Step 1 of main(). Requires DEEPL_API_KEY env variable.
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

# ── DEEPL API HELPERS ─────────────────────────────────────────────────────
# DEEPL_API_URL can be overridden with an environment variable (for example to
# use the Free plan endpoint, or a local test server in the automated tests).
DEEPL_API_URL = os.environ.get('DEEPL_API_URL', 'https://api.deepl.com').rstrip('/')

class DeepLError(Exception):
    """A DeepL API call failed. `status` is the HTTP status (0 = network problem)."""
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status

def deepl_http(method, path, api_key, data=None, json_body=None, retries=3):
    """Call the DeepL API and return the parsed JSON (None for an empty answer).
    Retries HTTP 429 and 5xx with exponential backoff, as DeepL recommends.
    400 and 456 are never retried."""
    url = DEEPL_API_URL + path
    headers = {'Authorization': f'DeepL-Auth-Key {api_key}'}
    body = None
    if json_body is not None:
        body = json.dumps(json_body).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    elif data is not None:
        body = data
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
    attempt = 0
    while True:
        req = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read()
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as e:
            detail = e.read().decode('utf-8', 'replace')[:300]
            trace = e.headers.get('X-Trace-ID', '') if e.headers else ''
            if (e.code == 429 or e.code >= 500) and attempt < retries:
                wait = 2 ** (attempt + 1)
                print(f"    [DEEPL] HTTP {e.code} on {method} {path} — retrying in {wait}s")
                time.sleep(wait)
                attempt += 1
                continue
            raise DeepLError(e.code, f"HTTP {e.code} on {method} {path}: {detail} (trace {trace})")
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt < retries:
                wait = 2 ** (attempt + 1)
                print(f"    [DEEPL] Network problem on {method} {path} ({e}) — retrying in {wait}s")
                time.sleep(wait)
                attempt += 1
                continue
            raise DeepLError(0, f"Network problem on {method} {path}: {e}")

def gh_warning(message):
    """Print a warning that GitHub Actions shows as a yellow annotation on the run."""
    print(f"::warning::{message}")

def translate_with_deepl(text, target_lang, api_key, glossary_id=None):
    """Translate text using DeepL API. target_lang is e.g. 'IT', 'ES', 'FR'.
    With a glossary_id the glossary is applied (DeepL then needs source_lang).
    If DeepL rejects the glossary (HTTP 400) the text is translated without it."""
    params = {
        'text': text,
        'target_lang': target_lang,
        'tag_handling': 'off',
        'preserve_formatting': '1',
    }
    if glossary_id:
        params['source_lang'] = 'EN'
        params['glossary_id'] = glossary_id
    try:
        result = deepl_http('POST', '/v2/translate', api_key,
                            data=urllib.parse.urlencode(params).encode('utf-8'))
    except DeepLError as e:
        if glossary_id and e.status == 400:
            gh_warning(f"DeepL rejected the glossary for {target_lang} — translating without it ({e})")
            params.pop('glossary_id')
            params.pop('source_lang')
            result = deepl_http('POST', '/v2/translate', api_key,
                                data=urllib.parse.urlencode(params).encode('utf-8'))
        else:
            raise
    return result['translations'][0]['text']

# ── GLOSSARY (brand name and agreed terms) ────────────────────────────────
# The terms live in guide-source/deepl-glossary.csv: first column "en", then one
# column per language code (it, es, fr, de, pt, vi, zh, ko, th). A cell is the
# agreed translation; the same word as in English means "keep as is" (e.g. Avatour).
# An empty cell means no rule for that language.
GLOSSARY_FILE   = "guide-source/deepl-glossary.csv"
GLOSSARY_PREFIX = "avatour-guide"
# DeepL offers no glossaries for these languages (DeepL API documentation, Nov 2026).
GLOSSARY_UNSUPPORTED = {"th"}

def read_glossary_file(path=None):
    """Read the glossary CSV. Returns {language: [(english, target), ...]}, or None if
    the file does not exist. Raises ValueError for a file DeepL would reject."""
    path = path or GLOSSARY_FILE
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8-sig', newline='') as f:
        rows = [(n, r) for n, r in enumerate(csv.reader(f), start=1) if any(c.strip() for c in r)]
    if not rows:
        return None
    header = [c.strip().lower() for c in rows[0][1]]
    if not header or header[0] != 'en':
        raise ValueError(f"{path}: the first column of the header row must be 'en'")
    langs = header[1:]
    if len(set(langs)) != len(langs):
        raise ValueError(f"{path}: a language column appears twice in the header row")
    targets = {lang: [] for lang in langs}
    seen = set()
    for n, row in rows[1:]:
        row = row + [''] * (len(header) - len(row))
        en = row[0].strip()
        if not en:
            continue
        if en in seen:
            raise ValueError(f"{path} line {n}: the English term '{en}' appears twice")
        seen.add(en)
        for lang, cell in zip(langs, row[1:]):
            target = cell.strip()
            if not target:
                continue
            for phrase in (en, target):
                if re.search(r'[\x00-\x1f\x7f\u2028\u2029]', phrase):
                    raise ValueError(f"{path} line {n}: '{phrase}' contains a control character")
                if len(phrase.encode('utf-8')) > 1024:
                    raise ValueError(f"{path} line {n}: '{phrase[:30]}...' is longer than 1024 bytes")
            targets[lang].append((en, target))
    return targets

def protected_terms(targets, lang):
    """English terms that must stay unchanged in this language (target == English)."""
    return [en for en, target in (targets or {}).get(lang, []) if en == target]

def glossary_tsv(entries):
    return "\n".join(f"{en}\t{target}" for en, target in entries)

def glossary_name(lang, entries):
    """Name = prefix + language + a short fingerprint of the entries. A changed CSV gives a
    new name, so the glossary is renewed automatically and the old one removed."""
    digest = hashlib.sha256(glossary_tsv(entries).encode('utf-8')).hexdigest()[:10]
    return f"{GLOSSARY_PREFIX}-{lang}-{digest}"

def sync_glossaries(api_key, targets, langs):
    """Make sure every language in `langs` that has entries has a current DeepL glossary.
    Returns {language: glossary_id}. Never raises: any problem is reported as a warning
    and that language is simply translated without a glossary."""
    ids = {}
    try:
        existing = (deepl_http('GET', '/v3/glossaries', api_key) or {}).get('glossaries', [])
    except Exception as e:
        gh_warning(f"Could not read the DeepL glossary list — translating without glossaries ({e})")
        return ids
    by_name = {g.get('name'): g.get('glossary_id') for g in existing}
    for lang in langs:
        entries = (targets or {}).get(lang, [])
        if not entries:
            continue
        if lang in GLOSSARY_UNSUPPORTED:
            print(f"  [GLOSSARY] {lang.upper()}: DeepL has no glossaries for this language — skipped")
            continue
        name = glossary_name(lang, entries)
        gid = by_name.get(name)
        if gid:
            print(f"  [GLOSSARY] {lang.upper()}: using existing glossary {name}")
        else:
            try:
                created = deepl_http('POST', '/v3/glossaries', api_key, json_body={
                    'name': name,
                    'dictionaries': [{
                        'source_lang': 'en',
                        'target_lang': lang,
                        'entries': glossary_tsv(entries),
                        'entries_format': 'tsv',
                    }],
                })
                gid = created['glossary_id']
                for _ in range(10):          # wait until DeepL reports it ready
                    if created.get('ready', True):
                        break
                    time.sleep(1)
                    created = deepl_http('GET', f'/v3/glossaries/{gid}', api_key)
                print(f"  [GLOSSARY] {lang.upper()}: created glossary {name} ({len(entries)} entries)")
            except Exception as e:
                gh_warning(f"Could not create the DeepL glossary for {lang.upper()} — translating without it ({e})")
                continue
        ids[lang] = gid
        prefix = f"{GLOSSARY_PREFIX}-{lang}-"
        for g in existing:                   # remove outdated versions of this language's glossary
            if (g.get('name') or '').startswith(prefix) and g.get('name') != name:
                try:
                    deepl_http('DELETE', f"/v3/glossaries/{g['glossary_id']}", api_key)
                    print(f"  [GLOSSARY] {lang.upper()}: removed outdated glossary {g['name']}")
                except Exception as e:
                    gh_warning(f"Could not remove the outdated glossary {g.get('name')} ({e})")
    return ids

# ── QUALITY CHECK: brand name must survive translation ────────────────────
def qa_check_language(en_text, lang_text, terms):
    """Compare how often each protected term appears, section by section, in the English
    and the translated text. Returns a list of readable problems (empty = fine)."""
    en_secs, lang_secs = split_sections(en_text), split_sections(lang_text)
    issues = []
    if len(en_secs) != len(lang_secs):
        for term in terms:
            n_en, n_tr = en_text.count(term), lang_text.count(term)
            if n_tr < n_en:
                issues.append(f"'{term}' appears {n_en}x in English but only {n_tr}x in the translation (section structure differs)")
        return issues
    for (eh, eb), (lh, lb) in zip(en_secs, lang_secs):
        label = 'intro' if eh == '__preamble__' else re.sub(r'\s*\{#[\w-]+\}\s*$', '', eh.strip())[:60]
        for term in terms:
            n_en, n_tr = (eh + eb).count(term), (lh + lb).count(term)
            if n_tr < n_en:
                issues.append(f"{label}: '{term}' appears {n_en}x in English but only {n_tr}x in the translation")
    return issues

def run_glossary_qa():
    """Check every existing language file. Warnings only — this never fails the build."""
    try:
        targets = read_glossary_file()
        if not targets:
            print("  [QA] No glossary file — brand-name check skipped")
            return
        en_path = "guide-source/Avatour User and Best Practices Guide.md"
        with open(en_path, 'r', encoding='utf-8') as f:
            en_text = f.read()
        for lang in LANGUAGES:
            code = lang["code"]
            if code == "en" or not os.path.exists(lang["source"]):
                continue
            terms = protected_terms(targets, code)
            if not terms:
                continue
            with open(lang["source"], 'r', encoding='utf-8') as f:
                issues = qa_check_language(en_text, f.read(), terms)
            if issues:
                for issue in issues:
                    print(f"  [QA] {code.upper()}: {issue}")
                gh_warning(f"[{code.upper()}] {len(issues)} place(s) where a protected term ({', '.join(terms)}) is missing "
                           f"in the translation, e.g. {issues[0]}")
            else:
                print(f"  [QA] {code.upper()}: protected terms ({', '.join(terms)}) OK")
    except Exception as e:
        gh_warning(f"Brand-name check could not run ({e})")

def auto_translate_lang(en_sections, en_prev_dict, lang_path, lang_name, lang_code, api_key, glossary_id=None):
    """Translate changed EN sections into one language file using DeepL."""
    # Load existing translated file by position (for unchanged sections only)
    existing = []
    if os.path.exists(lang_path):
        with open(lang_path, 'r', encoding='utf-8') as f:
            existing = split_sections(f.read())

    changed = 0
    parts = []

    for i, (en_heading, en_body) in enumerate(en_sections):
        # Always copy preamble as-is
        if en_heading == '__preamble__':
            parts.append(en_body)
            continue

        section_changed = en_prev_dict.get(en_heading, '') != en_body

        if not section_changed and i < len(existing):
            # Reuse existing translation if not oversized
            ex_h, ex_b = existing[i]
            if len(ex_b) <= len(en_body) * 2.0 and ex_h != '__preamble__':
                parts.append(ex_h + ex_b)
                continue

        # Translate heading text only (DeepL gets plain text, no ##)
        m = re.match(r'^(#{1,6}\s+)(.*?)(\s*\{#[\w-]+\})?\s*$', en_heading.strip())
        if m:
            prefix = m.group(1)
            heading_text = m.group(2)
            anchor = m.group(3) or ''
            translated_text = translate_with_deepl(heading_text, lang_code, api_key, glossary_id)
            translated_heading = f"{prefix}{translated_text.strip()}{anchor}\n"
        else:
            translated_heading = en_heading

        # Translate body with DeepL
        translated_body = translate_with_deepl(en_body, lang_code, api_key, glossary_id)

        parts.append(translated_heading + translated_body)
        label = en_heading.strip()[:60]
        print(f"      ✓ {label}")
        changed += 1

    if changed == 0:
        print(f"    [{lang_name}] No changes — skipping")
        return False

    with open(lang_path, 'w', encoding='utf-8') as f:
        f.write(''.join(parts))
    print(f"    [{lang_name}] ✓ Written to {lang_path}")
    return True

def translate_chunk(text, target_language, api_key):
    """Translate a single chunk of markdown body text."""
    payload = json.dumps({
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": 4096,
        "messages": [{"role": "user", "content":
            f"""Translate the following Markdown text to {target_language}.

CRITICAL RULES:
- Return ONLY the translated text, nothing else — no explanation, no preamble, no added content
- Preserve ALL Markdown formatting: bold, italic, links, images, code, blockquotes, lists, anchor IDs like {{#anchor}}, horizontal rules, and ALL subheadings (###, ####, #####)
- Translate ONLY readable text — never translate URLs, image paths, anchor IDs, or code
- Do NOT add any content beyond what is provided below
- Translate EXACTLY the text below and nothing more:

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
    with urllib.request.urlopen(req, timeout=120) as resp:
        result = json.loads(resp.read())['content'][0]['text']
    time.sleep(2)
    # Clean up any stray tags
    result = re.sub(r'</?section>\n?', '', result)
    result = re.sub(r'===(?:START|END)===\n?', '', result)
    return result

def translate_body_strict(body, target_language, api_key):
    """Stricter translation for large sections — warns model about exact length."""
    char_count = len(body)
    payload = json.dumps({
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": 4096,
        "messages": [{"role": "user", "content":
            f"""Translate the following Markdown text to {target_language}.

The input text is exactly {char_count} characters long.
Your translation should be approximately the same length — do NOT add any extra content.
Stop translating when the input text ends. Do not continue beyond it.

RULES:
- Return ONLY the translated text
- Preserve ALL Markdown formatting
- Never translate URLs, image paths, anchor IDs, or code
- Do NOT add any content that is not in the original text below

{body}"""}]
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
    with urllib.request.urlopen(req, timeout=120) as resp:
        result = json.loads(resp.read())['content'][0]['text']
    time.sleep(2)
    result = re.sub(r'</?section>\n?', '', result)
    result = re.sub(r'===(?:START|END)===\n?', '', result)
    return result

def translate_body(body, target_language, api_key):
    """Translate a section body, splitting on ### boundaries for large sections."""
    # Split on ### subsection boundaries to keep chunks manageable
    chunks = re.split(r'(?=^### )', body, flags=re.MULTILINE)
    if len(chunks) == 1:
        # Small section — translate directly
        return translate_chunk(body, target_language, api_key)
    # Translate each chunk separately and reassemble
    translated_chunks = []
    for chunk in chunks:
        if chunk.strip():
            translated_chunks.append(translate_chunk(chunk, target_language, api_key))
        else:
            translated_chunks.append(chunk)
    return ''.join(translated_chunks)

# DeepL target-language code and display name for each language in LANGUAGES.
# Add a line to both when adding a language.
DEEPL_TARGET_CODES = {"it": "IT", "es": "ES", "fr": "FR", "de": "DE", "pt": "PT-BR", "th": "TH", "vi": "VI", "zh": "ZH-HANS", "ko": "KO"}
LANGUAGE_NAMES     = {"it": "Italian", "es": "Spanish", "fr": "French", "de": "German", "pt": "Portuguese (Brazil)", "th": "Thai", "vi": "Vietnamese", "zh": "Chinese (Simplified)", "ko": "Korean"}

def run_auto_translate():
    """Step 1: detect changed EN sections and translate to IT, ES and FR using DeepL."""
    api_key = os.environ.get('DEEPL_API_KEY', '')
    if not api_key:
        print("  [TRANSLATE] No DEEPL_API_KEY — skipping")
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

    # Count changed sections, excluding preamble
    total_changed = sum(
        1 for h, b in en_sections
        if h != '__preamble__' and en_prev_dict.get(h, '') != b
    )
    print(f"  [TRANSLATE] {total_changed} section(s) changed")

    if total_changed > 0:
        glossary_ids = {}
        try:
            glossary_targets = read_glossary_file()
        except ValueError as e:
            glossary_targets = None
            gh_warning(f"Glossary file ignored — {e}")
        if glossary_targets:
            glossary_ids = sync_glossaries(api_key, glossary_targets,
                                           [l["code"] for l in LANGUAGES if l["code"] != "en"])
        else:
            print("  [GLOSSARY] No glossary in use")
        for lang in LANGUAGES:
            if lang["code"] == "en":
                continue
            lang_code = DEEPL_TARGET_CODES.get(lang["code"], lang["code"].upper())
            lang_name = LANGUAGE_NAMES.get(lang["code"], lang["code"])
            print(f"  [TRANSLATE] → {lang_name}")
            auto_translate_lang(en_sections, en_prev_dict,
                lang["source"], lang_name, lang_code, api_key,
                glossary_ids.get(lang["code"]))

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
        "title":   "Avatour User and Best Practices Guide",
    },
    {
        "code":    "it",
        "suffix":  "-it",
        "source":  "guide-source/Avatour User and Best Practices Guide - IT.md",
        "webflow": "https://avatour.com/user-guide-it",
        "title":   "Guida Utente e Best Practice di Avatour",
    },
    {
        "code":    "es",
        "suffix":  "-es",
        "source":  "guide-source/Avatour User and Best Practices Guide - ES.md",
        "webflow": "https://avatour.com/user-guide-es",
        "title":   "Guía del Usuario y Mejores Prácticas de Avatour",
    },
    {
        "code":    "fr",
        "suffix":  "-fr",
        "source":  "guide-source/Avatour User and Best Practices Guide - FR.md",
        "webflow": "https://avatour.com/user-guide-fr",
        "title":   "Guide de l'Utilisateur et Meilleures Pratiques Avatour",
    },
    {
        "code":    "de",
        "suffix":  "-de",
        "source":  "guide-source/Avatour User and Best Practices Guide - DE.md",
        "webflow": "https://avatour.com/user-guide-de",
        "title":   "Avatour Benutzer- und Best-Practice-Leitfaden",
    },
    {
        "code":    "pt",
        "suffix":  "-pt",
        "source":  "guide-source/Avatour User and Best Practices Guide - PT.md",
        "webflow": "https://avatour.com/user-guide-pt",
        "title":   "Guia do Usuário e Melhores Práticas do Avatour",
    },
    {
        "code":    "th",
        "suffix":  "-th",
        "source":  "guide-source/Avatour User and Best Practices Guide - TH.md",
        "webflow": "https://avatour.com/user-guide-th",
        "title":   "คู่มือผู้ใช้และแนวปฏิบัติที่ดีของ Avatour",
    },
    {
        "code":    "vi",
        "suffix":  "-vi",
        "source":  "guide-source/Avatour User and Best Practices Guide - VI.md",
        "webflow": "https://avatour.com/user-guide-vi",
        "title":   "Hướng dẫn Người dùng và Thực hành Tốt nhất của Avatour",
    },
    {
        "code":    "zh",
        "suffix":  "-zh",
        "source":  "guide-source/Avatour User and Best Practices Guide - ZH.md",
        "webflow": "https://avatour.com/user-guide-zh",
        "title":   "Avatour 用户指南与最佳实践",
    },
    {
        "code":    "ko",
        "suffix":  "-ko",
        "source":  "guide-source/Avatour User and Best Practices Guide - KO.md",
        "webflow": "https://avatour.com/user-guide-ko",
        "title":   "Avatour 사용자 가이드 및 모범 사례",
    },
]



# ── CSS ───────────────────────────────────────────────────────────────────
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Titillium+Web:wght@300;400;600;700&family=Roboto:wght@300;400;500&family=Sarabun:wght@300;400;500;600;700&family=Noto+Sans+SC:wght@300;400;500;600;700&family=Noto+Sans+KR:wght@300;400;500;600;700&display=swap');

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
  font-family: 'Roboto', 'Sarabun', 'Noto Sans SC', 'Noto Sans KR', sans-serif;
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
.lang-switcher { display:flex; gap:4px; align-items:center; }
.lang-btn {
  font-family:'Titillium Web',sans-serif; font-size:11px; font-weight:700;
  letter-spacing:.06em; padding:4px 8px; border-radius:4px;
  border:1px solid rgba(255,255,255,.25); background:transparent;
  color:rgba(255,255,255,.6); cursor:pointer; text-decoration:none; transition:all .15s;
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
  font-family: 'Titillium Web', 'Sarabun', 'Noto Sans SC', 'Noto Sans KR', sans-serif;
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
  font-family: 'Titillium Web', 'Sarabun', 'Noto Sans SC', 'Noto Sans KR', sans-serif;
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
  font-family: 'Titillium Web', 'Sarabun', 'Noto Sans SC', 'Noto Sans KR', sans-serif;
  font-size: 20px; font-weight: 700; color: var(--blue);
  margin: 40px 0 12px; padding-top: 8px;
  border-top: 2px solid var(--border);
  scroll-margin-top: calc(var(--header-h) + 16px);
}
.guide-article h3 {
  font-family: 'Titillium Web', 'Sarabun', 'Noto Sans SC', 'Noto Sans KR', sans-serif;
  font-size: 16px; font-weight: 700; color: var(--blue);
  margin: 28px 0 10px;
  scroll-margin-top: calc(var(--header-h) + 16px);
}
.guide-article h4 {
  font-family: 'Titillium Web', 'Sarabun', 'Noto Sans SC', 'Noto Sans KR', sans-serif;
  font-size: 15px; font-weight: 700; color: var(--slate);
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
  font-family: 'Titillium Web', 'Sarabun', 'Noto Sans SC', 'Noto Sans KR', sans-serif;
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
  border-radius: 0 6px 6px 0; font-size: 13.5px;
}
.guide-article blockquote p { margin-bottom: 0; color: #2a3a44; }
.guide-article blockquote strong { color: var(--orange); }

/* SCREENSHOTS */
.guide-article img {
  width: 100%; max-height: 450px; height: auto;
  object-fit: contain; display: block;
  border: 1px solid var(--border);
  border-radius: 6px; margin: 20px auto 4px;
}
.guide-article img + em {
  display: block; font-size: 12px;
  color: var(--muted); text-align: left;
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
  font-family: 'Titillium Web', 'Sarabun', 'Noto Sans SC', 'Noto Sans KR', sans-serif;
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
  .guide-article img { max-width: 80%; margin: 12px auto; }
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
body.print-mode .guide-main { margin-left: 0; padding-right: 0; }
body.print-mode .guide-article {
  max-width: 100%; padding: 0; margin: 0;
  font-size: 10.5pt; line-height: 1.5;
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
    font-family: 'Titillium Web', 'Sarabun', 'Noto Sans SC', 'Noto Sans KR', sans-serif;
    font-size: 9pt; color: #7A8A95;
  }
  @bottom-left {
    content: "avatour.com";
    font-family: 'Titillium Web', 'Sarabun', 'Noto Sans SC', 'Noto Sans KR', sans-serif;
    font-size: 9pt; color: #7A8A95;
  }
  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
    font-family: 'Titillium Web', 'Sarabun', 'Noto Sans SC', 'Noto Sans KR', sans-serif;
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
  max-width: 90%; display: block;
  margin: 12px auto; page-break-inside: avoid;
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

# Preview image for link unfurling (Apple Mail, Slack, iMessage, social shares).
# Without this, unfurl bots fall back to scanning the page and grabbing the
# largest embedded image — which is what was driving repeated Cloudinary
# bandwidth spikes on the guide's screenshots. Reusing an image already
# confirmed working as an og:image elsewhere on avatour.com.
OG_IMAGE = "https://cdn.prod.website-files.com/6578f6bdfadb289687b7a7ad/65c18a48553050a59b5658f9_Avatour%20Operator%20with%20Participants%20191.jpg"


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
    html += '<a href="mailto:support@avatour.live">Open Support Ticket ↗</a>\n'
    return html


# ── CLOUDINARY IMAGE OPTIMIZATION ─────────────────────────────────────────
CLOUDINARY_UPLOAD_RE = re.compile(
    r'(https://res\.cloudinary\.com/avatour/image/upload/)'
    r'((?:[a-z]{1,3}_[a-z0-9]+(?:,[a-z]{1,3}_[a-z0-9]+)*/)?)'
    r'(v\d+/)?'
    r'([^\s"\')]+)'
)

def optimize_cloudinary_urls(html):
    """Ensure every Cloudinary delivery URL uses f_auto,q_auto for format/quality optimization."""
    def repl(m):
        base, transform, version, rest = m.groups()
        if transform and 'f_auto' in transform:
            new_transform = transform
        elif transform:
            new_transform = transform[:-1] + ',f_auto,q_auto/'
        else:
            new_transform = 'f_auto,q_auto/'
        return f'{base}{new_transform}{version or ""}{rest}'
    return CLOUDINARY_UPLOAD_RE.sub(repl, html)


# ── MARKDOWN → HTML ───────────────────────────────────────────────────────
def md_to_html(md_text):
    """Convert Markdown to HTML."""
    md = markdown.Markdown(extensions=[
        TocExtension(slugify=lambda value, separator: re.sub(r'[^\w-]', '', value.lower().replace(' ', separator))),
        'tables', 'fenced_code', 'attr_list', 'md_in_html',
    ])
    return optimize_cloudinary_urls(md.convert(md_text))


# ── OPEN LINKS IN NEW TAB ─────────────────────────────────────────────────
def open_links_in_new_tab(html):
    """Add target=_blank to all external links."""
    def add_target(m):
        tag = m.group(0)
        href_m = re.search(r'href=["\'](["\']*)["\']', tag)
        if not href_m:
            href_m = re.search(r"href=[\"']([^\"']*)[\"']", tag)
        if href_m:
            url = href_m.group(1)
            if (url.startswith('http') or url.startswith('mailto')) and 'target=' not in tag:
                tag = tag[:-1] + ' target="_blank" rel="noopener">'
        return tag
    return re.sub(r'<a [^>]+>', add_target, html)


# ── LANG SWITCHER ─────────────────────────────────────────────────────────
def build_lang_switcher_html(active_lang, embed=False):
    """Build EN / IT / ES switcher buttons."""
    buttons = []
    for lang in LANGUAGES:
        code   = lang["code"]
        suffix = lang["suffix"]
        active = ' active' if code == active_lang else ''
        if embed:
            webflow_url = lang.get("webflow", "#")
            buttons.append(
                f'<a class="lang-btn{active}" href="{webflow_url}" '
                f"onclick=\"window.top.location.href='{webflow_url}'; return false;\">"
                f'{code.upper()}</a>'
            )
        else:
            href = f"avatour-guide{suffix}.html"
            buttons.append(f'<a class="lang-btn{active}" href="{href}">{code.upper()}</a>')
    return f'<div class="lang-switcher">{"".join(buttons)}</div>'


# ── HTML BUILDERS ─────────────────────────────────────────────────────────
def build_full_html(article_html, toc_html, sidenav_html, meta, body_class=""):
    lang_code     = meta.get('lang', 'en')
    lang_switcher = build_lang_switcher_html(lang_code, embed=False)
    return f"""<!DOCTYPE html>
<html lang="{lang_code}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{meta['title']} — Avatour</title>
<meta property="og:type" content="website">
<meta property="og:title" content="{meta['title']} — Avatour">
<meta property="og:description" content="Avatour User Guide and Best Practices">
<meta property="og:image" content="{OG_IMAGE}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{meta['title']} — Avatour">
<meta name="twitter:image" content="{OG_IMAGE}">
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
    """Webflow-compatible embed — no header, fixed-height iframe, manual scroll."""
    lang_code     = meta.get('lang', 'en')
    lang_switcher = build_lang_switcher_html(lang_code, embed=True)

    # Replace scroll-margin-top for embed (header hidden, so calc value wrong)
    embed_css = CSS.replace(
        'scroll-margin-top: calc(var(--header-h) + 16px);',
        'scroll-margin-top: 120px;'
    )

    EMBED_EXTRA_CSS = """
/* WEBFLOW EMBED OVERRIDES */
.guide-header { display: none; }
.guide-layout { padding-top: 0; }
.guide-sidenav {
  position: fixed; top: 0; bottom: 0;
  width: var(--sidebar-w); overflow-y: auto;
  padding-bottom: 120px;
}
.guide-main {
  margin-left: var(--sidebar-w) !important;
  padding-right: 0 !important;
  display: block;
}
.guide-article {
  max-width: 780px;
  padding-top: 24px;
}
.guide-toc { display: none; }
"""

    EMBED_JS = """
// ── ANCHOR LINKS ───────────────────────────────────────────────────────
// Use manual scrollTop calculation — scrollIntoView ignores scroll-margin-top
// inside fixed-height iframes in some browsers.
var SCROLL_PADDING = 20; // px of breathing room above heading
document.querySelectorAll('.guide-sidenav a[href^="#"]').forEach(function(link) {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    var id = this.getAttribute('href').slice(1);
    var target = document.getElementById(id);
    if (!target) return;
    var targetTop = target.getBoundingClientRect().top + window.pageYOffset - SCROLL_PADDING;
    window.scrollTo({ top: targetTop, behavior: 'smooth' });
  });
});

// ── ACTIVE SIDENAV HIGHLIGHTING ────────────────────────────────────────
var headings = document.querySelectorAll('.guide-article h2, .guide-article h3');
var sideLinks = document.querySelectorAll('.guide-sidenav a');
if (headings.length) {
  var obs = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
      if (e.isIntersecting) {
        var id = e.target.id;
        sideLinks.forEach(function(l) {
          l.classList.toggle('active', l.getAttribute('href') === '#' + id);
        });
      }
    });
  }, { rootMargin: '-10% 0px -80% 0px' });
  headings.forEach(function(h) { if (h.id) obs.observe(h); });
}
"""

    return f"""<!DOCTYPE html>
<html lang="{lang_code}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{meta['title']} — Avatour</title>
<meta property="og:type" content="website">
<meta property="og:title" content="{meta['title']} — Avatour">
<meta property="og:description" content="Avatour User Guide and Best Practices">
<meta property="og:image" content="{OG_IMAGE}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{meta['title']} — Avatour">
<meta name="twitter:image" content="{OG_IMAGE}">
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
        'title':   post.get('title', lang.get('title', 'Avatour User and Best Practices Guide')),
        'version': post.get('version', '2.0'),
        'updated': post.get('updated', '2026'),
        'lang':    code,
    }

    print(f"  [{code.upper()}] Building from {source}")

    lang_title = lang.get('title', 'Avatour User and Best Practices Guide')
    md_text = re.sub(r'^# .+', f'# {lang_title}', md_text, count=1)
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

    print("\n── Step 1b: Brand-name check ───────────────────────────")
    run_glossary_qa()

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
