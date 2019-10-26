import unittest


def find_duplicates(data):
    exist_set = set()
    duplicate_set = set()
    for n in data:
        if n in exist_set:
            duplicate_set.add(n)
        else:
            exist_set.add(n)
    return duplicate_set


class MyTestCase(unittest.TestCase):
    def test_something(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 5, 8, 9]
        self.assertEqual({2, 4, 5, 8, 9}, find_duplicates(data))


if __name__ == '__main__':
    unittest.main()
