"""6.6 JSON files: data that programs share.

Real-world comparison: a standard shipping box. Any courier in any
country knows how to carry it. JSON is the box every language and
website understands, and it maps almost one-to-one onto Python
dictionaries and lists.
"""

import json
from pathlib import Path

here = Path(__file__).parent

# Read JSON from a file into Python objects.
with open(here / "data" / "settings.json", encoding="utf-8") as file:
    settings = json.load(file)

print("App:", settings["app_name"])
print("Opens at:", settings["open_hours"]["start"])
print("Pays with:", ", ".join(settings["payment_methods"]))

# Change it and save it back with nice indentation.
settings["tax_percent"] = 12
settings["payment_methods"].append("wallet")
out = here / "output"
out.mkdir(exist_ok=True)
with open(out / "settings_updated.json", "w", encoding="utf-8") as file:
    json.dump(settings, file, indent=2)
print("Saved updated settings")

# Strings to and from JSON (what web APIs send and receive).
order = {"id": 101, "items": ["tea", "samosa"], "paid": True, "note": None}
text = json.dumps(order)
print("As JSON text:", text)        # True -> true, None -> null
back = json.loads(text)
print("Back to Python:", back, type(back))
