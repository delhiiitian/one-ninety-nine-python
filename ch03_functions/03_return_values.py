"""3.3 Return values: getting an answer back.

Real-world comparison: an ATM. You put in a request and it RETURNS
cash to you. print() only shows something on a screen; return hands
the value back so you can use it.
"""


def area_of_room(length, width):
    return length * width


bedroom = area_of_room(4, 3.5)
kitchen = area_of_room(3, 2.5)
print("Total area:", bedroom + kitchen, "square metres")


# A function can return more than one value (as a tuple).
def min_max(numbers):
    return min(numbers), max(numbers)


low, high = min_max([34, 12, 89, 7, 56])
print("Lowest:", low, "Highest:", high)


# return also ends the function immediately.
def is_even(n):
    if n % 2 == 0:
        return True
    return False


print("Is 10 even?", is_even(10))


# A function with no return gives back None.
def say_hi():
    print("hi")


result = say_hi()
print("say_hi returned:", result)


# Real use: final price after a discount.
def final_price(price, discount_percent):
    discount = price * discount_percent / 100
    return round(price - discount, 2)


print("Shoes after 20% off:", final_price(2499, 20))
