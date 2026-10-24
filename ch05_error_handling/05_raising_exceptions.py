"""5.5 Raising exceptions: signalling a problem yourself.

Real-world comparison: a referee blowing the whistle. The game cannot
continue under these conditions, so the referee stops play on purpose
and says why.
"""


def set_age(age):
    if not isinstance(age, int):
        raise TypeError("age must be a whole number")
    if age < 0 or age > 150:
        raise ValueError(f"age {age} is not realistic")
    return age


for value in [30, -5, "ten", 200]:
    try:
        print("Age set to", set_age(value))
    except (TypeError, ValueError) as error:
        print(f"Rejected {value!r}: {error}")


# Real use: a bank withdrawal that refuses bad requests.
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    if amount > balance:
        raise ValueError(f"cannot withdraw {amount}, balance is {balance}")
    return balance - amount


balance = 1000
for amount in [200, 5000, -10]:
    try:
        balance = withdraw(balance, amount)
        print("Withdrew", amount, "-> balance", balance)
    except ValueError as error:
        print("Withdrawal refused:", error)

# Re-raise: log the problem, then pass it on.
try:
    try:
        int("oops")
    except ValueError:
        print("Logging the problem, then passing it on...")
        raise
except ValueError as error:
    print("Caught again at the top:", error)
