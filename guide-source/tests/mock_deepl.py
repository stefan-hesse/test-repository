"""A small fake DeepL server for the automated tests (no network, no cost).

It follows the DeepL API documentation (November 2026):
  GET/POST /v3/glossaries, GET/DELETE /v3/glossaries/{id}, POST /v2/translate.
It also reproduces the real-world problem this project is protecting against:
Korean text translated WITHOUT a glossary has "Avatour" turned into "아바투어".
"""
import json, threading, uuid, urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# Glossary languages DeepL documents (Thai is NOT among them).
GLOSSARY_LANGS = set("ar bg cs da de el en es et fi fr he hu id it ja ko lt lv nb nl pl pt ro ru sk sl sv tr uk vi zh".split())


class MockDeepL:
    def __init__(self):
        self.glossaries = {}          # id -> {name, source_lang, target_lang, entries(dict), polls_left}
        self.requests = []            # every request: {method, path, params}
        self.failures = []            # injected failures
        self.reject_glossary_langs = set()
        self.not_ready_polls = 0      # newly created glossaries report ready=False this many times
        self.translate_calls = 0

    # -- control for tests ------------------------------------------------
    def fail(self, method, path_prefix, status, times=1, message="injected failure"):
        self.failures.append({"method": method, "prefix": path_prefix, "status": status,
                              "times": times, "message": message})

    def calls(self, method, path_prefix):
        return [r for r in self.requests if r["method"] == method and r["path"].startswith(path_prefix)]

    def start(self):
        mock = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def _send(self, status, payload=None):
                body = b"" if payload is None else json.dumps(payload).encode("utf-8")
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("X-Trace-ID", "mock-trace")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def _handle(self, method):
                length = int(self.headers.get("Content-Length") or 0)
                raw = self.rfile.read(length) if length else b""
                ctype = self.headers.get("Content-Type", "")
                if "json" in ctype and raw:
                    params = json.loads(raw)
                elif raw:
                    params = {k: v[0] for k, v in urllib.parse.parse_qs(raw.decode("utf-8")).items()}
                else:
                    params = {}
                path = self.path
                mock.requests.append({"method": method, "path": path, "params": params,
                                      "auth": self.headers.get("Authorization", "")})
                for f in mock.failures:
                    if f["method"] == method and path.startswith(f["prefix"]) and f["times"] > 0:
                        f["times"] -= 1
                        return self._send(f["status"], {"message": f["message"]})
                if not self.headers.get("Authorization", "").startswith("DeepL-Auth-Key "):
                    return self._send(403, {"message": "Forbidden"})
                return mock._route(self, method, path, params)

            def do_GET(self):
                self._handle("GET")

            def do_POST(self):
                self._handle("POST")

            def do_DELETE(self):
                self._handle("DELETE")

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.url = f"http://127.0.0.1:{self.server.server_address[1]}"
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        return self

    def stop(self):
        self.server.shutdown()
        self.server.server_close()

    # -- API behaviour ----------------------------------------------------
    def _glossary_json(self, gid, g, ready=True):
        return {"glossary_id": gid, "ready": ready, "name": g["name"],
                "dictionaries": [{"source_lang": g["source_lang"].upper(), "target_lang": g["target_lang"].upper(),
                                  "entry_count": len(g["entries"])}],
                "creation_time": "2026-11-15T12:00:00.000Z"}

    def _route(self, h, method, path, params):
        if path == "/v3/glossaries" and method == "GET":
            return h._send(200, {"glossaries": [self._glossary_json(i, g) for i, g in self.glossaries.items()]})
        if path == "/v3/glossaries" and method == "POST":
            dicts = params.get("dictionaries") or []
            if not params.get("name") or len(dicts) != 1:
                return h._send(400, {"message": "Invalid request"})
            d = dicts[0]
            target = d.get("target_lang", "").lower()
            if target not in GLOSSARY_LANGS or target in self.reject_glossary_langs or d.get("source_lang") != "en":
                return h._send(400, {"message": "Invalid language", "detail": f"target {target} not supported"})
            entries = {}
            for line in d.get("entries", "").split("\n"):
                if not line:
                    continue
                parts = line.split("\t")
                if len(parts) != 2 or not parts[0] or not parts[1]:
                    return h._send(400, {"message": "Invalid glossary entries provided"})
                if parts[0] in entries:
                    return h._send(400, {"message": "Invalid glossary entries provided", "detail": "duplicate key"})
                entries[parts[0]] = parts[1]
            if not entries:
                return h._send(400, {"message": "Invalid glossary entries provided"})
            gid = str(uuid.uuid4())
            self.glossaries[gid] = {"name": params["name"], "source_lang": "en", "target_lang": target,
                                    "entries": entries, "polls_left": self.not_ready_polls}
            return h._send(201, self._glossary_json(gid, self.glossaries[gid], ready=self.not_ready_polls == 0))
        if path.startswith("/v3/glossaries/"):
            gid = path.rsplit("/", 1)[1]
            if gid not in self.glossaries:
                return h._send(404, {"message": "Glossary not found"})
            if method == "GET":
                g = self.glossaries[gid]
                ready = g["polls_left"] <= 0
                g["polls_left"] -= 1
                return h._send(200, self._glossary_json(gid, g, ready=ready))
            if method == "DELETE":
                del self.glossaries[gid]
                return h._send(204)
        if path == "/v2/translate" and method == "POST":
            return self._translate(h, params)
        return h._send(404, {"message": "Not found"})

    def _translate(self, h, params):
        self.translate_calls += 1
        text, target = params.get("text", ""), params.get("target_lang", "")
        root = target.split("-")[0].lower()
        kept = set()
        gid = params.get("glossary_id")
        if gid:
            g = self.glossaries.get(gid)
            if not g or g["target_lang"] != root:
                return h._send(400, {"message": "Glossary does not match the language pair"})
            kept = {k for k, v in g["entries"].items() if k == v}
        out = text
        if root == "ko" and "Avatour" not in kept:      # the real-world problem
            out = out.replace("Avatour", "아바투어")
        return h._send(200, {"translations": [{"detected_source_language": "EN", "text": out}]})
