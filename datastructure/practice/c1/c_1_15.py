import unittest


def is_diff(seq: list) -> bool:
    s = set()
    for n in seq:
        if n in s:
            return False
        else:
            s.add(n)
    return True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(is_diff([]), True)
        self.assertEqual(is_diff([1, 2, 3]), True)
        self.assertEqual(is_diff([1, 2, 2]), False)


if __name__ == '__main__':
    unittest.main()
