"""3.2 Parameters and arguments: giving a function its inputs.

Real-world comparison: ordering at a juice bar. The menu says
"juice of your choice, size of your choice" (parameters). You say
"mango, large" (arguments).
"""


def make_juice(fruit, size):
    print(f"Making a {size} {fruit} juice")


make_juice("mango", "large")       # positional: order matters
make_juice("orange", "small")
make_juice(size="medium", fruit="apple")   # keyword: order does not matter


def greet(name):
    print(f"Hello, {name}! Welcome aboard.")


for passenger in ["Ravi", "Sara", "Tom"]:
    greet(passenger)


# Real use: one function, many shipping labels.
def shipping_label(name, street, city, pin):
    print(name.upper())
    print(street)
    print(f"{city} - {pin}")
    print()


shipping_label("Meera Shah", "12 MG Road", "Pune", "411001")
shipping_label("John Doe", "5 Park Street", "Kolkata", "700016")
