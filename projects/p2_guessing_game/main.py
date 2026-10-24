"""Number Guessing Game: the computer picks a number, you find it.

Run:  python main.py
"""

from game import LEVELS, hint, new_secret, parse_guess, score


def choose_level(ask):
    while True:
        choice = ask("Choose a level (easy/medium/hard): ").strip().lower()
        if choice in LEVELS:
            return choice
        print("  Please type easy, medium or hard.")


def play_round(level, secret, ask):
    top = LEVELS[level]["top"]
    allowed = LEVELS[level]["attempts"]
    print(f"I am thinking of a number from 1 to {top}. You have {allowed} tries.")
    attempts = 0
    while attempts < allowed:
        guess = parse_guess(ask(f"Guess #{attempts + 1}: "), top)
        if guess is None:
            print(f"  Type a whole number from 1 to {top}.")
            continue                       # a typo does not cost a try
        attempts += 1
        result, clue = hint(guess, secret)
        if result == "correct":
            points = score(level, attempts)
            print(f"  Correct! Found in {attempts} tries. +{points} points")
            return points
        print(f"  Go {result} ({clue}). {allowed - attempts} tries left.")
    print(f"  Out of tries! The number was {secret}.")
    return 0


def main(ask=input, secret_picker=new_secret):
    print("=== Number Guessing Game ===")
    total = 0
    rounds = 0
    while True:
        level = choose_level(ask)
        total += play_round(level, secret_picker(level), ask)
        rounds += 1
        print(f"Score: {total} after {rounds} round(s)\n")
        again = ask("Play again? (y/n): ").strip().lower()
        if again != "y":
            break
    print(f"Thanks for playing! Final score: {total}")
    return total


if __name__ == "__main__":
    main()
