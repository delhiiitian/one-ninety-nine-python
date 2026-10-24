"""1.6 Input and output: talking to the user.

Real-world comparison: input() is a shop assistant asking "what would
you like?", and print() is the assistant answering. The answer you
type always comes back as text (a string).
"""

name = input("What is your name? ")
city = input("Which city do you live in? ")

# input() returns a string. Convert it when you need a number.
cups_text = input("How many cups of tea do you drink a day? ")
cups = int(cups_text) if cups_text.strip().isdigit() else 0

print()
print(f"Nice to meet you, {name}!")
print(f"{city} is a lovely place.")

# f-string formatting: width, alignment and decimal places.
yearly = cups * 365
print(f"That is {yearly} cups a year.")
print(f"{'Item':<10}{'Count':>8}")
print(f"{'Tea':<10}{cups:>8}")
print(f"Cost per year at Rs 12.5 a cup: Rs {yearly * 12.5:,.2f}")
