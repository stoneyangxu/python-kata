import unittest


def power(x, n):
    r = 1
    for i in range(n // 2):
        r *= (x * x)
    if n % 2 == 1:
        r *= x
    return r


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(16, power(2, 4))
        self.assertEqual(32, power(2, 5))


if __name__ == '__main__':
    unittest.main()
