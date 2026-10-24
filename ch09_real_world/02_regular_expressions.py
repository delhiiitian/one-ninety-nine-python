"""9.2 Regular expressions: search patterns for text.

Real-world comparison: a metal detector on a beach. You do not look
for one exact coin; you describe the KIND of thing you want and the
detector beeps on every match. A regex describes the shape of text,
like "10 digits" or "something@something.com".
"""

import re

text = """Contact Asha at asha@example.com or 98765 43210.
Ben: ben.k@shop.in, phone 91234-56789. Order IDs: ORD-1042, ORD-77."""

emails = re.findall(r"[\w.]+@[\w.]+\.\w+", text)
print("Emails:", emails)

phones = re.findall(r"\b\d{5}[ -]?\d{5}\b", text)
print("Phones:", phones)

orders = re.findall(r"ORD-(\d+)", text)
print("Order numbers:", orders)

# search() finds the first match; groups pull out pieces.
match = re.search(r"(\w+)@([\w.]+)", text)
print("User:", match.group(1), "| Domain:", match.group(2))

# sub() replaces matches: hide phone numbers.
print(re.sub(r"\d{5}([ -]?)\d{5}", "XXXXX\\1XXXXX", text))

# fullmatch() checks an entire string, perfect for validation.
def valid_pin_code(pin):
    return re.fullmatch(r"[1-9]\d{5}", pin) is not None


for pin in ["110001", "012345", "4000"]:
    print(pin, "valid PIN?", valid_pin_code(pin))

# Cheat sheet: \d digit, \w letter/digit/_, \s space, . any char,
# + one or more, * zero or more, ? optional, {n} exactly n, [abc] one of.
