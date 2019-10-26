import unittest


def is_multiple(n, m):
    return n % m == 0 if m != 0 else True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(is_multiple(10, 5), True)
        self.assertEqual(is_multiple(10, 1), True)
        self.assertEqual(is_multiple(10, 0), True)

        self.assertEqual(is_multiple(10, 3), False)


if __name__ == '__main__':
    unittest.main()
