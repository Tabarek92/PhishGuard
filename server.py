#!/usr/bin/env python3
"""
PhishGuard local server — serves index.html and proxies Anthropic API calls.
Run:  python3 server.py
Then open:  http://localhost:8080
"""
import http.server
import urllib.request
import urllib.error
import os

PORT = 8080
ANTHROPIC_URL = 'https://api.anthropic.com/v1/messages'


class Handler(http.server.SimpleHTTPRequestHandler):
    # ── CORS pre-flight ───────────────────────────────────────
    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    # ── Proxy POST /proxy → Anthropic ─────────────────────────
    def do_POST(self):
        if self.path != '/proxy':
            self.send_error(404)
            return

        length = int(self.headers.get('Content-Length', 0))
        body   = self.rfile.read(length)

        req = urllib.request.Request(
            ANTHROPIC_URL,
            data=body,
            headers={
                'Content-Type':      'application/json',
                'x-api-key':         self.headers.get('x-api-key', ''),
                'anthropic-version': self.headers.get('anthropic-version', '2023-06-01'),
            },
        )

        try:
            with urllib.request.urlopen(req) as resp:
                data   = resp.read()
                status = resp.status
        except urllib.error.HTTPError as e:
            data   = e.read()
            status = e.code

        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self._cors()
        self.end_headers()
        self.wfile.write(data)

    # ── Suppress request logs ─────────────────────────────────
    def log_message(self, fmt, *args):
        pass

    def _cors(self):
        self.send_header('Access-Control-Allow-Origin',  '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers',
                         'Content-Type, x-api-key, anthropic-version')


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with http.server.HTTPServer(('', PORT), Handler) as srv:
        print(f'PhishGuard → http://localhost:{PORT}')
        srv.serve_forever()
