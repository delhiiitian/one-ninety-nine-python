"""7.8 Testing with unittest.

Real-world comparison: a car crash test. Engineers check the car does
the right thing BEFORE customers drive it. A test calls your code with
known inputs and checks the answer is what you expect, every time you
change something.

Run:  python 08_testing_unittest.py
  or: python -m unittest 08_testing_unittest.py -v
"""

import unittest


def shipping_cost(weight_kg, express=False):
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    cost = 50 if weight_kg <= 1 else 50 + (weight_kg - 1) * 20
    return cost * 2 if express else cost


class TestShippingCost(unittest.TestCase):
    def test_light_parcel(self):
        self.assertEqual(shipping_cost(0.5), 50)

    def test_heavy_parcel(self):
        self.assertEqual(shipping_cost(3), 90)

    def test_express_doubles(self):
        self.assertEqual(shipping_cost(3, express=True), 180)

    def test_bad_weight(self):
        with self.assertRaises(ValueError):
            shipping_cost(0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
