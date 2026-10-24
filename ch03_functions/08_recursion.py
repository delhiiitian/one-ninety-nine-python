"""3.8 Recursion: a function that calls itself.

Real-world comparison: Russian nesting dolls. To reach the smallest
doll you open one doll, and inside is a smaller version of the same
problem. You stop when a doll does not open (the base case).
"""


def open_doll(size):
    if size == 0:                    # base case: stop here
        print("Found the smallest doll!")
        return
    print(f"Opening doll of size {size}")
    open_doll(size - 1)              # same problem, smaller


open_doll(3)


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print("5! =", factorial(5))


# Real use: walking a folder tree, which is nested like the dolls.
folders = {
    "Documents": {
        "Taxes": {"2025.pdf": None, "2026.pdf": None},
        "CV.docx": None,
    },
    "Photos": {"Goa": {"beach.jpg": None}},
}


def count_files(tree):
    total = 0
    for name, content in tree.items():
        if content is None:          # a file
            total += 1
        else:                        # a folder: look inside
            total += count_files(content)
    return total


print("Files in the tree:", count_files(folders))
