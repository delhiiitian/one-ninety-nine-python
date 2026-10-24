import random
import unittest

import main
from game import hint, new_secret, parse_guess, score


class TestRules(unittest.TestCase):
    def test_hint_directions(self):
        self.assertEqual(hint(10, 10), ("correct", ""))
        self.assertEqual(hint(5, 7), ("higher", "very hot"))
        self.assertEqual(hint(30, 22), ("lower", "warm"))
        self.assertEqual(hint(1, 90), ("higher", "cold"))

    def test_parse_guess(self):
        self.assertEqual(parse_guess(" 12 ", 20), 12)
        self.assertIsNone(parse_guess("abc", 20))
        self.assertIsNone(parse_guess("0", 20))
        self.assertIsNone(parse_guess("21", 20))

    def test_score_rewards_speed_and_level(self):
        self.assertGreater(score("easy", 1), score("easy", 5))
        self.assertGreater(score("hard", 3), score("easy", 3))

    def test_secret_in_range(self):
        rng = random.Random(1)
        for _ in range(100):
            self.assertTrue(1 <= new_secret("hard", rng) <= 100)


class TestFullGame(unittest.TestCase):
    def test_scripted_game(self):
        answers = iter(["medium", "25", "oops", "40", "37", "n"])
        total = main.main(ask=lambda prompt: next(answers),
                          secret_picker=lambda level: 37)
        self.assertEqual(total, score("medium", 3))


if __name__ == "__main__":
    unittest.main()
