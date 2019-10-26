import unittest
from collections import deque

def min_time(cows):
    cows.sort()

    left = deque()
    right = deque()

    for cow in cows:
        right.append(cow)

    total_time = 0

    while len(right) >= 2:
        less = right.popleft()
        more = right.popleft()

        left.append(less)
        left.append(more)

        total_time += more

        if len(right) == 0:
            return total_time

        back_cow = left.popleft()
        right.append(back_cow)
        total_time += back_cow

    return total_time


class MyTestCase(unittest.TestCase):
    def test_something(self):
        cows = [2, 4, 10, 20]
        self.assertEqual(34, min_time(cows))


if __name__ == '__main__':
    unittest.main()
