# Project 9: To-do REST API

Chapter 9 project of **Python in 199 Pages**. A real web API, built only with the
standard library: an HTTP server that handles many clients at once, a SQLite
database, JSON in and out, input validation with regular expressions and dates,
logging, and a command-line client.

## Layout

```
p9_todo_api/
├── server.py       # HTTP routes: GET / POST / PATCH / DELETE
├── database.py     # TodoStore: all the SQL
├── validation.py   # checks every request body
├── client.py       # command-line client using urllib
└── tests/
    └── test_api.py # starts a real server on a free port and calls it
```

## Run it

In one terminal:

```bash
python server.py
```

In another:

```bash
python client.py add "Buy milk" --due 2026-11-01
python client.py list
python client.py done 1
curl http://127.0.0.1:8000/todos
```

## Test it

```bash
python -m unittest discover -s tests -t . -v
```

## Ideas to extend

- Add an `X-API-Key` header check.
- Rewrite it with Flask or FastAPI (`pip install fastapi uvicorn`) and compare.
- Add a simple HTML page that calls the API with JavaScript.
