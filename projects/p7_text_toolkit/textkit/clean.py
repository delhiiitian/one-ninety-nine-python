"""Cleaning text before analysing it."""

import re
import string
import unicodedata

_PUNCTUATION = str.maketrans("", "", string.punctuation)


def normalise_whitespace(text: str) -> str:
    """Collapse runs of spaces, tabs and newlines into single spaces."""
    return " ".join(text.split())


def remove_punctuation(text: str) -> str:
    return text.translate(_PUNCTUATION)


def slugify(text: str) -> str:
    """'Hello, Wörld! 2026' -> 'hello-world-2026' (handy for URLs and file names)."""
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")
