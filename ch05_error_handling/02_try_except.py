"""5.2 try / except: catching errors.

Real-world comparison: a safety net under a trapeze artist. The act
goes on as normal (try). If they fall, the net catches them (except)
and the show continues instead of ending in disaster.
"""

# Without try, a bad value would crash the whole program.
for text in ["25", "twenty", "40"]:
    try:
        age = int(text)
        print(f"{text!r} -> age {age}")
    except ValueError:
        print(f"{text!r} -> not a valid number, skipping")

# Catch the error object to see its message.
try:
    prices = {"tea": 20}
    print(prices["coffee"])
except KeyError as error:
    print("Missing item:", error)


# Real use: a safe division function for a spreadsheet-like tool.
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))

# Avoid a bare 'except:' that catches everything. It hides real bugs.
