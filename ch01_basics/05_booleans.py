"""1.5 Booleans and comparisons: True or False.

Real-world comparison: a boolean is a light switch. It is either on
(True) or off (False). Comparisons are questions with a yes/no
answer, like "is the shop open?".
"""

is_open = True
is_raining = False
print("Shop open?", is_open)
print("Raining?", is_raining)

# Comparison operators give back a boolean.
age = 20
print("age == 20 :", age == 20)
print("age != 18 :", age != 18)
print("age > 18  :", age > 18)
print("age < 18  :", age < 18)
print("age >= 20 :", age >= 20)
print("age <= 19 :", age <= 19)

# Strings can be compared too (alphabetical order, case matters).
print("'apple' < 'banana':", "apple" < "banana")
print("'Apple' == 'apple':", "Apple" == "apple")

# Chained comparisons read like maths.
temperature = 24
print("Pleasant weather?", 18 <= temperature <= 28)

# Truthiness: empty things act like False, everything else like True.
print("bool(0)  =", bool(0))
print("bool(42) =", bool(42))
print("bool('') =", bool(""))
print("bool('hi') =", bool("hi"))

# Real use: can this person vote?
can_vote = age >= 18
print("Can vote:", can_vote)
