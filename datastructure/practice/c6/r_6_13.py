import unittest
from collections import deque


def move(D, Q):
    Q.append(D.popleft())
    Q.append(D.popleft())
    Q.append(D.popleft())

    # put 4 at the end of D
    D.append(D.popleft())

    # move 5
    Q.append(D.popleft())

    # move 4 from the end of D
    Q.append(D.pop())

    Q.append(D.popleft())
    Q.append(D.popleft())
    Q.append(D.popleft())


class MyTestCase(unittest.TestCase):
    def test_something(self):
        D = deque()
        for i in range(1, 9):
            D.append(i)

        Q = deque()

        move(D, Q)

        self.assertEqual([1, 2, 3, 5, 4, 6, 7, 8], [n for n in Q])


if __name__ == '__main__':
    unittest.main()
