"""5.1 Reading error messages (tracebacks).

Real-world comparison: a car's dashboard warning light. It tells you
WHAT is wrong (low oil) and WHERE to look. A traceback tells you the
error type, the message, and the exact line that failed.
"""

import traceback


def average(values):
    return sum(values) / len(values)


def report(values):
    return f"Average is {average(values)}"


# We call report() with an empty list on purpose, catch the crash,
# and print the traceback so you can practise reading it.
try:
    report([])
except ZeroDivisionError:
    print("A traceback, read from the BOTTOM up:\n")
    traceback.print_exc()

print("""
How to read it:
  1. Last line: the error type and message -> ZeroDivisionError: division by zero
  2. The line just above: the exact code that failed -> sum(values) / len(values)
  3. Further up: the chain of calls that led there -> report() called average()
""")

# The errors beginners meet most often:
common = {
    "SyntaxError": "Python cannot read the code (missing colon, bracket).",
    "IndentationError": "Spaces at the start of a line are wrong.",
    "NameError": "A name is used before it exists, or is misspelled.",
    "TypeError": "Wrong type, e.g. 'age' + 5.",
    "ValueError": "Right type, bad value, e.g. int('abc').",
    "IndexError": "List position does not exist.",
    "KeyError": "Dictionary key does not exist.",
    "ZeroDivisionError": "Dividing by zero.",
    "FileNotFoundError": "The file path is wrong.",
}
for name, meaning in common.items():
    print(f"{name:18} {meaning}")
