"""3.9 Docstrings and type hints: labelling your functions.

Real-world comparison: the label on a medicine bottle. It says what it
is for, how much to take, and what you get. A docstring and type
hints do the same for a function.
"""


def bmi(weight_kg: float, height_m: float) -> float:
    """Return the body mass index, rounded to one decimal place.

    Args:
        weight_kg: weight in kilograms.
        height_m: height in metres.

    Returns:
        The BMI value.
    """
    return round(weight_kg / height_m ** 2, 1)


print("BMI:", bmi(70, 1.75))

# The docstring is stored with the function.
print(bmi.__doc__.splitlines()[0])

# Type hints are notes for humans and tools. Python does not enforce
# them at run time, but editors and checkers like mypy use them.
print("Hints:", bmi.__annotations__)


def initials(full_name: str, with_dots: bool = True) -> str:
    """Turn 'Grace Brewster Hopper' into 'G.B.H.'."""
    letters = [part[0].upper() for part in full_name.split()]
    joiner = "." if with_dots else ""
    return joiner.join(letters) + joiner


print(initials("Grace Brewster Hopper"))
print(initials("alan turing", with_dots=False))


def average(scores: list[int]) -> float | None:
    """Return the mean score, or None if there are no scores."""
    if not scores:
        return None
    return sum(scores) / len(scores)


print("Average:", average([80, 90, 70]))
print("Average of nothing:", average([]))
