"""1.2 Variables: giving names to values.

Real-world comparison: a variable is a labelled jar in a kitchen.
The label (name) stays the same, but you can empty the jar and put
something new inside at any time.
"""

# Create a variable with =. The name is on the left, the value on the right.
city = "Delhi"
population_millions = 33
print("City:", city)
print("Population (millions):", population_millions)

# Reassign: the label now points to a new value.
city = "Mumbai"
print("Now the city is:", city)

# A variable can be built from other variables.
apples = 5
oranges = 3
fruits = apples + oranges
print("Total fruits:", fruits)

# Assign several variables in one line.
x, y, z = 1, 2, 3
print("x, y, z =", x, y, z)

# Swap two values without a temporary jar.
x, y = y, x
print("After swap x, y =", x, y)

# Python figures out the type on its own. type() tells you what it is.
print(type(city), type(population_millions))

# Good names describe the content: snake_case, lowercase, no spaces.
monthly_rent = 25000
print("Monthly rent:", monthly_rent)
