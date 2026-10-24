"""7.2 Creating your own module.

Real-world comparison: a family recipe card. You write it once, keep
it in a drawer, and anyone in the house can use it. Any .py file is
a module that other files can import.

This file imports greetings.py, which sits in the same folder.
"""

import greetings
from greetings import greet

print(greetings.greet("Asha"))
print(greet("Ben", language="hi"))
print(greet("Carla", "es"))
print("Supported:", greetings.languages())
print("Default language:", greetings.DEFAULT_LANGUAGE)

# Where did Python find it?
print("Loaded from:", greetings.__file__.split("/")[-1])

# A leading underscore (_WORDS) means "private, please do not use".
# Python will not stop you, but it is a polite sign.
