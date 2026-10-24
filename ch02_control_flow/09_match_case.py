"""2.9 match / case: picking a branch by pattern (Python 3.10+).

Real-world comparison: a phone menu. "Press 1 for balance, 2 for
recharge, 0 for an operator." Each key goes to exactly one branch.
"""


def phone_menu(key):
    match key:
        case "1":
            return "Your balance is Rs 240"
        case "2":
            return "Recharge options: 99, 199, 299"
        case "0":
            return "Connecting you to an operator"
        case "8" | "9":
            return "Those keys are reserved"
        case _:
            return "Invalid choice, please try again"


for key in ["1", "2", "0", "9", "7"]:
    print(f"Pressed {key}: {phone_menu(key)}")


# match can also look inside data.
def describe(command):
    match command.split():
        case ["go", direction]:
            return f"Walking {direction}"
        case ["pick", "up", item]:
            return f"Picked up the {item}"
        case ["quit"]:
            return "Goodbye"
        case _:
            return "I do not understand"


for cmd in ["go north", "pick up lamp", "quit", "dance"]:
    print(f"{cmd!r:16} -> {describe(cmd)}")
