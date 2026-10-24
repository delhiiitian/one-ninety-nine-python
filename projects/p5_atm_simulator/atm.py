"""The ATM machine and the bank accounts behind it."""

import logging

from errors import (ATMOutOfCashError, CardBlockedError, CardNotFoundError, DailyLimitError,
                    InsufficientFundsError, InvalidAmountError, WrongPINError)

log = logging.getLogger("atm")

MAX_PIN_ATTEMPTS = 3
DAILY_LIMIT = 20000
NOTES = (500, 200, 100)


class Account:
    def __init__(self, card, pin, owner, balance):
        self.card = card
        self.pin = pin
        self.owner = owner
        self.balance = balance
        self.failed_pins = 0
        self.blocked = False
        self.withdrawn_today = 0
        self.history = []


class ATM:
    def __init__(self, accounts, cash=50000):
        self.accounts = {a.card: a for a in accounts}
        self.cash = cash

    # --- session ---------------------------------------------------------
    def login(self, card, pin):
        account = self.accounts.get(card)
        if account is None:
            log.warning("unknown card %s", card)
            raise CardNotFoundError(f"card {card} is not recognised")
        if account.blocked:
            raise CardBlockedError("card is blocked, please visit your branch")
        if pin != account.pin:
            account.failed_pins += 1
            left = MAX_PIN_ATTEMPTS - account.failed_pins
            log.warning("wrong PIN for card %s (%d left)", card, left)
            if left <= 0:
                account.blocked = True
                log.error("card %s blocked", card)
                raise CardBlockedError("too many wrong PINs, card blocked")
            raise WrongPINError(left)
        account.failed_pins = 0
        log.info("card %s logged in", card)
        return account

    # --- money -------------------------------------------------------------
    @staticmethod
    def _check_amount(amount):
        if not isinstance(amount, int) or amount <= 0:
            raise InvalidAmountError("amount must be a positive whole number")
        if amount % NOTES[-1] != 0:
            raise InvalidAmountError(f"amount must be a multiple of {NOTES[-1]}")

    @staticmethod
    def dispense_notes(amount):
        """Fewest notes possible, e.g. 1800 -> {500: 3, 200: 1, 100: 1}."""
        notes = {}
        for note in NOTES:
            count, amount = divmod(amount, note)
            if count:
                notes[note] = count
        return notes

    def withdraw(self, account, amount):
        self._check_amount(amount)
        if amount > account.balance:
            raise InsufficientFundsError(account.balance, amount)
        if account.withdrawn_today + amount > DAILY_LIMIT:
            left = DAILY_LIMIT - account.withdrawn_today
            raise DailyLimitError(f"daily limit reached, you can take Rs {left} more today")
        if amount > self.cash:
            raise ATMOutOfCashError("this ATM does not have enough cash")
        notes = self.dispense_notes(amount)
        account.balance -= amount
        account.withdrawn_today += amount
        self.cash -= amount
        account.history.append(("withdraw", amount))
        log.info("card %s withdrew %d", account.card, amount)
        return notes

    def deposit(self, account, amount):
        self._check_amount(amount)
        account.balance += amount
        self.cash += amount
        account.history.append(("deposit", amount))
        log.info("card %s deposited %d", account.card, amount)
        return account.balance

    def mini_statement(self, account, last=5):
        lines = [f"{kind:<9} Rs {amount:>7,}" for kind, amount in account.history[-last:]]
        lines.append(f"{'balance':<9} Rs {account.balance:>7,}")
        return "\n".join(lines)
