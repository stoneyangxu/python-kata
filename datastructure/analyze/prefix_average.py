import unittest
import timeit


def prefix_avg1(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)
    return A


def prefix_avg2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[:j + 1]) / (j + 1)
    return A

def prefix_avg3(S):
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j + 1)
    return A


class MyTestCase(unittest.TestCase):
    def test_prefix_avg1(self):
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5], prefix_avg1(S))
        self.assertEqual([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5], prefix_avg2(S))
        self.assertEqual([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5], prefix_avg3(S))


if __name__ == '__main__':
    unittest.main()
