import unittest
import random


def random_choise(seq) -> int:
    return seq[random.randrange(0, len(seq))]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.assertEqual(random_choise(seq) in seq, True)
        self.assertEqual(random_choise(seq) in seq, True)
        self.assertEqual(random_choise(seq) in seq, True)
        self.assertEqual(random_choise(seq) in seq, True)
        self.assertEqual(random_choise(seq) in seq, True)


if __name__ == '__main__':
    unittest.main()
