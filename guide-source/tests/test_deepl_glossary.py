"""Automated tests for the DeepL glossary support and the brand-name check in build.py.

Run:  python -m unittest discover -s guide-source/tests -v
No network and no API key needed: a fake DeepL server (mock_deepl.py) is used.
"""
import contextlib, io, os, shutil, sys, tempfile, unittest
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True

import build
from mock_deepl import MockDeepL

EN_GUIDE = """# Avatour User and Best Practices Guide

## 1. For All Avatour Users {#for-all-avatour-users}

Welcome to Avatour. Avatour helps teams collaborate.

## 2. Avatour User Types {#avatour-user-types}

### 2.1 Meeting Attendees

Attendees can join an Avatour meeting without an account.

## 3. Other {#other}

Nothing about the brand here.
"""


def lang(code, tmp):
    return {"code": code, "suffix": f"-{code}" if code != "en" else "",
            "source": os.path.join("guide-source", f"Guide - {code.upper()}.md") if code != "en"
                      else os.path.join("guide-source", "Avatour User and Best Practices Guide.md"),
            "webflow": f"https://example.invalid/{code}", "title": "Guide"}


def capture(fn, *args, **kwargs):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        result = fn(*args, **kwargs)
    return result, buf.getvalue()


class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = MockDeepL().start()

    @classmethod
    def tearDownClass(cls):
        cls.server.stop()

    def setUp(self):
        self.server.glossaries.clear()
        self.server.requests.clear()
        self.server.failures.clear()
        self.server.reject_glossary_langs.clear()
        self.server.not_ready_polls = 0
        self.server.translate_calls = 0
        patches = [mock.patch.object(build, 'DEEPL_API_URL', self.server.url),
                   mock.patch('time.sleep', lambda s: None)]
        for p in patches:
            p.start()
            self.addCleanup(p.stop)


class TestGlossaryFile(unittest.TestCase):
    def write(self, text, encoding='utf-8'):
        d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, d)
        path = os.path.join(d, "g.csv")
        with open(path, 'w', encoding=encoding, newline='') as f:
            f.write(text)
        return path

    def test_valid_file(self):
        t = build.read_glossary_file(self.write("en,it,ko\nAvatour,Avatour,Avatour\nHost,ospite,\n"))
        self.assertEqual(t['it'], [("Avatour", "Avatour"), ("Host", "ospite")])
        self.assertEqual(t['ko'], [("Avatour", "Avatour")])        # empty cell = no rule

    def test_bom_spaces_and_blank_lines(self):
        t = build.read_glossary_file(self.write("\ufeffen, ko\n\n Avatour , Avatour \n,\n"))
        self.assertEqual(t['ko'], [("Avatour", "Avatour")])

    def test_missing_file_means_no_glossary(self):
        self.assertIsNone(build.read_glossary_file("/nonexistent/glossary.csv"))

    def test_bad_header_is_rejected(self):
        with self.assertRaises(ValueError):
            build.read_glossary_file(self.write("term,ko\nAvatour,Avatour\n"))

    def test_duplicate_english_term_is_rejected(self):
        with self.assertRaises(ValueError):
            build.read_glossary_file(self.write("en,ko\nAvatour,Avatour\nAvatour,Avatour\n"))

    def test_duplicate_language_column_is_rejected(self):
        with self.assertRaises(ValueError):
            build.read_glossary_file(self.write("en,ko,ko\nAvatour,Avatour,Avatour\n"))

    def test_control_character_is_rejected(self):
        with self.assertRaises(ValueError):
            build.read_glossary_file(self.write('en,ko\nAva\ttour,"Ava\ttour"\n'))

    def test_protected_terms_only_unchanged_ones(self):
        t = {"ko": [("Avatour", "Avatour"), ("Host", "호스트")]}
        self.assertEqual(build.protected_terms(t, "ko"), ["Avatour"])
        self.assertEqual(build.protected_terms(t, "th"), [])

    def test_glossary_name_changes_with_content(self):
        a = build.glossary_name("ko", [("Avatour", "Avatour")])
        b = build.glossary_name("ko", [("Avatour", "Avatour")])
        c = build.glossary_name("ko", [("Avatour", "Avatour"), ("Host", "호스트")])
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertTrue(a.startswith("avatour-guide-ko-"))


class TestHttpAndTranslate(BaseCase):
    def test_retries_server_errors_then_succeeds(self):
        self.server.fail("POST", "/v2/translate", 500, times=2)
        out, _ = capture(build.translate_with_deepl, "Hello", "KO", "key")
        self.assertEqual(out, "Hello")
        self.assertEqual(len(self.server.calls("POST", "/v2/translate")), 3)

    def test_retries_rate_limit(self):
        self.server.fail("POST", "/v2/translate", 429, times=1)
        out, _ = capture(build.translate_with_deepl, "Hello", "IT", "key")
        self.assertEqual(out, "Hello")
        self.assertEqual(len(self.server.calls("POST", "/v2/translate")), 2)

    def test_gives_up_after_retries(self):
        self.server.fail("POST", "/v2/translate", 503, times=99)
        with self.assertRaises(build.DeepLError):
            capture(build.translate_with_deepl, "Hello", "IT", "key")
        self.assertEqual(len(self.server.calls("POST", "/v2/translate")), 4)   # 1 try + 3 retries

    def test_quota_exceeded_is_not_retried(self):
        self.server.fail("POST", "/v2/translate", 456, times=99)
        with self.assertRaises(build.DeepLError) as ctx:
            capture(build.translate_with_deepl, "Hello", "IT", "key")
        self.assertEqual(ctx.exception.status, 456)
        self.assertEqual(len(self.server.calls("POST", "/v2/translate")), 1)

    def test_auth_header_is_sent(self):
        capture(build.translate_with_deepl, "Hello", "IT", "secret-key")
        self.assertEqual(self.server.requests[-1]["auth"], "DeepL-Auth-Key secret-key")

    def test_without_glossary_request_is_unchanged(self):
        capture(build.translate_with_deepl, "Hello", "IT", "key")
        p = self.server.requests[-1]["params"]
        self.assertNotIn("glossary_id", p)
        self.assertNotIn("source_lang", p)
        self.assertEqual(p["tag_handling"], "off")
        self.assertEqual(p["preserve_formatting"], "1")

    def test_with_glossary_sends_id_and_source_language(self):
        ids, _ = capture(build.sync_glossaries, "key", {"ko": [("Avatour", "Avatour")]}, ["ko"])
        out, _ = capture(build.translate_with_deepl, "Avatour User Types", "KO", "key", ids["ko"])
        self.assertEqual(out, "Avatour User Types")              # brand name kept
        p = self.server.requests[-1]["params"]
        self.assertEqual(p["glossary_id"], ids["ko"])
        self.assertEqual(p["source_lang"], "EN")

    def test_without_glossary_the_mock_reproduces_the_bug(self):
        out, _ = capture(build.translate_with_deepl, "Avatour User Types", "KO", "key")
        self.assertIn("아바투어", out)

    def test_rejected_glossary_falls_back_to_plain_translation(self):
        ids, _ = capture(build.sync_glossaries, "key", {"ko": [("Avatour", "Avatour")]}, ["ko"])
        self.server.fail("POST", "/v2/translate", 400, times=1)
        out, log = capture(build.translate_with_deepl, "Hello", "KO", "key", ids["ko"])
        self.assertEqual(out, "Hello")
        self.assertIn("::warning::", log)
        last = self.server.calls("POST", "/v2/translate")[-1]["params"]
        self.assertNotIn("glossary_id", last)

    def test_portuguese_variant_uses_the_pt_glossary(self):
        ids, _ = capture(build.sync_glossaries, "key", {"pt": [("Avatour", "Avatour")]}, ["pt"])
        out, _ = capture(build.translate_with_deepl, "Hello", "PT-BR", "key", ids["pt"])
        self.assertEqual(out, "Hello")


class TestSync(BaseCase):
    T = {"ko": [("Avatour", "Avatour")], "pt": [("Avatour", "Avatour")], "th": [("Avatour", "Avatour")],
         "zh": [("Avatour", "Avatour")]}

    def test_creates_one_glossary_per_supported_language_and_skips_thai(self):
        ids, log = capture(build.sync_glossaries, "key", self.T, ["ko", "pt", "th", "zh"])
        self.assertEqual(set(ids), {"ko", "pt", "zh"})
        posts = self.server.calls("POST", "/v3/glossaries")
        self.assertEqual(len(posts), 3)
        body = {p["params"]["dictionaries"][0]["target_lang"] for p in posts}
        self.assertEqual(body, {"ko", "pt", "zh"})                  # root codes, never PT-BR / ZH-HANS
        d = posts[0]["params"]["dictionaries"][0]
        self.assertEqual(d["source_lang"], "en")
        self.assertEqual(d["entries_format"], "tsv")
        self.assertEqual(d["entries"], "Avatour\tAvatour")
        self.assertIn("TH: DeepL has no glossaries", log)

    def test_second_run_reuses_glossaries(self):
        capture(build.sync_glossaries, "key", self.T, ["ko", "pt"])
        before = len(self.server.calls("POST", "/v3/glossaries"))
        ids, log = capture(build.sync_glossaries, "key", self.T, ["ko", "pt"])
        self.assertEqual(len(self.server.calls("POST", "/v3/glossaries")), before)
        self.assertEqual(len(ids), 2)
        self.assertIn("using existing glossary", log)

    def test_changed_entries_create_new_glossary_and_remove_the_old_one(self):
        capture(build.sync_glossaries, "key", self.T, ["ko"])
        new = {"ko": [("Avatour", "Avatour"), ("Host", "호스트")]}
        ids, log = capture(build.sync_glossaries, "key", new, ["ko"])
        names = [g["name"] for g in self.server.glossaries.values()]
        self.assertEqual(len(names), 1)
        self.assertEqual(names[0], build.glossary_name("ko", new["ko"]))
        self.assertIn("removed outdated glossary", log)

    def test_languages_not_in_the_run_are_left_alone(self):
        capture(build.sync_glossaries, "key", self.T, ["ko", "pt"])
        capture(build.sync_glossaries, "key", {"ko": [("Avatour", "Avatour"), ("Host", "호스트")], "pt": self.T["pt"]}, ["ko"])
        names = sorted(g["name"] for g in self.server.glossaries.values())
        self.assertTrue(any(n.startswith("avatour-guide-pt-") for n in names))   # pt untouched

    def test_other_glossaries_of_the_account_are_never_deleted(self):
        self.server.glossaries["x"] = {"name": "someone-elses-glossary", "source_lang": "en", "target_lang": "ko",
                                       "entries": {"a": "b"}, "polls_left": 0}
        capture(build.sync_glossaries, "key", self.T, ["ko"])
        capture(build.sync_glossaries, "key", {"ko": [("Avatour", "Avatour"), ("Host", "호스트")]}, ["ko"])
        self.assertIn("x", self.server.glossaries)

    def test_waits_until_glossary_is_ready(self):
        self.server.not_ready_polls = 2
        ids, _ = capture(build.sync_glossaries, "key", self.T, ["ko"])
        self.assertIn("ko", ids)
        self.assertGreaterEqual(len(self.server.calls("GET", "/v3/glossaries/")), 2)

    def test_one_failing_language_does_not_block_the_others(self):
        self.server.reject_glossary_langs = {"ko"}
        ids, log = capture(build.sync_glossaries, "key", self.T, ["ko", "pt"])
        self.assertEqual(set(ids), {"pt"})
        self.assertIn("::warning::Could not create the DeepL glossary for KO", log)

    def test_total_api_failure_never_raises(self):
        self.server.fail("GET", "/v3/glossaries", 500, times=99)
        ids, log = capture(build.sync_glossaries, "key", self.T, ["ko"])
        self.assertEqual(ids, {})
        self.assertIn("::warning::", log)


class TestQA(unittest.TestCase):
    def test_ok_when_counts_match(self):
        self.assertEqual(build.qa_check_language(EN_GUIDE, EN_GUIDE.replace("Welcome", "Willkommen"), ["Avatour"]), [])

    def test_detects_a_transliterated_heading(self):
        bad = EN_GUIDE.replace("## 2. Avatour User Types", "## 2. 아바투어 User Types")
        issues = build.qa_check_language(EN_GUIDE, bad, ["Avatour"])
        self.assertEqual(len(issues), 1)
        self.assertIn("2. Avatour User Types", issues[0])

    def test_detects_a_missing_name_in_body_text(self):
        bad = EN_GUIDE.replace("Welcome to Avatour. Avatour helps", "Welcome to X. Avatour helps")
        self.assertEqual(len(build.qa_check_language(EN_GUIDE, bad, ["Avatour"])), 1)

    def test_different_section_structure_falls_back_to_totals(self):
        bad = EN_GUIDE.replace("## 3. Other {#other}", "").replace("Avatour", "XXX", 2)
        issues = build.qa_check_language(EN_GUIDE, bad, ["Avatour"])
        self.assertEqual(len(issues), 1)
        self.assertIn("structure differs", issues[0])


class TestEndToEnd(BaseCase):
    """Runs the real run_auto_translate / run_glossary_qa / main() in a temporary folder."""

    def setUp(self):
        super().setUp()
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp)
        self.cwd = os.getcwd()
        os.chdir(self.tmp)
        self.addCleanup(os.chdir, self.cwd)
        os.makedirs("guide-source")
        self.langs = [lang("en", self.tmp)] + [lang(c, self.tmp) for c in ("ko", "pt", "th")]
        for p in (mock.patch.object(build, 'LANGUAGES', self.langs),
                  mock.patch.dict(os.environ, {"DEEPL_API_KEY": "test-key"}),
                  mock.patch.object(build, 'GLOSSARY_FILE', "guide-source/deepl-glossary.csv")):
            p.start()
            self.addCleanup(p.stop)
        self.en = "guide-source/Avatour User and Best Practices Guide.md"
        self.write(self.en, EN_GUIDE)
        self.write("guide-source/deepl-glossary.csv",
                   "en,it,ko,pt,th\nAvatour,Avatour,Avatour,Avatour,Avatour\n")

    def write(self, path, text):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)

    def read(self, path):
        with open(path, encoding='utf-8') as f:
            return f.read()

    def test_full_run_keeps_the_brand_name_in_every_language(self):
        _, log = capture(build.run_auto_translate)
        ko = self.read("guide-source/Guide - KO.md")
        self.assertIn("## 2. Avatour User Types", ko)
        self.assertNotIn("아바투어", ko)
        # glossary calls: ko + pt created, th skipped
        targets = sorted(p["params"]["dictionaries"][0]["target_lang"]
                         for p in self.server.calls("POST", "/v3/glossaries"))
        self.assertEqual(targets, ["ko", "pt"])
        # translate calls carry the glossary for ko and pt, but not for th
        by_target = {}
        for r in self.server.calls("POST", "/v2/translate"):
            by_target.setdefault(r["params"]["target_lang"], set()).add("glossary_id" in r["params"])
        self.assertEqual(by_target["KO"], {True})
        self.assertEqual(by_target["PT-BR"], {True})
        self.assertEqual(by_target["TH"], {False})
        _, qa = capture(build.run_glossary_qa)
        self.assertNotIn("::warning::", qa)
        self.assertIn("[QA] KO: protected terms (Avatour) OK", qa)

    def test_qa_catches_the_problem_when_the_glossary_cannot_be_created(self):
        self.server.reject_glossary_langs = {"ko"}
        _, log = capture(build.run_auto_translate)
        self.assertIn("아바투어", self.read("guide-source/Guide - KO.md"))     # the bug appears ...
        _, qa = capture(build.run_glossary_qa)
        self.assertIn("::warning::[KO]", qa)                                  # ... and is reported
        self.assertNotIn("::warning::[PT]", qa)

    def test_qa_also_checks_thai_although_deepl_has_no_thai_glossary(self):
        self.write("guide-source/Guide - TH.md", EN_GUIDE.replace("## 2. Avatour User Types", "## 2. TRANSLITERATED User Types"))
        _, qa = capture(build.run_glossary_qa)
        self.assertIn("::warning::[TH]", qa)

    def test_second_run_without_english_changes_makes_no_api_calls(self):
        capture(build.run_auto_translate)
        self.server.requests.clear()
        _, log = capture(build.run_auto_translate)
        self.assertEqual(self.server.requests, [])
        self.assertIn("0 section(s) changed", log)

    def test_changing_one_section_translates_only_that_section(self):
        capture(build.run_auto_translate)
        self.server.requests.clear()
        self.write(self.en, EN_GUIDE.replace("Nothing about the brand here.", "Still nothing about the brand."))
        capture(build.run_auto_translate)
        translated = [r["params"]["text"] for r in self.server.calls("POST", "/v2/translate")]
        self.assertTrue(translated)
        self.assertTrue(all("Other" in t or "brand" in t for t in translated), translated)

    def test_broken_glossary_file_does_not_stop_the_translation(self):
        self.write("guide-source/deepl-glossary.csv", "en,ko\nAvatour,Avatour\nAvatour,Avatour\n")
        _, log = capture(build.run_auto_translate)
        self.assertIn("::warning::Glossary file ignored", log)
        self.assertTrue(os.path.exists("guide-source/Guide - KO.md"))
        self.assertEqual(self.server.calls("POST", "/v3/glossaries"), [])

    def test_no_glossary_file_behaves_like_before(self):
        os.remove("guide-source/deepl-glossary.csv")
        _, log = capture(build.run_auto_translate)
        self.assertEqual(self.server.calls("GET", "/v3/glossaries"), [])
        self.assertTrue(all("glossary_id" not in r["params"] for r in self.server.calls("POST", "/v2/translate")))
        self.assertTrue(os.path.exists("guide-source/Guide - KO.md"))

    def test_main_builds_all_html_files(self):
        capture(build.main)
        for name in ("avatour-guide.html", "avatour-guide-embed.html", "avatour-guide-print.html",
                     "avatour-guide-ko.html", "avatour-guide-embed-ko.html", "avatour-guide-print-th.html"):
            self.assertTrue(os.path.exists(os.path.join("dist", name)), name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
