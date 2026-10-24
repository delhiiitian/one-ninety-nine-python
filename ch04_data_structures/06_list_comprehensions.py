"""4.6 List comprehensions: build a list in one line.

Real-world comparison: a factory line. Items come in on a belt, a
machine changes each one, a filter throws out the bad ones, and a
new box of finished items comes out.
    [machine(item) for item in belt if item_is_good]
"""

prices = [100, 250, 80, 400, 60]

# The long way.
with_tax = []
for p in prices:
    with_tax.append(p * 1.18)

# The comprehension way: same result, one line.
with_tax = [round(p * 1.18, 2) for p in prices]
print("With tax:", with_tax)

# With a filter.
cheap = [p for p in prices if p < 100]
print("Under 100:", cheap)

# Transform text.
names = ["  asha ", "BEN", "chen  "]
clean = [n.strip().title() for n in names]
print("Clean names:", clean)

# Dictionary and set comprehensions.
squares = {n: n * n for n in range(1, 6)}
print("Squares:", squares)
first_letters = {n[0] for n in clean}
print("First letters:", sorted(first_letters))

# Real use: pull the emails of active users from records.
users = [
    {"email": "a@shop.com", "active": True},
    {"email": "b@shop.com", "active": False},
    {"email": "c@shop.com", "active": True},
]
active_emails = [u["email"] for u in users if u["active"]]
print("Send newsletter to:", active_emails)
