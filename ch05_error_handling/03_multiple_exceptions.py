"""5.3 Handling several kinds of errors.

Real-world comparison: a hospital emergency room. A broken arm goes
to orthopaedics, a fever goes to general medicine. Each kind of
problem has its own handler.
"""


def price_per_item(total_text, count_text):
    try:
        total = float(total_text)
        count = int(count_text)
        return f"Rs {total / count:.2f} each"
    except ValueError:
        return "Please type numbers only"
    except ZeroDivisionError:
        return "Count cannot be zero"


print(price_per_item("300", "4"))
print(price_per_item("abc", "4"))
print(price_per_item("300", "0"))

# One handler for several types: put them in a tuple.
data = [1, 2, 3]
for index in [1, 10, "x"]:
    try:
        print("Value:", data[index])
    except (IndexError, TypeError) as error:
        print(f"Bad index {index!r}: {type(error).__name__}")

# Order matters: put specific errors before general ones.
# Exception is the parent of almost all errors, so it goes last.
try:
    open("does_not_exist.txt")
except FileNotFoundError:
    print("That file is not there")
except Exception as error:
    print("Something else went wrong:", error)
