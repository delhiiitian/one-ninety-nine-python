"""Counting things in text."""

import re
from collections import Counter

STOP_WORDS = frozenset(
    "a an and are as at be but by for from has have he her his i in is it its "
    "of on or she that the their them they this to was we were will with you".split()
)

_WORD = re.compile(r"[A-Za-z']+")
_SENTENCE_END = re.compile(r"[.!?]+")


def words(text: str) -> list[str]:
    """All words in lower case, without punctuation."""
    return [w.strip("'").lower() for w in _WORD.findall(text) if w.strip("'")]


def word_count(text: str) -> int:
    return len(words(text))


def sentence_count(text: str) -> int:
    parts = [p for p in _SENTENCE_END.split(text) if p.strip()]
    return len(parts)


def top_words(text: str, n: int = 5, skip_stop_words: bool = True) -> list[tuple[str, int]]:
    chosen = [w for w in words(text) if not (skip_stop_words and w in STOP_WORDS)]
    return Counter(chosen).most_common(n)
