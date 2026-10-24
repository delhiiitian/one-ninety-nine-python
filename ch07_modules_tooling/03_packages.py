"""7.3 Packages: folders of modules.

Real-world comparison: a kitchen. The kitchen (package) has a spice
rack, a fridge and a cupboard (modules). You say "get the salt from
the kitchen's spice rack": kitchen.recipes.make_tea.

    kitchen/
        __init__.py   <- makes the folder a package
        recipes.py
        units.py
"""

import kitchen
from kitchen.units import cups_to_ml
from kitchen import recipes

print(kitchen.make_tea(2))
print(recipes.make_tea(1, sugar=False))
print("3 cups is", cups_to_ml(3), "ml")
print("Package exports:", kitchen.__all__)
