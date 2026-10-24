"""4.2 Slicing: taking a piece of a sequence.

Real-world comparison: cutting slices from a loaf of bread. You say
where to start, where to stop, and how thick the gap is between
slices: loaf[start:stop:step].
"""

week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Weekdays:", week[0:5])
print("Weekend:", week[5:])
print("First three:", week[:3])
print("Last two:", week[-2:])
print("Every other day:", week[::2])
print("Reversed:", week[::-1])

# Slicing makes a copy, so the original is safe.
copy = week[:]
copy[0] = "Monday"
print("Original still starts with:", week[0])

# Slices work on strings too.
order_id = "ORD-2026-10-24-0042"
print("Year:", order_id[4:8])
print("Sequence number:", order_id[-4:])

# You can replace a slice of a list.
scores = [10, 20, 30, 40, 50]
scores[1:3] = [99, 98]
print("Scores:", scores)

# Real use: paginate search results, 3 per page.
results = [f"result {n}" for n in range(1, 9)]
page_size = 3
for page in range(0, len(results), page_size):
    print(f"Page {page // page_size + 1}:", results[page:page + page_size])
