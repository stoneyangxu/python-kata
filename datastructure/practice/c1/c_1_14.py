import unittest


def exist_odd(seq: list) -> bool:
    length = len(seq)

    for i, n in enumerate(seq):
        for j in range(i + 1, length):
            m = seq[j]
            if (n * m % 2) == 1 and n != m:
                return True

    return False


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(exist_odd([]), False)
        self.assertEqual(exist_odd([1, 2, 3]), True)
        self.assertEqual(exist_odd([1, 2, 2]), False)
        self.assertEqual(exist_odd([1, 2, 1]), False)


if __name__ == '__main__':
    unittest.main()
