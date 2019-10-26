import unittest


def find_min_max(seq, start, end):
    if start == end:
        return seq[start], seq[start]

    if start == end - 1:
        left = seq[start]
        right = seq[end]
        return (left, right) if left > right else (right, left)

    mid = (start + end) // 2

    left_max, left_min = find_min_max(seq, start, mid - 1)
    right_max, right_min = find_min_max(seq, mid, end)
    return max(left_max, right_max), min(left_min, right_min)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = [1, 55, 2, 3, 22, 3, 23, 21]
        self.assertEqual((55, 1), find_min_max(s, 0, len(s) - 1))


if __name__ == '__main__':
    unittest.main()
