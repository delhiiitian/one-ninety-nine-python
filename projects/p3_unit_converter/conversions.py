"""Pure conversion functions, grouped by category.

Every ratio unit is stored as "how many base units is one of these",
so any unit converts to any other unit in the same category with one
formula: value * from_factor / to_factor.
"""

LENGTH = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
          "inch": 0.0254, "foot": 0.3048, "yard": 0.9144, "mile": 1609.344}

WEIGHT = {"g": 0.001, "kg": 1.0, "tonne": 1000.0,
          "ounce": 0.028349523125, "pound": 0.45359237}

VOLUME = {"ml": 0.001, "l": 1.0, "cup": 0.24, "gallon": 3.785411784}

CATEGORIES = {"length": LENGTH, "weight": WEIGHT, "volume": VOLUME}


def convert_ratio(value: float, from_unit: str, to_unit: str, table: dict) -> float:
    """Convert between two units of the same ratio-based category."""
    if from_unit not in table or to_unit not in table:
        raise KeyError(f"unknown unit: {from_unit!r} or {to_unit!r}")
    return value * table[from_unit] / table[to_unit]


def to_celsius(value: float, unit: str) -> float:
    if unit == "c":
        return value
    if unit == "f":
        return (value - 32) * 5 / 9
    if unit == "k":
        return value - 273.15
    raise KeyError(f"unknown temperature unit: {unit!r}")


def from_celsius(value: float, unit: str) -> float:
    if unit == "c":
        return value
    if unit == "f":
        return value * 9 / 5 + 32
    if unit == "k":
        return value + 273.15
    raise KeyError(f"unknown temperature unit: {unit!r}")


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Temperatures need offsets, not just ratios, so go through Celsius."""
    return from_celsius(to_celsius(value, from_unit), to_unit)


def convert(category: str, value: float, from_unit: str, to_unit: str) -> float:
    """One entry point for every category."""
    if category == "temperature":
        return convert_temperature(value, from_unit.lower(), to_unit.lower())
    table = CATEGORIES.get(category)
    if table is None:
        raise KeyError(f"unknown category: {category!r}")
    return convert_ratio(value, from_unit.lower(), to_unit.lower(), table)


def units_for(category: str) -> list[str]:
    if category == "temperature":
        return ["c", "f", "k"]
    return list(CATEGORIES[category])


def format_result(value: float, from_unit: str, result: float, to_unit: str) -> str:
    return f"{value:g} {from_unit} = {round(result, 4):g} {to_unit}"
