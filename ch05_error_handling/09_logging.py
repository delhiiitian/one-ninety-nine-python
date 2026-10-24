"""5.9 Logging: a diary for your program.

Real-world comparison: a ship's logbook. The crew writes down what
happens and when, so if something goes wrong later, anyone can read
back and see what led up to it. print() is shouting; logging is a
proper record with a time and a level.
"""

import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S",
    stream=sys.stdout,
)
log = logging.getLogger("shop")

log.debug("Detailed info for developers")
log.info("Shop opened")
log.warning("Only 2 units of tea left")
log.error("Payment gateway did not respond")
log.critical("Database is down!")


def process_order(order_id, quantity):
    log.info("Processing order %s", order_id)
    try:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        log.info("Order %s done (%d items)", order_id, quantity)
    except ValueError:
        # exception() logs the message AND the traceback.
        log.exception("Order %s failed", order_id)


process_order("A-1", 3)
process_order("A-2", 0)

# Change the level to hide the noise in production.
log.setLevel(logging.WARNING)
log.info("You will not see this line")
log.warning("But you will see this one")
