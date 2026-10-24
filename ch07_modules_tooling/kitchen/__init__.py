"""The kitchen package: a folder of related modules.

Anything imported here can be used as kitchen.<name>.
"""

from .recipes import make_tea
from .units import cups_to_ml

__all__ = ["make_tea", "cups_to_ml"]
