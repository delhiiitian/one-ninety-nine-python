"""5.6 Custom exceptions: errors with your own names.

Real-world comparison: airline status codes. Instead of saying "a
problem", the airline says "flight overbooked" or "gate changed".
Named errors tell the caller exactly what happened.
"""


class BookingError(Exception):
    """Base class for all booking problems."""


class FlightFullError(BookingError):
    def __init__(self, flight):
        super().__init__(f"flight {flight} is full")
        self.flight = flight


class InvalidSeatError(BookingError):
    pass


flights = {"AI101": {"seats": 2, "booked": ["Asha", "Ben"]},
           "6E202": {"seats": 3, "booked": []}}


def book(flight, passenger):
    info = flights.get(flight)
    if info is None:
        raise InvalidSeatError(f"no such flight {flight}")
    if len(info["booked"]) >= info["seats"]:
        raise FlightFullError(flight)
    info["booked"].append(passenger)
    return f"{passenger} booked on {flight}"


for flight, person in [("6E202", "Chen"), ("AI101", "Divya"), ("XX999", "Eli")]:
    try:
        print(book(flight, person))
    except FlightFullError as error:
        print("Sorry:", error, "-> offering the next flight")
    except BookingError as error:
        print("Booking problem:", error)
