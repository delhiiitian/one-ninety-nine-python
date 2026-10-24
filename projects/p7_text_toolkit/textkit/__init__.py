"""textkit: a small, installable toolkit for analysing plain text.

    >>> import textkit
    >>> textkit.word_count("Hello there, world")
    3
"""

from .clean import normalise_whitespace, remove_punctuation, slugify
from .readability import reading_time_minutes, flesch_reading_ease
from .stats import sentence_count, top_words, word_count, words

__version__ = "1.0.0"

__all__ = [
    "words", "word_count", "sentence_count", "top_words",
    "normalise_whitespace", "remove_punctuation", "slugify",
    "reading_time_minutes", "flesch_reading_ease",
]
