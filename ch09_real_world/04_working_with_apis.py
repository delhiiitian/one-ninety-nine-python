"""9.4 Working with REST APIs: read and send JSON.

Real-world comparison: a restaurant waiter. You (the client) do not
walk into the kitchen. You give the waiter (the API) an order in an
agreed format, and the waiter brings back exactly what you asked for.
GET reads, POST creates, PUT updates, DELETE removes.

This file runs a small fake "notes" API locally so it works offline.
"""

import json
import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

NOTES = {1: {"id": 1, "text": "Buy milk"}}


class NotesAPI(BaseHTTPRequestHandler):
    def _send(self, status, payload):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._send(200, list(NOTES.values()))

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        note = json.loads(self.rfile.read(length))
        note["id"] = max(NOTES) + 1
        NOTES[note["id"]] = note
        self._send(201, note)

    def log_message(self, *args):
        pass


server = HTTPServer(("127.0.0.1", 0), NotesAPI)
threading.Thread(target=server.serve_forever, daemon=True).start()
url = f"http://127.0.0.1:{server.server_port}/notes"


def api(method, url, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    request = urllib.request.Request(
        url, data=data, method=method,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=5) as response:
        return response.status, json.loads(response.read())


status, notes = api("GET", url)
print(status, "Notes:", notes)

status, created = api("POST", url, {"text": "Call the bank"})
print(status, "Created:", created)

status, notes = api("GET", url)
print(status, "Now:", [n["text"] for n in notes])

server.shutdown()

# Real APIs usually need a key sent in a header, for example:
#   headers={"Authorization": "Bearer <your-api-key>"}
# Never write a real key inside your code; read it from an environment variable.
