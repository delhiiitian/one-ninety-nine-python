import unittest

from bill import build_bill, format_receipt, split, subtotal, tax_amount


class TestBill(unittest.TestCase):
    items = [("Masala dosa", 120, 2), ("Filter coffee", 40, 3)]

    def test_subtotal(self):
        self.assertEqual(subtotal(self.items), 360)

    def test_tax(self):
        self.assertEqual(tax_amount(360), 18.0)

    def test_split_rounds_up(self):
        self.assertEqual(split(100, 3), (34, 2.0))

    def test_split_exact(self):
        self.assertEqual(split(90, 3), (30, 0))

    def test_split_needs_people(self):
        with self.assertRaises(ValueError):
            split(100, 0)

    def test_build_bill(self):
        bill = build_bill(self.items, tip_percent=10, people=4)
        self.assertEqual(bill["total"], 414.0)    # 360 + 18 + 36
        self.assertEqual(bill["share"], 104)

    def test_receipt_mentions_total(self):
        text = format_receipt(build_bill(self.items, 10, 4))
        self.assertIn("TOTAL", text)
        self.assertIn("414.00", text)


if __name__ == "__main__":
    unittest.main()
