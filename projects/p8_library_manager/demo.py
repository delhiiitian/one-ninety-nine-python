"""Library Manager demo: a day at the Python Public Library.

Run:  python demo.py
"""

from datetime import date, timedelta

from library import Book, EBook, Item, Library, LibraryError, Member

lib = Library("Python Public Library")
lib.add(
    Book("B1", "The Pragmatic Programmer", 1999, copies=2, author="Hunt & Thomas", pages=352),
    Book("B2", "Clean Code", 2008, author="Robert Martin", pages=464),
    EBook("E1", "Automate the Boring Stuff", 2015, author="Al Sweigart", size_mb=12.5),
    Item("M1", "World Atlas (map)", 2024),
)
asha = lib.join(Member("U1", "Asha"))
ben = lib.join(Member("U2", "Ben", max_loans=1))

print(f"Welcome to {lib.name}: {len(lib)} items\n")
for item in lib:                      # __iter__ gives items sorted by title
    print(" ", item)

day1 = date(2026, 10, 1)
print("\nAsha borrows B2, due", lib.borrow("U1", "B2", today=day1))
print("Asha borrows E1, due", lib.borrow("U1", "E1", today=day1))

for attempt in [("U2", "B2"), ("U2", "B1"), ("U2", "E1")]:
    try:
        print(f"Ben borrows {attempt[1]}, due", lib.borrow(*attempt, today=day1))
    except LibraryError as error:
        print("Refused:", error)

late_day = day1 + timedelta(days=20)
print("\nOverdue on", late_day)
for name, title, days in lib.overdue(late_day):
    print(f"  {name} is {days} days late with {title}")

fee = lib.give_back("U1", "B2", today=late_day)
print(f"Asha returns Clean Code, fee Rs {fee}")

with lib.reading_room("U1", "M1") as atlas:
    print("Reading in the room:", atlas.title, "| left on shelf:", atlas.available)
print("After the reading room:", lib["M1"].available, "on the shelf")

print("\nSearch 'code':", [i.title for i in lib.search("code")])
print("Stats:", lib.stats())
print("Activity log:")
for line in lib.activity:
    print("  ", line)
