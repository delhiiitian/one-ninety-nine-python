"""6.2 Writing files.

Real-world comparison: a notebook. Mode "w" tears out all the old
pages and starts fresh. Mode "a" (append) keeps what is there and
writes on the next empty line.
"""

from datetime import date
from pathlib import Path

out_dir = Path(__file__).parent / "output"
out_dir.mkdir(exist_ok=True)
diary = out_dir / "diary.txt"

# "w" creates the file, or wipes it if it already exists.
with open(diary, "w", encoding="utf-8") as file:
    file.write("My diary\n")
    file.write("========\n")

# "a" adds to the end.
with open(diary, "a", encoding="utf-8") as file:
    file.write(f"{date(2026, 10, 24)}: learned to write files\n")
    file.write(f"{date(2026, 10, 25)}: wrote a CSV report\n")

# writelines() writes a list of strings.
todo = ["- practise loops\n", "- read chapter 7\n"]
with open(diary, "a", encoding="utf-8") as file:
    file.writelines(todo)

# print() can write to a file too.
with open(diary, "a", encoding="utf-8") as file:
    print("Total entries:", 2, file=file)

print(diary.read_text(encoding="utf-8"))

# Real use: save a simple receipt.
items = [("Tea", 2, 20), ("Samosa", 3, 15)]
receipt = out_dir / "receipt.txt"
with open(receipt, "w", encoding="utf-8") as file:
    for name, qty, price in items:
        file.write(f"{name:10}{qty:>3} x {price:>4} = {qty * price:>5}\n")
    file.write(f"{'TOTAL':>21}{sum(q * p for _, q, p in items):>6}\n")
print(receipt.read_text(encoding="utf-8"))
