import unittest
from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next_handler):
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, a, b, c):
        pass


class PlusHandler(Handler):
    def handle(self, a, b, c):
        return a + b == c or a == b + c


class MinusHandler(Handler):
    def handle(self, a, b, c):
        return a - b == c or a == b - c


class MultipleHandler(Handler):
    def handle(self, a, b, c):
        return a * b == c or a == b * c


class DivisionHandler(Handler):
    def handle(self, a, b, c):
        return a / b == c or a == b / c


def main(a, b, c):
    division = DivisionHandler(None)
    multiple = MultipleHandler(division)
    minus = MinusHandler(multiple)
    plus = PlusHandler(minus)

    current = plus
    while current:
        if current.handle(a, b, c):
            return True
        else:
            current = current.next_handler
    return False


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(main(1, 2, 3), True)
        self.assertEqual(main(3, 2, 1), True)
        self.assertEqual(main(2, 2, 0), True)
        self.assertEqual(main(0, 2, 2), True)
        self.assertEqual(main(2, 3, 6), True)
        self.assertEqual(main(2, 3, 10), False)


if __name__ == '__main__':
    unittest.main()
