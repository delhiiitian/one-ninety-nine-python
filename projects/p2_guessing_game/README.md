# Project 2: Number Guessing Game

Chapter 2 project of **Python in 199 Pages**. The computer picks a secret number;
you guess it with "higher / lower" and "hot / cold" hints, three difficulty levels,
limited tries and a running score.

## Layout

```
p2_guessing_game/
├── game.py        # the rules: levels, hints, scoring, checking a guess
├── main.py        # the game loop: rounds, tries, play again
└── tests/
    └── test_game.py
```

## Run it

```bash
python main.py
```

## Test it

```bash
python -m unittest discover -s tests -t . -v
```

The test plays a whole game by passing a fake `ask` function instead of `input`,
and a fixed secret number instead of a random one.

## Ideas to extend

- Keep a high-score table in a file (Chapter 6).
- Add a "computer guesses your number" mode using binary search.
