class Flower:
    def __init__(self, name, amount, price):
        self._name = name
        self._amount = amount
        self._price = price

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_amount(self, amount):
        self._amount = amount

    def get_amount(self):
        return self._amount

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price
