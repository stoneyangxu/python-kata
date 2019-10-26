import unittest


def move_to_t(R, S, T):
    length = len(S)
    while len(S) > 0:
        R.append(S.pop())
    while length > 0:
        T.append(R.pop())
        length -= 1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        R = [1, 2, 3]
        S = [4, 5]
        T = [6, 7, 8, 9]
        move_to_t(R, S, T)
        self.assertEqual([6, 7, 8, 9, 4, 5], T)


if __name__ == '__main__':
    unittest.main()
