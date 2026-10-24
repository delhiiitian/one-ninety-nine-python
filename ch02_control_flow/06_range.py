"""2.6 range(): counting numbers for loops.

Real-world comparison: the numbered seats in a row at a stadium.
range() gives you the seat numbers without you writing them all out.
"""

print("range(5):", list(range(5)))              # 0 to 4
print("range(1, 6):", list(range(1, 6)))        # 1 to 5
print("range(0, 20, 5):", list(range(0, 20, 5)))  # step of 5
print("range(10, 0, -2):", list(range(10, 0, -2)))  # counting down

# Times table.
n = 7
for i in range(1, 11):
    print(f"{n} x {i:2} = {n * i}")

# Repeat something a fixed number of times.
for _ in range(3):
    print("Hip hip hooray!")

# Real use: EMI schedule for a 6-month loan with no interest.
loan = 30000
months = 6
for month in range(1, months + 1):
    remaining = loan - (loan // months) * month
    print(f"Month {month}: paid {loan // months}, remaining {remaining}")
