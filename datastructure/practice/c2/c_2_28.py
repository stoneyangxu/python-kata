import unittest

from datastructure.practice.c2.r_2_5 import CreditCard


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._count = 0

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


class MyTestCase(unittest.TestCase):
    def test_something(self):
        credit_card = PredatoryCreditCard("Yang", "CBB", "1234 5678", 1000, 0.1)

        for i in range(10):
            credit_card.charge(i)

        self.assertEqual(45, credit_card.get_balance())

        credit_card.charge(10)
        self.assertEqual(56, credit_card.get_balance())

        credit_card.charge(100)
        self.assertEqual(157, credit_card.get_balance())


if __name__ == '__main__':
    unittest.main()
