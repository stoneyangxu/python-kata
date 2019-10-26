import unittest

from datastructure.practice.c2.r_2_5 import CreditCard


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._count = 0
        self._last_month_payment = 0

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        if self._count >= 10:
            self._balance += 1
        self._count += 1
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor
        self._count = 0

        if self._last_month_payment == 0:
            print("didn't pay last month")
        self._last_month_payment = 0

    def make_payment(self, amount):
        super().make_payment(amount)
        self._last_month_payment = amount


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pass


if __name__ == '__main__':
    unittest.main()
