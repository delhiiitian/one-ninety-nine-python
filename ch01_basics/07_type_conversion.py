"""1.7 Type conversion: changing one type into another.

Real-world comparison: converting currency at an airport. The value
is the same idea, but it has to be in the right form before the shop
will accept it. "42" (text) must become 42 (number) before you add.
"""

text_number = "42"
print("As text, '42' + '8' =", text_number + "8")          # joins text
print("As number, 42 + 8 =", int(text_number) + 8)         # real maths

# The main converters.
print("int('7')     ->", int("7"))
print("float('3.5') ->", float("3.5"))
print("str(99)      ->", str(99) + " balloons")
print("int(9.99)    ->", int(9.99), "(cuts off, does not round)")
print("round(9.99)  ->", round(9.99))
print("bool('yes')  ->", bool("yes"))
print("list('abc')  ->", list("abc"))

# Check a string before converting it.
for value in ["150", "12.5", "abc"]:
    if value.isdigit():
        print(value, "is a whole number:", int(value))
    else:
        try:
            print(value, "is a decimal:", float(value))
        except ValueError:
            print(value, "is not a number")

# Real use: a price comes from a web form as text.
form_price = "499.00"
quantity = "3"
total = float(form_price) * int(quantity)
print(f"Total: Rs {total:.2f}")
