"""8.8 Writing your own context managers.

Real-world comparison: borrowing a meeting room. You book it, use it,
and the system frees it when you leave, even if the meeting ends in
chaos. You can build your own 'with' blocks that set up and tidy up.
"""

import time
from contextlib import contextmanager


class MeetingRoom:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Booked {self.name}")
        return self

    def __exit__(self, exc_type, exc, tb):
        print(f"Released {self.name}")
        return False          # False: let errors carry on upwards


with MeetingRoom("Room 4B") as room:
    print("Meeting in", room.name)

try:
    with MeetingRoom("Room 2A"):
        raise RuntimeError("fire alarm!")
except RuntimeError as error:
    print("Meeting ended early:", error)


# The short way: a generator with @contextmanager.
@contextmanager
def stopwatch(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {(time.perf_counter() - start) * 1000:.1f} ms")


with stopwatch("Building a big list"):
    numbers = [n * 2 for n in range(200_000)]
print("Built", len(numbers), "numbers")
