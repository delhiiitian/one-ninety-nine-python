"""1.8 Comments and code style: writing code humans can read.

Real-world comparison: comments are sticky notes on a recipe.
The cook (Python) ignores them, but the next person reading the
recipe is very glad they are there.
"""

# A single-line comment starts with a hash.

# BAD: names that say nothing.
a = 1200
b = 0.05
c = a * b

# GOOD: names that explain themselves, so fewer comments are needed.
monthly_salary = 1200
savings_rate = 0.05
monthly_savings = monthly_salary * savings_rate

print("Unclear version:", c)
print("Clear version:", monthly_savings)


def yearly_savings(salary, rate):
    """Return how much is saved in a year.

    A docstring (this triple-quoted text) explains what a function does.
    Tools and editors show it as help.
    """
    return salary * rate * 12


print("Yearly savings:", yearly_savings(monthly_salary, savings_rate))
help(yearly_savings)

# PEP 8, the Python style guide, in five rules:
# 1. Indent with 4 spaces.
# 2. Use snake_case for variables and functions.
# 3. Use UPPER_CASE for constants.
# 4. Put spaces around operators: x = y + 1
# 5. Keep lines shorter than about 79-99 characters.
MAX_LOGIN_ATTEMPTS = 3
print("Max login attempts:", MAX_LOGIN_ATTEMPTS)
