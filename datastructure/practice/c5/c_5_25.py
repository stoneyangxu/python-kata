import unittest


def remove_all(data, value):
    return [n for n in data if n != value]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        data = [1, 2, 3, 4, 2, 5, 2, 5, 9, 1, 2]
        self.assertEqual([1, 3, 4, 5, 5, 9, 1], remove_all(data, 2))


if __name__ == '__main__':
    unittest.main()
