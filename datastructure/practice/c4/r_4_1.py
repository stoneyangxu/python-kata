import unittest


def find_max(seq, start, end):
    if start == end:
        return seq[start]
    if start == end - 1:
        return max(seq[start], seq[end])
    mid = (start + end) // 2
    left_max = find_max(seq, start, mid - 1)
    right_max = find_max(seq, mid, end)
    return max(left_max, right_max)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        seq = [1, 44, 6, 2, 3, 5, 19, 2, 22, 33]
        self.assertEqual(44, find_max(seq, 0, len(seq) - 1))


if __name__ == '__main__':
    unittest.main()
