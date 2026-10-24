"""5.8 Assertions: checking your own assumptions.

Real-world comparison: a pilot's pre-flight checklist. "Fuel full?
Doors closed?" If a check fails, you stop right away, before the
problem gets bigger. assert is a checklist item for the programmer.
"""


def apply_discount(price, percent):
    assert 0 <= percent <= 100, f"discount {percent}% makes no sense"
    new_price = price * (100 - percent) / 100
    assert new_price <= price, "a discount should never raise the price"
    return new_price


print("20% off 500:", apply_discount(500, 20))

try:
    apply_discount(500, 150)
except AssertionError as error:
    print("Assertion failed:", error)

# Assertions are for catching BUGS during development.
# They can be switched off with 'python -O', so never use them to
# check user input. Use if + raise for that (see 5.5).

# Tiny self-tests with assert.
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


assert celsius_to_fahrenheit(0) == 32
assert celsius_to_fahrenheit(100) == 212
assert celsius_to_fahrenheit(-40) == -40
print("All temperature checks passed")
