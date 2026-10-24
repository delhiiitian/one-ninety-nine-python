"""7.1 Importing modules: borrowing ready-made tools.

Real-world comparison: a public library. You do not write every book
yourself; you borrow the one you need. 'import' borrows code that
someone already wrote and tested.
"""

import math                       # borrow the whole module
from random import choice, seed   # borrow just two tools
import datetime as dt             # borrow it under a shorter name

print("Square root of 144:", math.sqrt(144))
print("Pi to 4 places:", round(math.pi, 4))
print("Round up 4.1:", math.ceil(4.1))

seed(7)                           # makes the random pick repeatable
print("Lunch today:", choice(["dosa", "pasta", "salad", "biryani"]))

print("A fixed date:", dt.date(2026, 10, 24).strftime("%A, %d %B %Y"))

# See what is inside a module.
print("Some names in math:", [n for n in dir(math) if not n.startswith("_")][:8])

# Real use: distance between two cities with the haversine formula.
def distance_km(lat1, lon1, lat2, lon2):
    r = 6371
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


print(f"Delhi to Mumbai: {distance_km(28.61, 77.21, 19.08, 72.88):.0f} km")
