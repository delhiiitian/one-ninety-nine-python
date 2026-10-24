"""ATM Simulator: log in with a card and PIN, then withdraw, deposit or check balance.

Run:  python main.py
Demo cards:  1111 (PIN 1234, Asha)   2222 (PIN 4321, Ben)
Every action is also written to atm.log.
"""

import logging
from pathlib import Path

from atm import ATM, Account
from errors import ATMError, WrongPINError

logging.basicConfig(filename=Path(__file__).with_name("atm.log"), level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")


def ask_amount(ask, prompt):
    text = ask(prompt).strip()
    try:
        return int(text)
    except ValueError:
        return text           # let the ATM reject it with a clear message


def session(atm, ask):
    card = ask("Insert card (card number): ").strip()
    while True:
        try:
            account = atm.login(card, ask("PIN: ").strip())
            break
        except WrongPINError as error:
            print(" ", error)
        except ATMError as error:          # unknown or blocked card
            print(" ", error)
            return
    print(f"Welcome, {account.owner}!")
    while True:
        choice = ask("\n1 Balance  2 Withdraw  3 Deposit  4 Statement  0 Exit: ").strip()
        try:
            if choice == "1":
                print(f"  Balance: Rs {account.balance:,}")
            elif choice == "2":
                notes = atm.withdraw(account, ask_amount(ask, "  Amount: "))
                print("  Take your cash:", ", ".join(f"{n} x Rs {v}" for v, n in notes.items()))
            elif choice == "3":
                print(f"  New balance: Rs {atm.deposit(account, ask_amount(ask, '  Amount: ')):,}")
            elif choice == "4":
                print(atm.mini_statement(account))
            elif choice == "0":
                print("  Please take your card. Goodbye!")
                return
            else:
                print("  Unknown option")
        except ATMError as error:
            print("  Sorry:", error)


def main(ask=input):
    atm = ATM([Account("1111", "1234", "Asha", 15000), Account("2222", "4321", "Ben", 3000)])
    session(atm, ask)
    return atm


if __name__ == "__main__":
    main()
