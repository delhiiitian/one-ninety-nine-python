"""6.3 The with statement: automatic clean-up.

Real-world comparison: a hotel key card. When you check out, the room
is locked and cleaned for you automatically, even if you leave in a
hurry. 'with' closes the file for you, even if an error happens.
"""

from pathlib import Path

path = Path(__file__).parent / "data" / "notes.txt"

# Without 'with', you must remember to close, and an error can skip it.
file = open(path, encoding="utf-8")
try:
    first = file.readline().strip()
finally:
    file.close()
print("First note:", first, "| closed:", file.closed)

# With 'with', closing is guaranteed.
with open(path, encoding="utf-8") as file:
    second_file_lines = file.read().splitlines()
    print("Inside with, closed:", file.closed)
print("After with, closed:", file.closed)
print("Notes:", second_file_lines)

# Even when an error happens, the file still gets closed.
try:
    with open(path, encoding="utf-8") as file:
        raise RuntimeError("something broke mid-read")
except RuntimeError as error:
    print("Error:", error, "| still closed:", file.closed)

# You can open two files in one with: copy notes into upper case.
out_dir = Path(__file__).parent / "output"
out_dir.mkdir(exist_ok=True)
with open(path, encoding="utf-8") as src, \
        open(out_dir / "NOTES.txt", "w", encoding="utf-8") as dst:
    for line in src:
        dst.write(line.upper())
print((out_dir / "NOTES.txt").read_text(encoding="utf-8"))
