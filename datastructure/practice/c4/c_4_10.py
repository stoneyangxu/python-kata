import unittest
import math


def get_integer_part(n):
    i = 0
    while n > 1:
        n /= 2
        i += 1
    return i - 1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(7, get_integer_part(145))


if __name__ == '__main__':
    unittest.main()
