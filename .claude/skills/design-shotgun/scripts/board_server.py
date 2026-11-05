#!/usr/bin/env python3
"""Mini-Server für das Vergleichsboard (nur Python-Standardbibliothek).

- liefert ein Explorations-Verzeichnis statisch aus (Demos + board.html)
- nimmt POST /feedback entgegen und speichert den Body als feedback.json im selben Verzeichnis
- schreibt "FEEDBACK_RECEIVED <pfad>" auf stdout, damit Claude es mitbekommt

Aufruf: python3 -I board_server.py <explorations-verzeichnis> [port]
"""
import json
import sys
from datetime import datetime
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

MAX_BODY = 256 * 1024


class BoardHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/feedback":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", 0))
        if not 0 < length <= MAX_BODY:
            self.send_error(413)
            return
        try:
            data = json.loads(self.rfile.read(length))
        except json.JSONDecodeError:
            self.send_error(400, "kein gültiges JSON")
            return
        data["received_at"] = datetime.now().isoformat(timespec="seconds")
        out = Path(self.directory) / "feedback.json"
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"FEEDBACK_RECEIVED {out}", flush=True)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"ok":true}')

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass  # ruhig bleiben, nur Feedback-Events ausgeben


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    root = Path(sys.argv[1]).resolve()
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8765
    server = ThreadingHTTPServer(("127.0.0.1", port), partial(BoardHandler, directory=str(root)))
    print(f"BOARD_URL http://127.0.0.1:{port}/board.html  (root: {root})", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
