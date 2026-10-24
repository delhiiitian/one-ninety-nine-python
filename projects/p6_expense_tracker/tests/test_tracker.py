import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

import reports
import storage
import tracker


class TestTracker(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.csv = Path(self.tmp.name) / "spend.csv"

    def tearDown(self):
        self.tmp.cleanup()

    def test_missing_file_means_empty(self):
        self.assertEqual(storage.load(self.csv), ([], []))

    def test_add_then_load(self):
        tracker.main(["--file", str(self.csv), "add", "450", "Food", "Pizza", "--date", "2026-10-02"])
        tracker.main(["--file", str(self.csv), "add", "100", "transport"])
        expenses, problems = storage.load(self.csv)
        self.assertEqual(problems, [])
        self.assertEqual(len(expenses), 2)
        self.assertEqual(expenses[0].category, "food")
        self.assertEqual(expenses[0].date, date(2026, 10, 2))

    def test_bad_rows_are_skipped(self):
        self.csv.write_text("date,category,amount,note\n2026-10-01,food,abc,x\n"
                            "2026-10-02,food,50,ok\n", encoding="utf-8")
        expenses, problems = storage.load(self.csv)
        self.assertEqual(len(expenses), 1)
        self.assertIn("line 2", problems[0])

    def test_reports(self):
        expenses, _ = storage.load()          # the sample file
        october = reports.in_month(expenses, 2026, 10)
        self.assertEqual(len(october), 8)
        totals = reports.by_category(october)
        self.assertEqual(list(totals)[0], "groceries")
        self.assertEqual(totals["groceries"], 6540)
        over = reports.check_budgets(october, {"groceries": 5000, "food": 2000})
        self.assertEqual(over, [("groceries", 6540, 5000)])
        self.assertEqual(reports.monthly_totals(expenses)["2026-09"], 25000)

    def test_export_json(self):
        expenses, _ = storage.load()
        out = Path(self.tmp.name) / "out.json"
        self.assertEqual(storage.export_json(expenses, out), 9)
        self.assertEqual(json.loads(out.read_text())[0]["category"], "rent")

    def test_negative_amount_refused(self):
        self.assertEqual(tracker.main(["--file", str(self.csv), "add", "-5", "food"]), 1)
        self.assertFalse(self.csv.exists())


if __name__ == "__main__":
    unittest.main()
