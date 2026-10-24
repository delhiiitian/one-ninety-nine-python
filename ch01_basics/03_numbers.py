"""1.3 Numbers: integers, floats and arithmetic.

Real-world comparison: Python is a calculator that never gets tired.
Whole numbers (int) count things, like people in a queue. Decimal
numbers (float) measure things, like litres of milk.
"""

people = 12          # int: whole number
milk_litres = 2.5    # float: number with a decimal point

print("Addition      7 + 3 =", 7 + 3)
print("Subtraction   7 - 3 =", 7 - 3)
print("Multiply      7 * 3 =", 7 * 3)
print("Divide        7 / 3 =", 7 / 3)     # always gives a float
print("Floor divide  7 // 3 =", 7 // 3)   # drops the decimal part
print("Remainder     7 % 3 =", 7 % 3)     # what is left over
print("Power         7 ** 3 =", 7 ** 3)

# Real use: share 50 sweets among 12 people.
sweets = 50
each = sweets // people
left_over = sweets % people
print(f"Each person gets {each} sweets, {left_over} are left over.")

# Floats can be slightly imprecise, so round() for display.
price = 19.99
tax = price * 0.18
print("Tax:", tax)
print("Tax rounded:", round(tax, 2))

# Big numbers are fine, and _ makes them easier to read.
world_population = 8_100_000_000
print("World population:", world_population)

# Useful built-ins.
print("abs(-5) =", abs(-5))
print("max(3, 9, 4) =", max(3, 9, 4))
print("min(3, 9, 4) =", min(3, 9, 4))
print("milk per person:", round(milk_litres / people, 3), "litres")
