"""Unit Converter: length, weight, volume and temperature from a menu.

Run:          python main.py
One-liner:    python main.py length 5 km mile
"""

import sys

from conversions import convert, format_result, units_for

MENU = ["length", "weight", "volume", "temperature"]


def pick_category(ask):
    for number, name in enumerate(MENU, start=1):
        print(f"  {number}. {name}")
    print("  0. quit")
    choice = ask("Choose: ").strip()
    if choice == "0":
        return None
    if choice.isdigit() and 1 <= int(choice) <= len(MENU):
        return MENU[int(choice) - 1]
    print("  Not a menu option.")
    return pick_category(ask)


def ask_conversion(category, ask):
    units = units_for(category)
    print(f"Units: {', '.join(units)}")
    from_unit = ask("From unit: ").strip().lower()
    to_unit = ask("To unit: ").strip().lower()
    try:
        value = float(ask("Value: "))
        result = convert(category, value, from_unit, to_unit)
    except ValueError:
        return "  That value is not a number."
    except KeyError as error:
        return f"  {error.args[0]}"
    return "  " + format_result(value, from_unit, result, to_unit)


def interactive(ask=input):
    print("=== Unit Converter ===")
    while True:
        category = pick_category(ask)
        if category is None:
            print("Bye!")
            return
        print(ask_conversion(category, ask))
        print()


def one_shot(args):
    category, value, from_unit, to_unit = args
    result = convert(category, float(value), from_unit, to_unit)
    print(format_result(float(value), from_unit, result, to_unit))


if __name__ == "__main__":
    if len(sys.argv) == 5:
        one_shot(sys.argv[1:])
    else:
        interactive()
