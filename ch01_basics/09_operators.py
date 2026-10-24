"""1.9 Operators and precedence: the order Python does maths.

Real-world comparison: getting dressed has an order. Socks go on
before shoes. Python also has an order: brackets first, then powers,
then multiply/divide, then add/subtract (like BODMAS at school).
"""

print("2 + 3 * 4   =", 2 + 3 * 4)       # multiply first -> 14
print("(2 + 3) * 4 =", (2 + 3) * 4)     # brackets first -> 20
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)     # powers go right to left -> 512
print("-3 ** 2     =", -3 ** 2)         # power before minus -> -9

# Augmented assignment: update a variable in place.
score = 10
score += 5     # score = score + 5
score -= 2     # score = score - 2
score *= 3     # score = score * 3
score //= 2    # score = score // 2
print("Final score:", score)

# Logical operators: and, or, not.
has_ticket = True
has_id = False
print("Can board (ticket and id):", has_ticket and has_id)
print("Can enter lounge (ticket or id):", has_ticket or has_id)
print("Needs help (not has_id):", not has_id)

# Membership and identity.
fruits = ["apple", "mango"]
print("'mango' in fruits:", "mango" in fruits)
empty = None
print("empty is None:", empty is None)

# Real use: a restaurant bill.
food = 850
gst_rate = 5
tip_rate = 10
total = food + food * gst_rate / 100 + food * tip_rate / 100
print(f"Bill with GST and tip: Rs {total:.2f}")
