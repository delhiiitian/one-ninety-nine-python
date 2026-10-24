"""Game rules for the number guessing game. No input() or print() here."""

import random

LEVELS = {
    "easy": {"top": 20, "attempts": 8},
    "medium": {"top": 50, "attempts": 7},
    "hard": {"top": 100, "attempts": 6},
}


def new_secret(level, rng=random):
    return rng.randint(1, LEVELS[level]["top"])


def hint(guess, secret):
    """Return 'correct', 'higher' or 'lower', plus a warm/cold clue."""
    if guess == secret:
        return "correct", ""
    direction = "higher" if guess < secret else "lower"
    gap = abs(guess - secret)
    if gap <= 3:
        clue = "very hot"
    elif gap <= 10:
        clue = "warm"
    else:
        clue = "cold"
    return direction, clue


def score(level, attempts_used):
    """More points for harder levels and fewer attempts."""
    allowed = LEVELS[level]["attempts"]
    multiplier = {"easy": 1, "medium": 2, "hard": 3}[level]
    return (allowed - attempts_used + 1) * 10 * multiplier


def parse_guess(text, top):
    """Return an int guess, or None when the text is not a valid guess."""
    text = text.strip()
    if not text.isdigit():
        return None
    value = int(text)
    if not 1 <= value <= top:
        return None
    return value
