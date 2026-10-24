"""8.7 Decorators: wrapping a function with extra behaviour.

Real-world comparison: gift wrapping. The present inside does not
change, but the wrapping adds something around it. A decorator wraps
a function to add timing, logging or checks, without editing it.
"""

import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        took = (time.perf_counter() - start) * 1000
        print(f"[timer] {func.__name__} took {took:.2f} ms")
        return result
    return wrapper


def require_login(func):
    @functools.wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("logged_in"):
            return "Access denied: please log in"
        return func(user, *args, **kwargs)
    return wrapper


@timer
def slow_sum(n):
    return sum(range(n))


@require_login
def view_orders(user):
    return f"Showing orders for {user['name']}"


print("Sum:", slow_sum(1_000_000))
print(view_orders({"name": "Asha", "logged_in": True}))
print(view_orders({"name": "Guest", "logged_in": False}))


# Built-in decorator: cache results so repeat calls are instant.
@functools.lru_cache(maxsize=None)
def ways_to_climb(steps):
    if steps <= 1:
        return 1
    return ways_to_climb(steps - 1) + ways_to_climb(steps - 2)


print("Ways to climb 50 stairs:", ways_to_climb(50))
