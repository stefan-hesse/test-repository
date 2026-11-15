#!/usr/bin/env python3
"""
Live check of the DeepL glossary setup against the REAL DeepL API.

Run it from GitHub: Actions -> "Test DeepL glossary" -> Run workflow.
It does NOT change any file in the repository and does NOT touch the guide.

What it does
  1. Reads guide-source/deepl-glossary.csv and checks that it is valid.
  2. Creates the DeepL glossaries exactly as the build does (first time) and runs the same
     step again (must reuse them, not create new ones).
  3. Translates two short test texts into every language, with and without the glossary,
     and checks that the brand name 'Avatour' is kept wherever a glossary is in use.
  4. Runs the brand-name check on the existing language files.
Cost: a few thousand characters in total (a few cents at most).
Exit code 0 = everything as expected, 1 = something needs attention.
"""
import contextlib, io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True
import build

TEXTS = ["Avatour User Types", "Avatour hosts the meeting. Join an Avatour meeting from any browser."]
BRAND = "Avatour"


def capture(fn, *args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        result = fn(*args)
    return result, buf.getvalue()


def translate_all(code, api_key, glossary_id=None):
    return " || ".join(build.translate_with_deepl(t, code, api_key, glossary_id) for t in TEXTS)


def main():
    api_key = os.environ.get("DEEPL_API_KEY", "")
    if not api_key:
        print("DEEPL_API_KEY is not set - cannot run the live check.")
        return 1
    problems, rows = [], []
    expected_brand = sum(t.count(BRAND) for t in TEXTS)

    print("\n== 1. Glossary file ==")
    try:
        targets = build.read_glossary_file()
    except ValueError as e:
        print(f"  FAIL  {e}")
        return 1
    if not targets:
        print(f"  FAIL  {build.GLOSSARY_FILE} not found or empty")
        return 1
    for lang, entries in targets.items():
        print(f"  {lang.upper():3} {len(entries)} entr{'y' if len(entries) == 1 else 'ies'}: "
              + ", ".join(f"{en} -> {t}" for en, t in entries))

    langs = [l["code"] for l in build.LANGUAGES if l["code"] != "en"]
    wanted = [c for c in langs if targets.get(c) and c not in build.GLOSSARY_UNSUPPORTED]

    print("\n== 2. Create glossaries (same code as the build) ==")
    ids, log = capture(build.sync_glossaries, api_key, targets, langs)
    print(log.rstrip())
    for c in wanted:
        if c not in ids:
            problems.append(f"{c.upper()}: DeepL did not accept the glossary (see warning above)")
    print("  Second run, must reuse the glossaries:")
    ids2, log2 = capture(build.sync_glossaries, api_key, targets, langs)
    print("   ", log2.strip().replace("\n", "\n    "))
    if ids2 != ids or "created glossary" in log2:
        problems.append("Second run did not reuse the existing glossaries")

    print("\n== 3. Test translations ==")
    for c in langs:
        code = build.DEEPL_TARGET_CODES.get(c, c.upper())
        try:
            plain = translate_all(code, api_key)
        except Exception as e:
            problems.append(f"{c.upper()}: plain translation failed ({e})")
            rows.append((c, "error", "-", "FAIL"))
            continue
        kept_plain = plain.count(BRAND)
        if c in ids:
            try:
                with_g = translate_all(code, api_key, ids[c])
            except Exception as e:
                problems.append(f"{c.upper()}: translation with glossary failed ({e})")
                rows.append((c, f"{kept_plain}/{expected_brand}", "error", "FAIL"))
                continue
            kept_g = with_g.count(BRAND)
            ok = kept_g == expected_brand
            if not ok:
                problems.append(f"{c.upper()}: with glossary {BRAND} appears {kept_g}x instead of {expected_brand}x: {with_g}")
            rows.append((c, f"{kept_plain}/{expected_brand}", f"{kept_g}/{expected_brand}", "OK" if ok else "FAIL"))
            print(f"  {c.upper():3} without glossary: {plain}\n      with glossary:    {with_g}")
        else:
            reason = "no glossary possible" if c in build.GLOSSARY_UNSUPPORTED else "no glossary"
            rows.append((c, f"{kept_plain}/{expected_brand}", reason, "info"))
            print(f"  {c.upper():3} ({reason}): {plain}")

    print("\n== 4. Brand-name check of the existing language files ==")
    _, qa = capture(build.run_glossary_qa)
    print(qa.rstrip())
    qa_warnings = [l for l in qa.splitlines() if l.startswith("::warning::")]

    print("\n== Result ==")
    print(f"  {'lang':5}{'Avatour kept (no glossary)':28}{'Avatour kept (glossary)':26}status")
    for c, a, b, st in rows:
        print(f"  {c.upper():5}{a:28}{b:26}{st}")
    if qa_warnings:
        print(f"\n  NOTE: the brand-name check reports problems in {len(qa_warnings)} existing language file(s).")
        print("        This is information about current translations, not a failure of the glossary.")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write("### DeepL glossary live check\n\n| language | Avatour kept without glossary | with glossary | status |\n|---|---|---|---|\n")
            for c, a, b, st in rows:
                f.write(f"| {c.upper()} | {a} | {b} | {st} |\n")
            f.write(f"\nBrand-name check of existing files: {'**' + str(len(qa_warnings)) + ' file(s) with problems**' if qa_warnings else 'no problems'}\n")
    if problems:
        print("\n  RESULT: FAIL")
        for p in problems:
            print(f"   - {p}")
        return 1
    print("\n  RESULT: PASS - glossaries are accepted by DeepL and the brand name is kept.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
