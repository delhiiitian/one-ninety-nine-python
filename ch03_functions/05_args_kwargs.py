"""3.5 *args and **kwargs: any number of arguments.

Real-world comparison: a shopping bag. You do not know in advance how
many items a customer will put in it, so the bag stretches to fit
(*args). A form with optional fields works like **kwargs: each extra
answer comes with a label.
"""


def total(*prices):
    # prices arrives as a tuple
    return sum(prices)


print("Total of 3 items:", total(10, 20, 30))
print("Total of 5 items:", total(5, 5, 5, 5, 5))


def profile(name, **details):
    # details arrives as a dictionary
    print(f"Profile: {name}")
    for key, value in details.items():
        print(f"  {key}: {value}")


profile("Asha", city="Chennai", job="designer")
profile("Ben", age=31)

# Unpacking: * spreads a list, ** spreads a dictionary.
numbers = [4, 8, 15]
print("Unpacked total:", total(*numbers))
options = {"city": "Goa", "hobby": "surfing"}
profile("Chen", **options)


# Real use: a logger that accepts any message parts and settings.
def log(*parts, level="INFO", **context):
    message = " ".join(str(p) for p in parts)
    extras = " ".join(f"{k}={v}" for k, v in context.items())
    print(f"[{level}] {message} {extras}".strip())


log("User", "signed", "in", user_id=42, ip="10.0.0.1")
log("Disk almost full", level="WARN", percent=93)
