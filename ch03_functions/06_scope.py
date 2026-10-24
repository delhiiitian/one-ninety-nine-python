"""3.6 Scope: where a variable can be seen.

Real-world comparison: rooms in a house. Something you put down in
the kitchen (a local variable) stays in the kitchen. Things in the
hallway (global variables) can be seen from every room.
"""

house_name = "Rose Villa"      # global: visible everywhere


def kitchen():
    spoon = "silver spoon"     # local: only inside kitchen()
    print("In the kitchen I see:", spoon, "and", house_name)


kitchen()
# print(spoon)  # would fail: NameError, spoon only lives in the kitchen

# A local name can hide a global one with the same name.
colour = "blue"


def paint():
    colour = "red"             # a new local variable
    print("Inside paint():", colour)


paint()
print("Outside paint():", colour)

# Changing a global needs the global keyword (use it rarely).
visitors = 0


def welcome():
    global visitors
    visitors += 1


for _ in range(3):
    welcome()
print("Visitors today:", visitors)


# Better style: pass values in and return results out.
def add_visitor(count):
    return count + 1


count = add_visitor(add_visitor(0))
print("Counted the clean way:", count)
