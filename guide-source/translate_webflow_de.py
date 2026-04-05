#!/usr/bin/env python3
"""
Avatour Webflow German Translation Script
==========================================
Fetches page content from Webflow, translates text nodes via DeepL,
and pushes German translations back to Webflow's DE locale.

Usage:
    python translate_webflow_de.py [--page PAGE_ID] [--dry-run]

Requirements:
    WEBFLOW_API_TOKEN  - Webflow API token (Pages: read/write, Sites: read)
    DEEPL_API_KEY      - DeepL API key (free or pro)

Page IDs (avatour.com):
    Homepage:   6578f6bdfadb289687b7a7d6
    (add more as pilot expands)
"""

import os
import sys
import json
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
DEEPL_URL    = (
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

def fetch_page_nodes(page_id: str) -> list:
    """Fetch all text nodes for a page."""
    url = f"{WEBFLOW_BASE}/pages/{page_id}/dom"
    params = {"limit": 100}
    resp = requests.get(url, headers=WEBFLOW_HEADERS, params=params)
    resp.raise_for_status()
    data = resp.json()
    nodes = data.get("nodes", [])
    print(f"  Fetched {len(nodes)} nodes ({sum(1 for n in nodes if n['type'] == 'text')} text nodes)")
    return nodes


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

    url = f"{WEBFLOW_BASE}/pages/{page_id}/dom"
    payload = {
        "localeId": LOCALE_ID,
        "nodes": translated_nodes,
    }
    resp = requests.post(url, headers=WEBFLOW_HEADERS, json=payload)
    if resp.status_code in (200, 201, 204):
        print(f"  ✓ Pushed {len(translated_nodes)} translated nodes to Webflow DE locale")
    else:
        print(f"  ✗ Webflow API error: {resp.status_code}")
        print(f"    {resp.text[:500]}")
        resp.raise_for_status()


# ── Main ──────────────────────────────────────────────────────────────────────

def translate_page(page_name: str, page_id: str, dry_run: bool = False):
    print(f"\n📄 {page_name} ({page_id})")

    # 1. Fetch nodes
    nodes = fetch_page_nodes(page_id)
    text_nodes = [n for n in nodes if n["type"] == "text"]

    if not text_nodes:
        print("  No text nodes found — skipping.")
        return

    # 2. Translate each text node via DeepL
    translated = []
    errors = []

    for i, node in enumerate(text_nodes):
        original_html = node["text"]["html"]
        try:
            german_html = translate_html(original_html)
            translated.append({
                "nodeId": node["id"],
                "text": german_html,
            })
            print(f"  ✓ {i+1}/{len(text_nodes)}: {original_html[:60].strip()[:60]}…")
        except Exception as e:
            errors.append({"nodeId": node["id"], "error": str(e)})
            print(f"  ✗ {i+1}/{len(text_nodes)}: ERROR — {e}")

    print(f"\n  Translated: {len(translated)}, Errors: {len(errors)}")

    if not translated:
        print("  Nothing to push.")
        return

    # 3. Push to Webflow
    push_translations(page_id, translated, dry_run=dry_run)


def main():
    parser = argparse.ArgumentParser(description="Translate Webflow pages to German via DeepL")
    parser.add_argument("--page", help="Translate a single page by ID (overrides default list)")
    parser.add_argument("--dry-run", action="store_true", help="Translate but don't push to Webflow")
    args = parser.parse_args()

    print("🌐 Avatour Webflow → German Translation")
    print(f"   Site:   {SITE_ID}")
    print(f"   Locale: {LOCALE_ID} (de)")
    print(f"   Mode:   {'DRY RUN' if args.dry_run else 'LIVE'}")

    pages_to_run = {}
    if args.page:
        pages_to_run = {args.page: args.page}
    else:
        pages_to_run = PAGES

    for name, pid in pages_to_run.items():
        translate_page(name, pid, dry_run=args.dry_run)

    print("\n✅ Done.")


if __name__ == "__main__":
    main()
