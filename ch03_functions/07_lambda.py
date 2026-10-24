"""3.7 Lambda functions: tiny one-line functions.

Real-world comparison: a sticky note with one instruction, like
"sort by price". You write it on the spot and throw it away after,
instead of writing a full manual.
"""

double = lambda x: x * 2      # same as: def double(x): return x * 2
print("double(21) =", double(21))

products = [
    ("laptop", 55000),
    ("mouse", 600),
    ("monitor", 12000),
    ("keyboard", 1500),
]

# Most common use: telling sorted() what to sort by.
by_price = sorted(products, key=lambda item: item[1])
print("Cheapest first:", by_price)

by_name_length = sorted(products, key=lambda item: len(item[0]))
print("Shortest name first:", by_name_length)

# With max(), min(), filter() and map().
most_expensive = max(products, key=lambda item: item[1])
print("Most expensive:", most_expensive)

prices = [p for _, p in products]
with_gst = list(map(lambda p: round(p * 1.18), prices))
print("With 18% GST:", with_gst)

affordable = list(filter(lambda item: item[1] < 2000, products))
print("Under Rs 2000:", affordable)
