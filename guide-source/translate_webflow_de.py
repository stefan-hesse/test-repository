#!/usr/bin/env python3
"""
Avatour Webflow German Translation Script
==========================================
Fetches page content from Webflow, translates text nodes via DeepL,
and pushes German translations back to Webflow's DE locale.

Safe to re-run: nodes that have already been manually edited in German
are detected and skipped — only nodes still showing English fallback
text are translated.

Usage:
    python translate_webflow_de.py [--page PAGE_ID] [--dry-run] [--force]

    --dry-run   Translate but do not push to Webflow
    --force     Overwrite all nodes, even manually edited German ones

Requirements:
    WEBFLOW_API_TOKEN  - Webflow API token (Pages: read/write, Sites: read)
    DEEPL_API_KEY      - DeepL API key (free or pro)

Page IDs (avatour.com):
    Homepage:   6578f6bdfadb289687b7a7d6
    (add more as pilot expands)
"""

import os
import argparse
import requests

# ── Config ────────────────────────────────────────────────────────────────────

WEBFLOW_API_TOKEN = os.environ["WEBFLOW_API_TOKEN"]
DEEPL_API_KEY     = os.environ["DEEPL_API_KEY"]

SITE_ID     = "6578f6bdfadb289687b7a7ad"
LOCALE_ID   = "69d235ac4ced97b0b3403524"   # German (de)
TARGET_LANG = "DE"
SOURCE_LANG = "EN"

WEBFLOW_BASE = "https://api.webflow.com/v2"
# Free DeepL keys end in :fx and require a different endpoint
DEEPL_URL = (
    "https://api-free.deepl.com/v2/translate"
    if DEEPL_API_KEY.endswith(":fx")
    else "https://api.deepl.com/v2/translate"
)

WEBFLOW_HEADERS = {
    "Authorization": f"Bearer {WEBFLOW_API_TOKEN}",
    "Content-Type":  "application/json",
}

# Pages to translate: name → page ID
PAGES = {
    "Homepage": "6578f6bdfadb289687b7a7d6",
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def fetch_page_nodes(page_id: str, locale_id: str = None) -> list:
    """Fetch all nodes for a page, optionally in a specific locale."""
    url    = f"{WEBFLOW_BASE}/pages/{page_id}/dom"
    params = {"limit": 100}
    if locale_id:
        params["localeId"] = locale_id
    resp = requests.get(url, headers=WEBFLOW_HEADERS, params=params)
    resp.raise_for_status()
    return resp.json().get("nodes", [])


def build_text_map(nodes: list) -> dict:
    """Build a nodeId → plain text map for easy comparison."""
    return {
        n["id"]: n["text"]["text"]
        for n in nodes
        if n["type"] == "text"
    }


def translate_html(html: str) -> str:
    """Translate an HTML string from English to German via DeepL."""
    resp = requests.post(
        DEEPL_URL,
        headers={"Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}"},
        json={
            "text": [html],
            "source_lang": SOURCE_LANG,
            "target_lang": TARGET_LANG,
            "tag_handling": "html",
            "preserve_formatting": True,
        },
    )
    resp.raise_for_status()
    return resp.json()["translations"][0]["text"]


def push_translations(page_id: str, translated_nodes: list, dry_run: bool = False):
    """Push translated nodes to Webflow DE locale."""
    if dry_run:
        print(f"  [DRY RUN] Would push {len(translated_nodes)} nodes to Webflow")
        return

    url     = f"{WEBFLOW_BASE}/pages/{page_id}/dom"
    params  = {"localeId": LOCALE_ID}
    payload = {"nodes": translated_nodes}

    resp = requests.post(url, headers=WEBFLOW_HEADERS, params=params, json=payload)
    if resp.status_code in (200, 201, 204):
        print(f"  ✓ Pushed {len(translated_nodes)} translated nodes to Webflow DE locale")
    else:
        print(f"  ✗ Webflow API error: {resp.status_code}")
        print(f"    {resp.text[:500]}")
        resp.raise_for_status()


# ── Main ──────────────────────────────────────────────────────────────────────

def translate_page(page_name: str, page_id: str, dry_run: bool = False, force: bool = False):
    print(f"\n📄 {page_name} ({page_id})")

    # 1. Fetch EN nodes (primary locale = no localeId param)
    en_nodes = fetch_page_nodes(page_id)
    en_text  = build_text_map(en_nodes)
    en_html  = {n["id"]: n["text"]["html"] for n in en_nodes if n["type"] == "text"}
    print(f"  EN: {len(en_text)} text nodes")

    # 2. Fetch current DE nodes
    de_nodes = fetch_page_nodes(page_id, locale_id=LOCALE_ID)
    de_text  = build_text_map(de_nodes)
    print(f"  DE: {len(de_text)} text nodes fetched")

    # 3. Decide which nodes need translation
    to_translate = []
    skipped = 0

    for node_id, en_plain in en_text.items():
        de_plain = de_text.get(node_id, "")

        if not force and de_plain and de_plain != en_plain:
            # DE text exists and differs from EN → manually edited, skip
            skipped += 1
            continue

        to_translate.append({
            "id":   node_id,
            "html": en_html[node_id],
        })

    print(f"  To translate: {len(to_translate)}, Already localised (skipped): {skipped}")

    if not to_translate:
        print("  Nothing to translate — all nodes already localised.")
        return

    # 4. Translate via DeepL
    translated = []
    errors = []

    for i, node in enumerate(to_translate):
        try:
            german_html = translate_html(node["html"])
            translated.append({"nodeId": node["id"], "text": german_html})
            print(f"  ✓ {i+1}/{len(to_translate)}: {node['html'][:60].strip()[:60]}…")
        except Exception as e:
            errors.append({"nodeId": node["id"], "error": str(e)})
            print(f"  ✗ {i+1}/{len(to_translate)}: ERROR — {e}")

    print(f"\n  Translated: {len(translated)}, Errors: {len(errors)}")

    if not translated:
        print("  Nothing to push.")
        return

    # 5. Push to Webflow
    push_translations(page_id, translated, dry_run=dry_run)


def main():
    parser = argparse.ArgumentParser(description="Translate Webflow pages to German via DeepL")
    parser.add_argument("--page",    help="Translate a single page by ID (overrides default list)")
    parser.add_argument("--dry-run", action="store_true", help="Translate but don't push to Webflow")
    parser.add_argument("--force",   action="store_true", help="Overwrite all nodes including manually edited German")
    args = parser.parse_args()

    print("🌐 Avatour Webflow → German Translation")
    print(f"   Site:   {SITE_ID}")
    print(f"   Locale: {LOCALE_ID} (de)")
    print(f"   Mode:   {'DRY RUN' if args.dry_run else 'LIVE'}")
    print(f"   Force:  {args.force}")

    pages_to_run = {args.page: args.page} if args.page else PAGES

    for name, pid in pages_to_run.items():
        translate_page(name, pid, dry_run=args.dry_run, force=args.force)

    print("\n✅ Done.")


if __name__ == "__main__":
    main()
