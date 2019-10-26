import unittest


def odd_quadratic_sum(n: int) -> int:
    """calculate the quadratic num of odd from 1 ~ n"""
    return sum(n ** 2 for n in range(1, n + 1) if n % 2 == 1)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(odd_quadratic_sum(1), 1)
        self.assertEqual(odd_quadratic_sum(2), 1)
        self.assertEqual(odd_quadratic_sum(3), 10)


if __name__ == '__main__':
    unittest.main()
