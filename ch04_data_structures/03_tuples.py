"""4.3 Tuples: an ordered collection that cannot change.

Real-world comparison: the date printed on your birth certificate.
It is fixed. A tuple holds values that belong together and should
never be edited, like (latitude, longitude).
"""

taj_mahal = (27.1751, 78.0421)
print("Taj Mahal is at:", taj_mahal)
print("Latitude:", taj_mahal[0])

# Unpacking puts each value into its own variable.
lat, lon = taj_mahal
print(f"lat={lat}, lon={lon}")

# Tuples cannot be changed.
try:
    taj_mahal[0] = 0
except TypeError as error:
    print("Cannot change a tuple:", error)

# A one-item tuple needs a trailing comma.
single = ("only",)
print(type(single), len(single))

# Functions often return tuples.
def divide(a, b):
    return a // b, a % b

quotient, remainder = divide(17, 5)
print("17 / 5 =", quotient, "remainder", remainder)

# Tuples can be dictionary keys because they never change.
distances = {("Delhi", "Agra"): 233, ("Mumbai", "Pune"): 148}
print("Delhi to Agra:", distances[("Delhi", "Agra")], "km")

# Real use: a list of RGB colours.
colours = [("red", (255, 0, 0)), ("green", (0, 128, 0)), ("navy", (0, 0, 128))]
for name, (r, g, b) in colours:
    print(f"{name:6} -> #{r:02x}{g:02x}{b:02x}")
