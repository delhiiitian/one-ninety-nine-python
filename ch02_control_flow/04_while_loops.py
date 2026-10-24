"""2.4 while loops: repeat while something is true.

Real-world comparison: stirring soup WHILE it is not yet boiling.
You do not know how many stirs it takes; you keep checking.
"""

temperature = 20
stirs = 0
while temperature < 100:
    temperature += 15
    stirs += 1
print(f"Boiling after {stirs} stirs (temperature {temperature})")

# Countdown.
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print("Lift off!")

# Real use: how many years until savings double at 7% interest?
savings = 10000
target = savings * 2
years = 0
while savings < target:
    savings *= 1.07
    years += 1
print(f"Money doubles in {years} years (Rs {savings:,.0f})")

# Warning: if the condition never becomes False the loop runs forever.
# Always make sure something inside the loop moves you toward the end.
