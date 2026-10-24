"""4.8 Sorting: putting things in order.

Real-world comparison: arranging books on a shelf. You can sort by
title, by author, or by height. sorted() makes a new neat shelf;
.sort() rearranges the shelf you already have.
"""

numbers = [42, 7, 19, 3, 88]
print("sorted():", sorted(numbers))
print("original unchanged:", numbers)
numbers.sort(reverse=True)
print("after .sort(reverse=True):", numbers)

words = ["banana", "Apple", "cherry"]
print("Default (capitals first):", sorted(words))
print("Ignore case:", sorted(words, key=str.lower))
print("By length:", sorted(words, key=len))

books = [
    {"title": "Dune", "author": "Herbert", "year": 1965, "rating": 4.3},
    {"title": "Emma", "author": "Austen", "year": 1815, "rating": 4.0},
    {"title": "It", "author": "King", "year": 1986, "rating": 4.3},
]

by_year = sorted(books, key=lambda b: b["year"])
print("Oldest first:", [b["title"] for b in by_year])

# Sort by rating (high first), then title (A-Z) to break ties.
ranked = sorted(books, key=lambda b: (-b["rating"], b["title"]))
for b in ranked:
    print(f"{b['rating']}  {b['title']}")

# Real use: a leaderboard showing the top 3.
scores = {"asha": 320, "ben": 150, "chen": 480, "divya": 290, "eli": 410}
top3 = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)[:3]
for place, (player, score) in enumerate(top3, start=1):
    print(f"#{place} {player:6} {score}")
