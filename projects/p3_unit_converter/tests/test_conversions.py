import unittest

import main
from conversions import convert, convert_temperature, format_result


class TestConversions(unittest.TestCase):
    def test_length(self):
        self.assertAlmostEqual(convert("length", 1, "km", "m"), 1000)
        self.assertAlmostEqual(convert("length", 1, "mile", "km"), 1.609344)
        self.assertAlmostEqual(convert("length", 12, "inch", "foot"), 1)

    def test_weight(self):
        self.assertAlmostEqual(convert("weight", 1, "kg", "pound"), 2.20462, places=4)

    def test_volume(self):
        self.assertAlmostEqual(convert("volume", 2, "l", "ml"), 2000)

    def test_temperature(self):
        self.assertAlmostEqual(convert_temperature(100, "c", "f"), 212)
        self.assertAlmostEqual(convert_temperature(32, "f", "c"), 0)
        self.assertAlmostEqual(convert_temperature(0, "k", "c"), -273.15)
        self.assertAlmostEqual(convert("temperature", -40, "F", "C"), -40)

    def test_unknown_unit(self):
        with self.assertRaises(KeyError):
            convert("length", 1, "km", "parsec")

    def test_format(self):
        self.assertEqual(format_result(5, "km", 3.10686, "mile"), "5 km = 3.1069 mile")


class TestMenu(unittest.TestCase):
    def test_bad_value_message(self):
        answers = iter(["km", "m", "lots"])
        message = main.ask_conversion("length", lambda _: next(answers))
        self.assertIn("not a number", message)


if __name__ == "__main__":
    unittest.main()
