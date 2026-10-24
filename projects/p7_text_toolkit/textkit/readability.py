"""How easy is a text to read?"""

import math
import re

from .stats import sentence_count, words

WORDS_PER_MINUTE = 200


def reading_time_minutes(text: str, wpm: int = WORDS_PER_MINUTE) -> int:
    """Rounded up, and at least 1 minute for any non-empty text."""
    count = len(words(text))
    return math.ceil(count / wpm) if count else 0


def syllables(word: str) -> int:
    """A rough count: groups of vowels, minus a silent final 'e'."""
    word = word.lower()
    groups = re.findall(r"[aeiouy]+", word)
    count = len(groups)
    if word.endswith("e") and count > 1 and not word.endswith("le"):
        count -= 1
    return max(count, 1)


def flesch_reading_ease(text: str) -> float:
    """Higher is easier. 60-70 is plain English; under 30 is very hard."""
    all_words = words(text)
    sentences = sentence_count(text)
    if not all_words or not sentences:
        return 0.0
    total_syllables = sum(syllables(w) for w in all_words)
    score = (206.835 - 1.015 * (len(all_words) / sentences)
             - 84.6 * (total_syllables / len(all_words)))
    return round(score, 1)


def describe(score: float) -> str:
    if score >= 80:
        return "very easy"
    if score >= 60:
        return "plain English"
    if score >= 30:
        return "fairly difficult"
    return "very difficult"
