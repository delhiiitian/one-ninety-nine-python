"""To-do REST API built only with the standard library.

Run:   python server.py            (http://127.0.0.1:8000)
       python server.py --port 9000 --db my.db

Endpoints:
    GET    /todos              list (optional ?done=true / ?done=false)
    POST   /todos              create   {"title": "...", "due": "2026-11-01"}
    GET    /todos/<id>         one item
    PATCH  /todos/<id>         update   {"done": true}
    DELETE /todos/<id>         remove
    GET    /health             is the server alive?
"""

import argparse
import json
import logging
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from database import TodoStore
from validation import ValidationError, clean_todo

log = logging.getLogger("todo-api")
ITEM_PATH = re.compile(r"^/todos/(\d+)$")
MAX_BODY = 10_000


class TodoHandler(BaseHTTPRequestHandler):
    store: TodoStore = None              # set by make_server()

    # ----- helpers -----
    def send_json(self, status, payload=None):
        body = b"" if payload is None else json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def read_json(self):
        length = int(self.headers.get("Content-Length", 0))
        if length > MAX_BODY:
            raise ValidationError("body too large")
        try:
            return json.loads(self.rfile.read(length) or b"null")
        except json.JSONDecodeError:
            raise ValidationError("body is not valid JSON") from None

    def item_id(self):
        match = ITEM_PATH.match(urlparse(self.path).path)
        return int(match.group(1)) if match else None

    def log_message(self, fmt, *args):
        log.info("%s %s", self.address_string(), fmt % args)

    def handle_safely(self, action):
        try:
            action()
        except ValidationError as error:
            self.send_json(400, {"error": str(error)})
        except Exception:                       # never leak a traceback to clients
            log.exception("unexpected error")
            self.send_json(500, {"error": "internal server error"})

    # ----- routes -----
    def do_GET(self):
        self.handle_safely(self._get)

    def do_POST(self):
        self.handle_safely(self._post)

    def do_PATCH(self):
        self.handle_safely(self._patch)

    def do_DELETE(self):
        self.handle_safely(self._delete)

    def _get(self):
        url = urlparse(self.path)
        if url.path == "/health":
            return self.send_json(200, {"status": "ok"})
        if url.path == "/todos":
            done = parse_qs(url.query).get("done", [None])[0]
            if done not in (None, "true", "false"):
                raise ValidationError("done must be true or false")
            flag = None if done is None else done == "true"
            return self.send_json(200, self.store.list(done=flag))
        todo_id = self.item_id()
        todo = self.store.get(todo_id) if todo_id else None
        if todo is None:
            return self.send_json(404, {"error": "not found"})
        self.send_json(200, todo)

    def _post(self):
        if urlparse(self.path).path != "/todos":
            return self.send_json(404, {"error": "not found"})
        fields = clean_todo(self.read_json())
        todo = self.store.create(fields["title"], fields.get("due"))
        self.send_json(201, todo)

    def _patch(self):
        todo_id = self.item_id()
        if todo_id is None or self.store.get(todo_id) is None:
            return self.send_json(404, {"error": "not found"})
        fields = clean_todo(self.read_json(), partial=True)
        self.send_json(200, self.store.update(todo_id, **fields))

    def _delete(self):
        todo_id = self.item_id()
        if todo_id is None or not self.store.delete(todo_id):
            return self.send_json(404, {"error": "not found"})
        self.send_json(204)


def make_server(host="127.0.0.1", port=8000, db_path="todos.db"):
    handler = type("BoundTodoHandler", (TodoHandler,), {"store": TodoStore(db_path)})
    return ThreadingHTTPServer((host, port), handler)


def main():
    parser = argparse.ArgumentParser(description="Run the to-do REST API.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--db", default="todos.db")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    server = make_server(args.host, args.port, args.db)
    print(f"To-do API on http://{args.host}:{args.port}  (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
