"""9.6 A tiny web server.

Real-world comparison: a shop counter. The server waits at the
counter; each browser that visits is a customer asking for a page.
The server looks at what was asked for (the path) and hands back the
right page.

Run it:  python 06_web_server.py --serve   then open http://127.0.0.1:8000
Without --serve, it starts, visits its own pages once, and stops.
"""

import sys
import threading
import urllib.request
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

PAGES = {
    "/": "<h1>Welcome to my shop</h1><p><a href='/menu'>See the menu</a></p>",
    "/menu": "<h1>Menu</h1><ul><li>Tea - Rs 20</li><li>Coffee - Rs 40</li></ul>",
}


class ShopHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/time":
            html = f"<p>Server time: {datetime.now():%H:%M:%S}</p>"
            status = 200
        elif self.path in PAGES:
            html, status = PAGES[self.path], 200
        else:
            html, status = "<h1>404 - page not found</h1>", 404
        body = f"<!doctype html><html><body>{html}</body></html>".encode()
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print("  [server]", fmt % args)


if "--serve" in sys.argv:
    print("Serving on http://127.0.0.1:8000  (Ctrl+C to stop)")
    HTTPServer(("127.0.0.1", 8000), ShopHandler).serve_forever()
else:
    server = HTTPServer(("127.0.0.1", 0), ShopHandler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    for path in ["/", "/menu", "/missing"]:
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{server.server_port}{path}") as r:
                print(path, "->", r.status, r.read()[:60])
        except urllib.error.HTTPError as error:
            print(path, "->", error.code)
    server.shutdown()
