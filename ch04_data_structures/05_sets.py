"""4.5 Sets: unique items, no order.

Real-world comparison: the guest list at a party's door. Each person
is on it only once, and the bouncer only cares IF you are on it,
not in which position.
"""

guests = {"Asha", "Ben", "Chen"}
guests.add("Divya")
guests.add("Asha")         # already there, nothing happens
print("Guests:", sorted(guests))
print("Is Ben invited?", "Ben" in guests)

# Remove duplicates from a list in one step.
visits = ["home", "cart", "home", "pay", "cart", "home"]
unique_pages = set(visits)
print("Unique pages:", sorted(unique_pages))

# Set maths.
python_devs = {"Asha", "Ben", "Chen", "Eli"}
sql_devs = {"Ben", "Eli", "Farah"}
print("Know both:", sorted(python_devs & sql_devs))        # intersection
print("Know either:", sorted(python_devs | sql_devs))      # union
print("Only Python:", sorted(python_devs - sql_devs))      # difference
print("Know exactly one:", sorted(python_devs ^ sql_devs)) # symmetric difference

# Real use: which required documents are still missing?
required = {"passport", "photo", "address proof", "bank statement"}
submitted = {"photo", "passport"}
print("Still missing:", sorted(required - submitted))
