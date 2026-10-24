from .units import cups_to_ml


def make_tea(cups=1, sugar=True):
    water = cups_to_ml(cups)
    sweet = "with sugar" if sugar else "no sugar"
    return f"Boil {water} ml water, add tea leaves, {sweet}."
