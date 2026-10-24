"""A tiny command-line client for the to-do API.

    python client.py add "Buy milk" --due 2026-11-01
    python client.py list
    python client.py done 1
    python client.py delete 1
"""

import argparse
import json
import urllib.error
import urllib.request

BASE = "http://127.0.0.1:8000"


def call(method, path, payload=None, base=BASE):
    data = json.dumps(payload).encode() if payload is not None else None
    request = urllib.request.Request(base + path, data=data, method=method,
                                     headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            body = response.read()
            return response.status, json.loads(body) if body else None
    except urllib.error.HTTPError as error:
        return error.code, json.loads(error.read() or b"null")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default=BASE)
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("add")
    add.add_argument("title")
    add.add_argument("--due")
    sub.add_parser("list")
    for name in ("done", "delete"):
        sub.add_parser(name).add_argument("id", type=int)
    args = parser.parse_args()

    if args.command == "add":
        status, body = call("POST", "/todos", {"title": args.title, "due": args.due}, args.base)
    elif args.command == "list":
        status, body = call("GET", "/todos", base=args.base)
        if status == 200:
            for t in body:
                print(f"{'[x]' if t['done'] else '[ ]'} {t['id']:>3}  {t['title']}"
                      + (f"  (due {t['due']})" if t["due"] else ""))
            return
    elif args.command == "done":
        status, body = call("PATCH", f"/todos/{args.id}", {"done": True}, args.base)
    else:
        status, body = call("DELETE", f"/todos/{args.id}", base=args.base)
    print(status, body if body is not None else "")


if __name__ == "__main__":
    main()
