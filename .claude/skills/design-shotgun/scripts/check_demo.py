#!/usr/bin/env python3
"""Statische Prüfung einer Demo-HTML-Datei (ohne Node, ohne Browser).

- extrahiert alle Inline-<script>-Blöcke und prüft die JS-Syntax mit macOS JavaScriptCore (jsc)
- prüft, dass die Importmap nur gepinnte CDN-Versionen nutzt
- meldet externe Ressourcen

Aufruf: python3 -I check_demo.py <datei.html> [<datei.html> ...]
"""
import json
import re
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path

JSC = "/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc"
ALLOWED_HOSTS = ("cdn.jsdelivr.net", "cdnjs.cloudflare.com", "unpkg.com", "fonts.googleapis.com", "fonts.gstatic.com")


class ScriptCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.scripts = []  # (type, src, body)
        self.links = []
        self._cur = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "script":
            self._cur = [a.get("type", ""), a.get("src"), ""]
        elif tag == "link" and a.get("href"):
            self.links.append(a["href"])

    def handle_data(self, data):
        if self._cur is not None:
            self._cur[2] += data

    def handle_endtag(self, tag):
        if tag == "script" and self._cur is not None:
            self.scripts.append(tuple(self._cur))
            self._cur = None


def jsc_check(src, module):
    fn = "checkModuleSyntax" if module else "checkSyntax"
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(src)
        path = f.name
    if module:
        code = f'checkModuleSyntax(readFile({json.dumps(path)})); print("OK")'
    else:
        code = f'checkSyntax({json.dumps(path)}); print("OK")'
    r = subprocess.run([JSC, "-e", code], capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    Path(path).unlink(missing_ok=True)
    return out.endswith("OK"), out.replace(path, "<inline>"), fn


def check(file):
    html = Path(file).read_text(encoding="utf-8")
    p = ScriptCollector()
    p.feed(html)
    problems = []
    for i, (typ, src, body) in enumerate(p.scripts):
        if src:
            if not src.startswith("https://") or not any(h in src for h in ALLOWED_HOSTS):
                problems.append(f"script src nicht erlaubt: {src}")
            if not re.search(r"@\d+\.\d+\.\d+", src) and "/ajax/libs/" not in src:
                problems.append(f"script src ohne exakte Version: {src}")
            continue
        if typ == "importmap":
            try:
                imports = json.loads(body).get("imports", {})
            except json.JSONDecodeError as e:
                problems.append(f"importmap kein gültiges JSON: {e}")
                continue
            for k, url in imports.items():
                if not re.search(r"@\d+\.\d+\.\d+", url):
                    problems.append(f"importmap '{k}' ohne exakte Version: {url}")
            continue
        if typ not in ("", "module", "text/javascript"):
            continue  # z.B. Shader in <script type="x-shader">
        ok, out, fn = jsc_check(body, typ == "module")
        if not ok:
            problems.append(f"Script #{i} ({typ or 'classic'}) Syntaxfehler: {out}")
    for href in p.links:
        if href.startswith("http") and not any(h in href for h in ALLOWED_HOSTS):
            problems.append(f"link href nicht erlaubt: {href}")
    print(f"{'OK  ' if not problems else 'FAIL'} {file}  ({len(p.scripts)} scripts, {len(html)//1024} KB)")
    for pr in problems:
        print("   -", pr)
    return not problems


if __name__ == "__main__":
    results = [check(f) for f in sys.argv[1:]]
    sys.exit(0 if all(results) else 1)
