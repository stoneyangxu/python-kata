import unittest


def find_duplicate(seq):
    s = set()
    for i in seq:
        if i in s:
            return i
        else:
            s.add(i)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        seq = [1, 2, 3, 4, 5, 9, 7, 2]
        self.assertEqual(2, find_duplicate(seq))


if __name__ == '__main__':
    unittest.main()
