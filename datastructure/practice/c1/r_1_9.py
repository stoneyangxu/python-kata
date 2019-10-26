import unittest


def range_50_to_80() -> list:
    return [n for n in range(50, 90, 10)]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(range_50_to_80(), [50, 60, 70, 80])


if __name__ == '__main__':
    unittest.main()
