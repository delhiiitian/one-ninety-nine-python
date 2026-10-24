import tempfile
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from client import call
from server import make_server
from validation import ValidationError, clean_todo


class TestValidation(unittest.TestCase):
    def test_good(self):
        self.assertEqual(clean_todo({"title": " Milk ", "due": "2026-11-01"}),
                         {"title": "Milk", "due": "2026-11-01"})

    def test_bad(self):
        for data in [{}, {"title": ""}, {"title": "x", "due": "tomorrow"},
                     {"title": "x", "due": "2026-02-30"}, {"title": "x", "done": "yes"},
                     {"title": "x", "colour": "red"}, ["not", "a", "dict"]]:
            with self.assertRaises(ValidationError, msg=data):
                clean_todo(data)

    def test_partial(self):
        self.assertEqual(clean_todo({"done": True}, partial=True), {"done": True})


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.server = make_server(port=0, db_path=str(Path(cls.tmp.name) / "test.db"))
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.tmp.cleanup()

    def api(self, method, path, payload=None):
        return call(method, path, payload, base=self.base)

    def test_health(self):
        self.assertEqual(self.api("GET", "/health"), (200, {"status": "ok"}))

    def test_full_lifecycle(self):
        status, todo = self.api("POST", "/todos", {"title": "Write chapter 9", "due": "2026-11-01"})
        self.assertEqual(status, 201)
        self.assertFalse(todo["done"])
        path = f"/todos/{todo['id']}"

        self.assertEqual(self.api("GET", path)[1]["title"], "Write chapter 9")
        status, updated = self.api("PATCH", path, {"done": True})
        self.assertEqual((status, updated["done"]), (200, True))
        self.assertIn(todo["id"], [t["id"] for t in self.api("GET", "/todos?done=true")[1]])
        self.assertEqual(self.api("DELETE", path)[0], 204)
        self.assertEqual(self.api("GET", path)[0], 404)

    def test_errors(self):
        self.assertEqual(self.api("POST", "/todos", {"title": ""})[0], 400)
        self.assertEqual(self.api("GET", "/todos?done=maybe")[0], 400)
        self.assertEqual(self.api("PATCH", "/todos/99999", {"done": True})[0], 404)
        self.assertEqual(self.api("GET", "/nothing")[0], 404)

    def test_many_clients_at_once(self):
        with ThreadPoolExecutor(max_workers=10) as pool:
            results = list(pool.map(
                lambda n: self.api("POST", "/todos", {"title": f"task {n}"})[0], range(20)))
        self.assertEqual(results, [201] * 20)


if __name__ == "__main__":
    unittest.main()
