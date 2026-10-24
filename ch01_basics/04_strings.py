"""1.4 Strings: working with text.

Real-world comparison: a string is a necklace of beads, where each
bead is a character. You can count the beads, pick one out by its
position, or cut a piece of the necklace.
"""

name = "Ada Lovelace"

# Length and indexing (positions start at 0).
print("Length:", len(name))
print("First letter:", name[0])
print("Last letter:", name[-1])

# Slicing: [start:stop] takes a piece (stop is not included).
print("First name:", name[0:3])
print("Last name:", name[4:])

# Joining strings with + and repeating with *.
greeting = "Hello, " + name + "!"
print(greeting)
print("-" * 20)

# Common methods return a NEW string; the original never changes.
print(name.upper())
print(name.lower())
print(name.replace("Ada", "Augusta Ada"))
print("  padded  ".strip())
print("ada lovelace".title())

# Searching inside a string.
print("Is 'Love' in the name?", "Love" in name)
print("Position of 'L':", name.find("L"))

# split() breaks a string into a list of words; join() glues them back.
words = "tea,coffee,juice".split(",")
print(words)
print(" | ".join(words))

# f-strings put values straight into text.
age = 36
print(f"{name} was {age} years old in 1852.")

# Real use: clean up an email typed by a user.
raw_email = "  Ada.Lovelace@Example.COM "
clean_email = raw_email.strip().lower()
print("Clean email:", clean_email)
