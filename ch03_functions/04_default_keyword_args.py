"""3.4 Default and keyword arguments.

Real-world comparison: ordering a pizza. If you do not say the size,
you get medium (the default). You can still ask for large by name.
"""


def order_pizza(topping, size="medium", extra_cheese=False):
    cheese = " with extra cheese" if extra_cheese else ""
    return f"A {size} {topping} pizza{cheese}"


print(order_pizza("veggie"))
print(order_pizza("paneer", "large"))
print(order_pizza("margherita", extra_cheese=True))
print(order_pizza(topping="corn", size="small", extra_cheese=True))


# Defaults make simple calls short and still allow full control.
def send_message(text, to="everyone", urgent=False):
    flag = "[URGENT] " if urgent else ""
    return f"To {to}: {flag}{text}"


print(send_message("Lunch is ready"))
print(send_message("Server down", to="ops team", urgent=True))


# Common trap: never use a list as a default. Use None instead.
def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


print(add_item("apple"))
print(add_item("bread"))   # a fresh basket each time
