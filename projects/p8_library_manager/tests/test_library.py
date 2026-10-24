import unittest
from datetime import date, timedelta

from library import (Book, EBook, Item, Library, LimitReachedError, Member,
                     NotAvailableError, UnknownItemError)

DAY = date(2026, 10, 1)


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.lib = Library("Test")
        self.lib.add(Book("B1", "Zen", 2000, copies=1, author="A"),
                     EBook("E1", "Alpha", 2010, author="B"),
                     Item("M1", "Map", 2020))
        self.lib.join(Member("U1", "Asha", max_loans=2))
        self.lib.join(Member("U2", "Ben"))

    def test_iteration_sorted_by_title(self):
        self.assertEqual([i.title for i in self.lib], ["Alpha", "Map", "Zen"])

    def test_dunder_methods(self):
        self.assertEqual(len(self.lib), 3)
        self.assertIn("B1", self.lib)
        with self.assertRaises(UnknownItemError):
            self.lib["X9"]

    def test_borrow_and_due_dates(self):
        self.assertEqual(self.lib.borrow("U1", "B1", DAY), DAY + timedelta(days=14))
        self.assertEqual(self.lib.borrow("U2", "E1", DAY), DAY + timedelta(days=7))
        self.assertEqual(self.lib["B1"].available, 0)

    def test_no_copies_left(self):
        self.lib.borrow("U1", "B1", DAY)
        with self.assertRaises(NotAvailableError):
            self.lib.borrow("U2", "B1", DAY)

    def test_ebooks_never_run_out(self):
        self.lib.borrow("U1", "E1", DAY)
        self.lib.borrow("U2", "E1", DAY)
        self.assertEqual(self.lib["E1"].available, 1)

    def test_loan_limit(self):
        self.lib.borrow("U1", "B1", DAY)
        self.lib.borrow("U1", "E1", DAY)
        with self.assertRaises(LimitReachedError):
            self.lib.borrow("U1", "M1", DAY)

    def test_late_fees(self):
        self.lib.borrow("U1", "B1", DAY)
        self.lib.borrow("U1", "E1", DAY)
        late = DAY + timedelta(days=17)
        self.assertEqual(list(self.lib.overdue(late)), [("Asha", "Zen", 3)])
        self.assertEqual(self.lib.give_back("U1", "B1", late), 15)
        self.assertEqual(self.lib.give_back("U1", "E1", late), 0)

    def test_reading_room_always_returns(self):
        with self.assertRaises(RuntimeError):
            with self.lib.reading_room("U1", "M1"):
                raise RuntimeError("spilled coffee")
        self.assertEqual(self.lib["M1"].available, 1)
        self.assertEqual(len(self.lib.members["U1"]), 0)

    def test_str_uses_overrides(self):
        self.assertEqual(str(self.lib["B1"]), "[B1] Zen (2000) by A - 1/1 in")
        self.assertEqual(str(self.lib["E1"]), "[E1] Alpha (2010) by B - e-book, always in")

    def test_search_is_lazy_generator(self):
        results = self.lib.search("a")
        self.assertEqual(next(results).title, "Alpha")

    def test_activity_log_decorator(self):
        self.lib.borrow("U2", "M1", DAY)
        self.assertEqual(self.lib.activity, ["borrow: U2, M1"])


if __name__ == "__main__":
    unittest.main()
