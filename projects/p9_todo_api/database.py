"""All SQL lives here. Every function opens a short connection, so it is thread safe."""

import sqlite3
from contextlib import closing
from datetime import datetime, timezone

SCHEMA = """
CREATE TABLE IF NOT EXISTS todos (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    title      TEXT    NOT NULL,
    done       INTEGER NOT NULL DEFAULT 0,
    due        TEXT,
    created_at TEXT    NOT NULL
)
"""


class TodoStore:
    def __init__(self, path="todos.db"):
        self.path = path
        with closing(self._connect()) as db, db:
            db.execute(SCHEMA)

    def _connect(self):
        db = sqlite3.connect(self.path)
        db.row_factory = sqlite3.Row
        return db

    @staticmethod
    def _to_dict(row):
        return {"id": row["id"], "title": row["title"], "done": bool(row["done"]),
                "due": row["due"], "created_at": row["created_at"]}

    def list(self, done=None):
        sql, params = "SELECT * FROM todos", ()
        if done is not None:
            sql, params = sql + " WHERE done = ?", (int(done),)
        with closing(self._connect()) as db:
            return [self._to_dict(r) for r in db.execute(sql + " ORDER BY id", params)]

    def get(self, todo_id):
        with closing(self._connect()) as db:
            row = db.execute("SELECT * FROM todos WHERE id = ?", (todo_id,)).fetchone()
        return self._to_dict(row) if row else None

    def create(self, title, due=None):
        now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        with closing(self._connect()) as db, db:
            cursor = db.execute("INSERT INTO todos (title, due, created_at) VALUES (?, ?, ?)",
                                (title, due, now))
        return self.get(cursor.lastrowid)

    def update(self, todo_id, **fields):
        allowed = {k: v for k, v in fields.items() if k in ("title", "done", "due")}
        if allowed:
            assignments = ", ".join(f"{column} = ?" for column in allowed)
            values = [int(v) if k == "done" else v for k, v in allowed.items()]
            with closing(self._connect()) as db, db:
                db.execute(f"UPDATE todos SET {assignments} WHERE id = ?", (*values, todo_id))
        return self.get(todo_id)

    def delete(self, todo_id):
        with closing(self._connect()) as db, db:
            return db.execute("DELETE FROM todos WHERE id = ?", (todo_id,)).rowcount > 0
