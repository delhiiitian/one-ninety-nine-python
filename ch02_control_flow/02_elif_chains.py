"""2.2 elif: choosing between many options.

Real-world comparison: a lift (elevator) panel. You press exactly one
floor out of many. Python checks each elif from the top and stops at
the first one that is True.
"""


def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"


for marks in [95, 82, 64, 45, 12]:
    print(f"{marks} marks -> grade {grade(marks)}")

# Order matters. If the checks were reversed, 95 would match ">= 40"
# first and wrongly get a D.

# Real use: electricity bill slabs.
units = 260
if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = 100 * 3 + (units - 100) * 5
else:
    bill = 100 * 3 + 100 * 5 + (units - 200) * 8
print(f"{units} units -> Rs {bill}")
