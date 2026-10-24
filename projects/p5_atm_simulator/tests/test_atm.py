import unittest

from atm import ATM, DAILY_LIMIT, Account
from errors import (ATMOutOfCashError, CardBlockedError, CardNotFoundError, DailyLimitError,
                    InsufficientFundsError, InvalidAmountError, WrongPINError)


class TestATM(unittest.TestCase):
    def setUp(self):
        self.atm = ATM([Account("1111", "1234", "Asha", 50000)], cash=30000)
        self.acc = self.atm.login("1111", "1234")

    def test_unknown_card(self):
        with self.assertRaises(CardNotFoundError):
            self.atm.login("9999", "0000")

    def test_three_wrong_pins_block_card(self):
        with self.assertRaises(WrongPINError) as ctx:
            self.atm.login("1111", "0000")
        self.assertEqual(ctx.exception.attempts_left, 2)
        with self.assertRaises(WrongPINError):
            self.atm.login("1111", "0000")
        with self.assertRaises(CardBlockedError):
            self.atm.login("1111", "0000")
        with self.assertRaises(CardBlockedError):
            self.atm.login("1111", "1234")    # even the right PIN is refused now

    def test_withdraw_gives_fewest_notes(self):
        self.assertEqual(self.atm.withdraw(self.acc, 1800), {500: 3, 200: 1, 100: 1})
        self.assertEqual(self.acc.balance, 48200)

    def test_bad_amounts(self):
        for amount in (0, -100, 150, "abc"):
            with self.assertRaises(InvalidAmountError):
                self.atm.withdraw(self.acc, amount)

    def test_insufficient_funds(self):
        poor = Account("2", "1", "Ben", 300)
        with self.assertRaises(InsufficientFundsError):
            self.atm.withdraw(poor, 500)

    def test_daily_limit(self):
        self.atm.withdraw(self.acc, DAILY_LIMIT)
        with self.assertRaises(DailyLimitError):
            self.atm.withdraw(self.acc, 100)

    def test_atm_runs_out_of_cash(self):
        self.atm.cash = 1000
        with self.assertRaises(ATMOutOfCashError):
            self.atm.withdraw(self.acc, 2000)

    def test_deposit_and_statement(self):
        self.atm.deposit(self.acc, 1000)
        self.assertIn("deposit", self.atm.mini_statement(self.acc))


if __name__ == "__main__":
    unittest.main()
