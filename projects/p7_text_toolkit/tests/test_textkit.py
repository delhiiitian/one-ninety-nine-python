import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import textkit
from textkit.__main__ import main
from textkit.readability import describe, syllables

SAMPLE = Path(__file__).parent.parent / "sample.txt"


class TestStats(unittest.TestCase):
    def test_words(self):
        self.assertEqual(textkit.words("It's a dog's life!"), ["it's", "a", "dog's", "life"])

    def test_counts(self):
        text = "One fish. Two fish! Red fish? Blue fish."
        self.assertEqual(textkit.word_count(text), 8)
        self.assertEqual(textkit.sentence_count(text), 4)

    def test_top_words_skips_stop_words(self):
        text = "the cat and the hat and the bat sat on the cat"
        self.assertEqual(textkit.top_words(text, 1), [("cat", 2)])


class TestClean(unittest.TestCase):
    def test_whitespace(self):
        self.assertEqual(textkit.normalise_whitespace("  a \n\t b  "), "a b")

    def test_punctuation(self):
        self.assertEqual(textkit.remove_punctuation("Hi, there!"), "Hi there")

    def test_slugify(self):
        self.assertEqual(textkit.slugify("Hello, Wörld! 2026"), "hello-world-2026")


class TestReadability(unittest.TestCase):
    def test_syllables(self):
        self.assertEqual(syllables("cat"), 1)
        self.assertEqual(syllables("python"), 2)
        self.assertEqual(syllables("table"), 2)
        self.assertEqual(syllables("make"), 1)

    def test_reading_time(self):
        self.assertEqual(textkit.reading_time_minutes(""), 0)
        self.assertEqual(textkit.reading_time_minutes("word " * 201), 2)

    def test_simple_text_is_easy(self):
        score = textkit.flesch_reading_ease("The cat sat. The dog ran. We had fun.")
        self.assertEqual(describe(score), "very easy")


class TestCLI(unittest.TestCase):
    def run_cli(self, *args):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = main(list(args))
        return code, buffer.getvalue()

    def test_report(self):
        code, out = self.run_cli("report", str(SAMPLE))
        self.assertEqual(code, 0)
        self.assertIn("Words:", out)

    def test_top(self):
        code, out = self.run_cli("top", str(SAMPLE), "-n", "1")
        self.assertTrue(out.startswith("python"))

    def test_missing_file(self):
        code, _ = self.run_cli("report", "nope.txt")
        self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
