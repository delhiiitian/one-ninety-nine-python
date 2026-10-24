"""8.9 Pythonic idioms: writing code the Python way.

Real-world comparison: speaking a language like a local. You can be
understood with textbook phrases, but locals use short, natural
expressions. These idioms are how experienced Python programmers talk.
"""

names = ["Asha", "Ben", "Chen"]
scores = [88, 72, 95]

# Unpacking with a star.
first, *middle, last = [1, 2, 3, 4, 5]
print("first:", first, "middle:", middle, "last:", last)

# zip two lists into a dictionary.
report = dict(zip(names, scores))
print("Report:", report)

# any() and all() instead of loops with flags.
print("Anyone above 90?", any(s > 90 for s in scores))
print("Everyone passed (>=40)?", all(s >= 40 for s in scores))

# Merge dictionaries with |.
defaults = {"theme": "light", "font": 12}
user_choice = {"theme": "dark"}
print("Settings:", defaults | user_choice)

# The walrus operator := assigns inside an expression.
data = [3, 8, 1, 9, 4]
if (n := len(data)) > 3:
    print(f"List is long ({n} items)")

# Conditional expression and 'or' for defaults.
nickname = ""
print("Hello,", nickname or "friend")

# f-string power.
price = 1234567.891
print(f"{price:,.2f} | {0.256:.1%} | {'left':<8}| {'right':>8}|")

# The Zen of Python, a poem about good code (first 5 lines).
import io
import contextlib
buffer = io.StringIO()
with contextlib.redirect_stdout(buffer):
    import this  # noqa: F401
print("\n".join(buffer.getvalue().splitlines()[2:7]))
