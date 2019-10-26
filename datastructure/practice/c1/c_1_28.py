import unittest
import math


def norm(*args):
    return math.sqrt(sum(v ** 2 for v in args))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(norm(4, 3), 5)


if __name__ == '__main__':
    unittest.main()
