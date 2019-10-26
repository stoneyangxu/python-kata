import unittest


def range_8() -> list:
    return [n for n in range(8, -10, -2)]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(range_8(), [8, 6, 4, 2, 0, -2, -4, -6, -8])


if __name__ == '__main__':
    unittest.main()
