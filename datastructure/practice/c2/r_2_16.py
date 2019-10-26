import unittest


def range_length(start, stop, step=1):
    return max(0, (stop - start + step - 1) // step)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(range_length(0, 10), 10)
        self.assertEqual(range_length(0, 10, 2), 5)
        self.assertEqual(range_length(0, 10, 3), 4)
        self.assertEqual(range_length(-10, 0, 3), 4)
        self.assertEqual(range_length(-10, 0, -3), 0)


if __name__ == '__main__':
    unittest.main()
