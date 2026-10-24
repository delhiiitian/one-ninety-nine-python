"""8.2 Inheritance: building on an existing class.

Real-world comparison: a family recipe passed down. The child keeps
the parent's recipe and adds a personal twist. A subclass gets every
method of its parent class and can change or add some.
"""


class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def describe(self):
        return f"{self.brand} with {self.wheels} wheels"

    def fare(self, km):
        return km * 10


class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand, wheels=2)    # reuse the parent's setup

    def fare(self, km):                      # override: cheaper per km
        return km * 6


class Cab(Vehicle):
    def __init__(self, brand, seats):
        super().__init__(brand, wheels=4)
        self.seats = seats                   # something new

    def fare(self, km):
        return 50 + super().fare(km)         # base fare + parent's rate


rides = [Bike("Hero"), Cab("Maruti", seats=4), Vehicle("Generic", 3)]
for ride in rides:
    print(f"{ride.describe():25} 8 km costs Rs {ride.fare(8)}")

print("Is a Cab a Vehicle?", isinstance(rides[1], Vehicle))
print("Is a Bike a Cab?", isinstance(rides[0], Cab))
