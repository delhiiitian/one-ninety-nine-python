"""Every way an ATM visit can go wrong, as its own exception type."""


class ATMError(Exception):
    """Base class: catch this to handle any ATM problem."""


class CardNotFoundError(ATMError):
    pass


class CardBlockedError(ATMError):
    pass


class WrongPINError(ATMError):
    def __init__(self, attempts_left):
        super().__init__(f"wrong PIN, {attempts_left} attempt(s) left")
        self.attempts_left = attempts_left


class InsufficientFundsError(ATMError):
    def __init__(self, balance, amount):
        super().__init__(f"cannot withdraw Rs {amount}, balance is Rs {balance}")
        self.balance = balance
        self.amount = amount


class DailyLimitError(ATMError):
    pass


class InvalidAmountError(ATMError):
    pass


class ATMOutOfCashError(ATMError):
    pass
