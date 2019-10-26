import unittest


def multiple(m, n):
    if n == 0:
        return 0
    if n == 1:
        return m
    return multiple(m, n - 1) + m


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(20, multiple(5, 4))


if __name__ == '__main__':
    unittest.main()
