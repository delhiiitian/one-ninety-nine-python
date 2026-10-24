"""5.7 Validating user input: ask again until it is right.

Real-world comparison: a petrol pump keypad. If you type an amount it
cannot accept, it beeps and asks again. It never pumps fuel for
nonsense input.
"""


def ask_number(prompt, low, high, answers):
    """Keep asking until we get a whole number between low and high.

    'answers' stands in for a person typing, so the example runs on its
    own. In a real program you would use input(prompt) instead.
    """
    for text in answers:
        print(prompt + text)
        try:
            value = int(text)
        except ValueError:
            print("  Please type a whole number.")
            continue
        if not low <= value <= high:
            print(f"  Please choose between {low} and {high}.")
            continue
        return value
    raise ValueError("no valid answer given")


litres = ask_number("Litres (1-60): ", 1, 60, ["ten", "0", "75", "25"])
print("Pumping", litres, "litres")


# Validating a whole form and collecting every problem at once.
def validate_signup(form):
    problems = []
    if len(form.get("username", "")) < 3:
        problems.append("username must be at least 3 characters")
    if "@" not in form.get("email", ""):
        problems.append("email must contain @")
    if not form.get("age", "").isdigit():
        problems.append("age must be a number")
    return problems


print(validate_signup({"username": "al", "email": "al.example.com", "age": "x"}))
print(validate_signup({"username": "alice", "email": "a@b.com", "age": "30"}))
