"""2.5 for loops: repeat for each item.

Real-world comparison: a teacher taking attendance. She goes through
the register one name at a time, from the first to the last.
"""

students = ["Asha", "Ben", "Chen", "Divya"]
for student in students:
    print("Present:", student)

# Looping over the letters of a string.
for letter in "Python":
    print(letter, end=" ")
print()

# enumerate() gives a position number with each item.
for number, student in enumerate(students, start=1):
    print(f"{number}. {student}")

# Adding up as you go (an accumulator).
prices = [120, 45, 300, 80]
total = 0
for price in prices:
    total += price
print("Basket total:", total)

# Real use: find the most expensive item.
most_expensive = prices[0]
for price in prices:
    if price > most_expensive:
        most_expensive = price
print("Most expensive item:", most_expensive)
