import unittest


def is_even(k):
    return (k >> 1) << 1 == k


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(is_even(0), True)
        self.assertEqual(is_even(1), False)
        self.assertEqual(is_even(2), True)
        self.assertEqual(is_even(12), True)


if __name__ == '__main__':
    unittest.main()
