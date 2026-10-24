"""2.8 Nested loops: a loop inside a loop.

Real-world comparison: a clock. The minute hand goes all the way round
(inner loop) for every single step of the hour hand (outer loop).
"""

for hour in range(1, 3):
    for minute in (0, 15, 30, 45):
        print(f"{hour}:{minute:02}", end="  ")
    print()

# A small multiplication grid.
for row in range(1, 6):
    for col in range(1, 6):
        print(f"{row * col:4}", end="")
    print()

# Drawing a triangle of stars.
for size in range(1, 6):
    print("*" * size)

# Real use: find every pair of items that fits a budget.
menu = {"tea": 20, "samosa": 15, "sandwich": 60, "juice": 40}
budget = 60
for first, price1 in menu.items():
    for second, price2 in menu.items():
        if first < second and price1 + price2 <= budget:
            print(f"{first} + {second} = Rs {price1 + price2}")
