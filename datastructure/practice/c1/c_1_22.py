import unittest


def dot_product(a, b) -> list:
    min_length = min(len(a), len(b))
    return [a[i] * b[i] for i in range(min_length)]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(dot_product([], []), [])
        self.assertEqual(dot_product([1], [2]), [2])
        self.assertEqual(dot_product([1], []), [])
        self.assertEqual(dot_product([1, 2], [2, 4, 6]), [2, 8])


if __name__ == '__main__':
    unittest.main()
