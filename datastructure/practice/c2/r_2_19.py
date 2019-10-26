import unittest
from datastructure.oop.progression.test_progression import ArithmeticProgression


class MyTestCase(unittest.TestCase):
    def test_something(self):
        count = 2e63 / 128
        self.assertEqual(1.5625e+61, count)


if __name__ == '__main__':
    unittest.main()
