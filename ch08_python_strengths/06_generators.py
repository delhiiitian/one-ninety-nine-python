"""8.6 Generators: making values on demand.

Real-world comparison: a tap versus a water tank. A list fills a whole
tank first. A generator is a tap: water (values) flows only when you
open it, so you can handle endless streams without filling memory.
"""

import sys


def countdown(n):
    while n > 0:
        yield n          # hand out one value, then pause here
        n -= 1


for number in countdown(3):
    print("Generated:", number)


def fibonacci():
    a, b = 0, 1
    while True:          # endless, but only computes what you ask for
        yield a
        a, b = b, a + b


fib = fibonacci()
print("First 10 Fibonacci numbers:", [next(fib) for _ in range(10)])

# Generator expressions: like list comprehensions with ( ).
squares_list = [n * n for n in range(1_000_000)]
squares_gen = (n * n for n in range(1_000_000))
print("List size in memory:", sys.getsizeof(squares_list), "bytes")
print("Generator size in memory:", sys.getsizeof(squares_gen), "bytes")
print("Sum from generator:", sum(squares_gen))


# Real use: read a huge log one line at a time and keep only errors.
def error_lines(lines):
    for line in lines:
        if "ERROR" in line:
            yield line.strip()


fake_log = ["INFO start\n", "ERROR disk full\n", "INFO ok\n", "ERROR timeout\n"]
for line in error_lines(fake_log):
    print("Found:", line)
