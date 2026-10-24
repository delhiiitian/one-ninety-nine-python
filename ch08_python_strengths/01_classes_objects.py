"""8.1 Classes and objects: your own data types.

Real-world comparison: a cookie cutter and cookies. The class is the
cutter (the design). Each object is one cookie made from it. Every
cookie has the same shape, but each can have its own icing.
"""


class BankAccount:
    bank_name = "Python Bank"            # shared by every account

    def __init__(self, owner, balance=0):
        self.owner = owner               # each account has its own
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
        return self.balance

    def statement(self):
        return f"{self.owner}: Rs {self.balance} at {self.bank_name}"


asha = BankAccount("Asha", 1000)        # create objects (instances)
ben = BankAccount("Ben")

asha.deposit(500)
ben.deposit(200)
asha.withdraw(300)

print(asha.statement())
print(ben.statement())
print("Same class?", type(asha) is type(ben))
print("Same object?", asha is ben)

try:
    ben.withdraw(1000)
except ValueError as error:
    print("Ben's withdrawal failed:", error)
