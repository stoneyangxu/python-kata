import unittest


def quadratic_sum(n: int) -> int:
    """calculate the quadratic num from 1 ~ n"""
    return sum(n ** 2 for n in range(1, n + 1))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(quadratic_sum(1), 1)
        self.assertEqual(quadratic_sum(2), 5)
        self.assertEqual(quadratic_sum(3), 14)


if __name__ == '__main__':
    unittest.main()
