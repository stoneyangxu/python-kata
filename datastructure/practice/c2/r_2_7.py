import unittest


class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._acnt

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        price = float(price)
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        amount = float(amount)
        if amount < 0:
            raise ValueError("amount cannot be negative")
        self._balance -= amount


class MyTestCase(unittest.TestCase):
    def test_something(self):
        credit_card = CreditCard("Yang", "CBB", "1234 5678", 1000)
        self.assertEqual(credit_card.get_balance(), 0)

        credit_card = CreditCard("Yang", "CBB", "1234 5678", 1000, 500)
        self.assertEqual(credit_card.get_balance(), 500)


if __name__ == '__main__':
    unittest.main()
