"""Bill Splitter: type what you ordered, get a receipt and each person's share.

Run:  python main.py
"""

from bill import build_bill, format_receipt


def ask_items():
    print("Enter each item as: name, price, quantity  (blank line to finish)")
    items = []
    while True:
        line = input("item> ").strip()
        if not line:
            break
        parts = [p.strip() for p in line.split(",")]
        if len(parts) != 3:
            print("  Please type three parts: name, price, quantity")
            continue
        name, price_text, qty_text = parts
        try:
            items.append((name, float(price_text), int(qty_text)))
        except ValueError:
            print("  Price must be a number and quantity a whole number")
    return items


def ask_int(prompt, default):
    text = input(f"{prompt} [{default}]: ").strip()
    return int(text) if text.isdigit() else default


def main():
    print("Welcome to the Bill Splitter\n")
    items = ask_items()
    if not items:
        print("Nothing ordered, nothing to pay!")
        return
    tip = ask_int("Tip percent", 10)
    people = max(1, ask_int("Number of people", 2))
    print()
    print(format_receipt(build_bill(items, tip, people)))


if __name__ == "__main__":
    main()
