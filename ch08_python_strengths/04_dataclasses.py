"""8.4 Dataclasses: classes for holding data, with less typing.

Real-world comparison: a printed form with labelled boxes. You only
say which boxes exist (name, price, quantity); the form takes care of
the layout. @dataclass writes __init__, __repr__ and __eq__ for you.
"""

from dataclasses import dataclass, field, asdict


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    def total_value(self):
        return self.price * self.quantity


@dataclass(frozen=True)              # frozen: cannot be changed later
class Point:
    x: float
    y: float


@dataclass
class Cart:
    owner: str
    items: list[Product] = field(default_factory=list)

    def add(self, product):
        self.items.append(product)

    def total(self):
        return sum(p.total_value() for p in self.items)


pen = Product("pen", 10, 5)
print(pen)                                  # a free, readable repr
print("Value of stock:", pen.total_value())
print("Equal?", pen == Product("pen", 10, 5))

cart = Cart("Asha")
cart.add(pen)
cart.add(Product("notebook", 45, 2))
print(f"{cart.owner}'s cart total: Rs {cart.total()}")
print("As a dictionary:", asdict(cart))

home = Point(1, 2)
try:
    home.x = 5
except Exception as error:
    print("Frozen:", type(error).__name__)
