"""2.1 if / else: making a decision.

Real-world comparison: a traffic light. IF the light is green, you
drive. ELSE you wait. The program picks one path, never both.
"""

light = "green"

if light == "green":
    print("Go!")
else:
    print("Wait.")

# The indented block belongs to the if. Indentation is not optional.
balance = 500
price = 750

if balance >= price:
    balance -= price
    print("Purchase done. Balance left:", balance)
else:
    shortfall = price - balance
    print(f"Not enough money. You need Rs {shortfall} more.")

# An if without else is fine when there is nothing to do otherwise.
items_in_cart = 3
if items_in_cart > 0:
    print(f"You have {items_in_cart} items in your cart.")

# One-line conditional expression (ternary).
age = 15
ticket = "child" if age < 18 else "adult"
print("Ticket type:", ticket)
