"""3.1 Defining functions: name a job once, reuse it many times.

Real-world comparison: a coffee machine. Someone built it once. Now
anyone presses one button and gets coffee, without knowing what
happens inside.
"""


def make_coffee():
    print("Grinding beans...")
    print("Heating water...")
    print("Coffee is ready!")


# Defining a function does nothing on its own. You must call it.
make_coffee()
print("---")
make_coffee()


def print_receipt_header():
    print("=" * 24)
    print("   CORNER CAFE RECEIPT")
    print("=" * 24)


# Real use: the same header on every receipt, written once.
for order_number in range(1, 3):
    print_receipt_header()
    print(f"Order #{order_number}")
    print()
