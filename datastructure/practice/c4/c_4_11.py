import unittest


def unique(seq, start, end):
    pass


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, unique([1, 2, 3, 4, 5], 0, 4))
        self.assertEqual(False, unique([1, 2, 3, 4, 2], 0, 4))


if __name__ == '__main__':
    unittest.main()
