"""8.5 Iterators: one item at a time.

Real-world comparison: a ticket dispenser at a bank. Each pull gives
you the next number. You cannot go back, and the machine only prints
a ticket when someone asks for one.
"""

# Anything you can loop over is iterable. iter() gives the dispenser,
# next() pulls one ticket.
queue = ["A1", "A2", "A3"]
dispenser = iter(queue)
print(next(dispenser))
print(next(dispenser))
print(next(dispenser))
try:
    next(dispenser)
except StopIteration:
    print("No more tickets")


# Your own iterator: a class with __iter__ and __next__.
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


print("Countdown:", list(Countdown(5)))

# Handy built-in iterator tools.
names = ["Asha", "Ben", "Chen"]
scores = [88, 72, 95]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

for position, name in enumerate(names, start=1):
    print(position, name)

for name in reversed(names):
    print("Reverse:", name)
