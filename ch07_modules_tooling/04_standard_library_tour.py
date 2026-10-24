"""7.4 A tour of the standard library ("batteries included").

Real-world comparison: a Swiss Army knife. Python comes with a blade,
scissors, a screwdriver and more, already in your pocket. No download
needed.
"""

import collections
import datetime
import os
import platform
import random
import statistics
import string
import textwrap
import uuid

print("Python version:", platform.python_version())
print("Operating system:", platform.system())
print("Folder separator:", repr(os.sep))

marks = [72, 88, 95, 64, 88, 79]
print("Mean:", statistics.mean(marks), "| Median:", statistics.median(marks),
      "| Mode:", statistics.mode(marks))

rng = random.Random(42)
print("Dice roll:", rng.randint(1, 6))
print("Random password:", "".join(rng.choices(string.ascii_letters + string.digits, k=10)))

print("Unique id:", len(str(uuid.uuid4())), "characters long")

deadline = datetime.date(2026, 12, 31)
print("Days from 24 Oct 2026 to year end:", (deadline - datetime.date(2026, 10, 24)).days)

print("Most common letter in 'banana':", collections.Counter("banana").most_common(1))

long_text = ("Python's standard library covers files, dates, maths, internet "
             "protocols, compression, testing and much more.")
print(textwrap.fill(long_text, width=40))
