"""9.3 Making HTTP requests: talking to websites.

Real-world comparison: sending a letter and getting a reply. Your
program writes a request ("GET /weather"), a server reads it and
posts back a response with a status code (200 = OK, 404 = not found)
and a body.

To run anywhere (even offline), this file starts a tiny server on
your own computer first, then sends requests to it.
"""

import json
import threading
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer


class WeatherHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/weather":
            body = json.dumps({"city": "Pune", "temp_c": 27}).encode()
            self.send_response(200)
        else:
            body = b'{"error": "not found"}'
            self.send_response(404)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):     # keep the output quiet
        pass


server = HTTPServer(("127.0.0.1", 0), WeatherHandler)   # port 0 = any free port
threading.Thread(target=server.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{server.server_port}"

# A GET request with urllib (built in, no install needed).
with urllib.request.urlopen(f"{base}/weather", timeout=5) as response:
    print("Status:", response.status)
    print("Content-Type:", response.headers["Content-Type"])
    data = json.loads(response.read())
print(f"It is {data['temp_c']} C in {data['city']}")

# Errors come back as exceptions you can catch.
try:
    urllib.request.urlopen(f"{base}/nowhere", timeout=5)
except urllib.error.HTTPError as error:
    print("Request failed with status", error.code)

server.shutdown()

# With the popular 'requests' package (pip install requests), the same
# call is:  requests.get(url, timeout=5).json()
