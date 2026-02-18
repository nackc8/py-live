#!/usr/bin/env python3
"""Web UI for browsing and replaying .cast recordings."""

import http.server
import socketserver
import threading
import time
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SHARED = REPO_ROOT / ".shared"
PORT = 7777

_STATIC = {
    "/player.js":        (SHARED / "asciinema-player.min.js",      "text/javascript"),
    "/player.css":       (SHARED / "asciinema-player.css",         "text/css"),
    "/player-worker.js": (SHARED / "asciinema-player-worker.min.js", "text/javascript"),
}

_PING_JS = '<script>setInterval(() => fetch("/ping").catch(()=>{}), 1000)</script>'

_last_ping = None  # None until the first browser ping arrives


def _cast_files():
    return sorted(
        f.relative_to(REPO_ROOT)
        for f in REPO_ROOT.rglob("recordings/*.cast")
    )


def _page_list():
    items = [
        f'<li><a href="/play?f={urllib.parse.quote(str(f))}">{f}</a></li>'
        for f in _cast_files()
    ]
    body = "<ul>\n" + "\n".join(items) + "\n</ul>" if items else "<p>No recordings found.</p>"
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Recordings</title>
<style>body{{font-family:monospace;padding:1em 2em}}</style>
</head><body>
<h1>Recordings</h1>
{body}
{_PING_JS}
</body></html>"""


def _page_player(rel_path):
    cast_url = "/cast/" + urllib.parse.quote(rel_path)
    base = Path(rel_path).with_suffix("")
    links = []
    for ext, label in ((".html", "cleaned HTML"), (".txt", "cleaned text")):
        if (REPO_ROOT / base.with_suffix(ext)).is_file():
            url = "/rec/" + urllib.parse.quote(str(base.with_suffix(ext)))
            links.append(f'<a href="{url}">{label}</a>')
    extras = "  |  ".join(links)
    extras_html = f'<p>{extras}</p>' if extras else ""
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{rel_path}</title>
<link rel="stylesheet" href="/player.css">
<style>body{{font-family:monospace;padding:1em 2em}}</style>
</head><body>
<p><a href="/">← recordings</a></p>
<h2>{rel_path}</h2>
<div id="player"></div>
{extras_html}<script src="/player.js"></script>
<script>AsciinemaPlayer.create("{cast_url}", document.getElementById("player"), {{
    autoPlay: true,
    workerUrl: "/player-worker.js"
}});</script>
{_PING_JS}
</body></html>"""


class _Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global _last_ping
        parsed = urllib.parse.urlparse(self.path)
        qs = urllib.parse.parse_qs(parsed.query)

        if parsed.path == "/ping":
            _last_ping = time.monotonic()
            self.send_response(204)
            self.end_headers()
        elif parsed.path in ("/", "/index"):
            self._send_html(_page_list())
        elif parsed.path == "/play":
            rel = urllib.parse.unquote(qs.get("f", [""])[0])
            self._send_html(_page_player(rel)) if rel else self.send_error(400)
        elif parsed.path.startswith("/cast/"):
            self._send_cast(urllib.parse.unquote(parsed.path[len("/cast/"):]))
        elif parsed.path.startswith("/rec/"):
            self._send_rec(urllib.parse.unquote(parsed.path[len("/rec/"):]))
        elif parsed.path in _STATIC:
            self._send_file(*_STATIC[parsed.path])
        else:
            self.send_error(404)

    def _send_html(self, content):
        data = content.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_file(self, path, content_type):
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _send_rec(self, rel_path):
        target = (REPO_ROOT / rel_path).resolve()
        try:
            target.relative_to(REPO_ROOT.resolve())
        except ValueError:
            self.send_error(403)
            return
        if not target.is_file() or target.suffix not in (".txt", ".html"):
            self.send_error(404)
            return
        content_type = "text/html; charset=utf-8" if target.suffix == ".html" else "text/plain; charset=utf-8"
        self._send_file(target, content_type)

    def _send_cast(self, rel_path):
        target = (REPO_ROOT / rel_path).resolve()
        try:
            target.relative_to(REPO_ROOT.resolve())
        except ValueError:
            self.send_error(403)
            return
        if not target.is_file() or target.suffix != ".cast":
            self.send_error(404)
            return
        data = target.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        pass  # suppress per-request noise


class _Server(socketserver.TCPServer):
    allow_reuse_address = True


port = PORT
while True:
    try:
        server = _Server(("", port), _Handler)
        break
    except OSError:
        port += 1


def _watchdog():
    start = time.monotonic()
    while True:
        time.sleep(1)
        if _last_ping is None:
            if time.monotonic() - start > 60:
                print("No browser connected within 60 seconds, exiting.")
                server.shutdown()
                return
        elif time.monotonic() - _last_ping > 2:
            print("Browser disconnected, exiting.")
            server.shutdown()
            return


threading.Thread(target=_watchdog, daemon=True).start()

try:
    with server:
        print(f"Recordings: http://localhost:{port}/")
        server.serve_forever()
except KeyboardInterrupt:
    pass
