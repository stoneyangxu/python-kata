import unittest
from collections import deque


def factor(n):
    k = 1
    stack = deque()
    while k * k < n:
        if n % k == 0:
            yield k
            stack.append(n // k)
        k += 1
    if k * k == n:
        yield k

    while len(stack) > 0:
        yield stack.pop()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual([n for n in factor(16)], [1, 2, 4, 8, 16])


if __name__ == '__main__':
    unittest.main()
