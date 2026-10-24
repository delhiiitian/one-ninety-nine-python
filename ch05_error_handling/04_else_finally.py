"""5.4 else and finally: what runs after success, and always.

Real-world comparison: a restaurant. If the meal goes well (else) you
leave a tip. Whatever happens (finally) the table gets cleaned.
"""


def checkout(cart_total, card_balance):
    print(f"\nPaying Rs {cart_total} with balance Rs {card_balance}")
    try:
        if cart_total > card_balance:
            raise ValueError("insufficient balance")
        card_balance -= cart_total
    except ValueError as error:
        print("Payment failed:", error)
    else:
        print("Payment succeeded. New balance:", card_balance)
    finally:
        print("Receipt printed and session closed.")


checkout(500, 1200)
checkout(1500, 1200)

# finally is perfect for cleanup, like closing a connection.
connection_open = False
try:
    connection_open = True
    print("\nConnected to the database")
    result = 10 / 0          # something goes wrong
except ZeroDivisionError:
    print("Query failed")
finally:
    connection_open = False
    print("Connection closed:", not connection_open)
