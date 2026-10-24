"""7.9 Debugging: finding out why code misbehaves.

Real-world comparison: a detective at a crime scene. You gather clues
(print and logging), freeze time to look closely (breakpoint), and
test one theory at a time until you find the culprit.
"""

import os

# Clue 1: print the values you are unsure about.
def average_price(prices):
    total = sum(prices)
    count = len(prices) - 1            # BUG on purpose
    print(f"[debug] total={total} count={count}")
    return total / count


print("Buggy average:", average_price([100, 200, 300]))
# The debug line shows count=2, but there are 3 prices. Found it!


def average_price_fixed(prices):
    return sum(prices) / len(prices)


print("Fixed average:", average_price_fixed([100, 200, 300]))

# Clue 2: f"{name=}" prints the name and the value together.
discount = 0.15
print(f"{discount=}")

# Clue 3: breakpoint() freezes the program and opens the pdb debugger.
# Commands there: n (next line), s (step in), p x (print x), c (continue), q (quit).
# We only pause when you ask for it, so this file runs straight through:
#   DEBUG=1 python 09_debugging.py
if os.environ.get("DEBUG") == "1":
    breakpoint()

# Clue 4: rubber-duck debugging. Explain the code line by line to a
# rubber duck (or a friend). Saying it out loud often reveals the bug.
print("Done")
