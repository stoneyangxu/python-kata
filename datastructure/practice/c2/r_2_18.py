import unittest
from datastructure.oop.progression.test_progression import FibonacciProgression


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p = FibonacciProgression(2, 2)
        self.assertEqual(42, [next(p) for i in range(8)][7])


if __name__ == '__main__':
    unittest.main()
