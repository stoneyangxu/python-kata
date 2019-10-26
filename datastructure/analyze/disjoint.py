import unittest


def disjoint1(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True


def disjoint2(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        A = [1, 2, 3]
        B = [2, 3, 4]
        C = [3, 4, 5]
        self.assertEqual(False, disjoint1(A, B, C))
        self.assertEqual(False, disjoint2(A, B, C))


if __name__ == '__main__':
    unittest.main()
