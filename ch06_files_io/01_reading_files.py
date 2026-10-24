"""6.1 Reading files.

Real-world comparison: reading a book. You open it, read (all at once
or one line at a time), then close it. A file on disk is a book that
your program can open.
"""

from pathlib import Path

notes_path = Path(__file__).parent / "data" / "notes.txt"

# Read the whole file into one string.
file = open(notes_path, encoding="utf-8")
everything = file.read()
file.close()
print("Whole file:\n" + everything)

# Read it as a list of lines.
with open(notes_path, encoding="utf-8") as file:
    lines = file.readlines()
print("Number of lines:", len(lines))
print("First line (raw):", repr(lines[0]))      # note the \n at the end

# Best for big files: loop line by line, memory stays small.
with open(notes_path, encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number}. {line.strip()}")

# Real use: search a file for a word.
with open(notes_path, encoding="utf-8") as file:
    matches = [line.strip() for line in file if "bill" in line.lower()]
print("Lines mentioning 'bill':", matches)
