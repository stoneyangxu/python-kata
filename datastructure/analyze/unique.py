import unittest


def unique1(S):
    for j in range(len(S)):
        for k in range(j + 1, len(S)):
            if S[j] == S[k]:
                return False
    return True


def unique2(S):
    sorted_s = sorted(S)
    for j in range(1, len(S)):
        if sorted_s[j] == sorted_s[j - 1]:
            return False
    return True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        S = [1, 2, 3, 4, 22, 2, 3]
        self.assertEqual(False, unique1(S))
        self.assertEqual(False, unique2(S))


if __name__ == '__main__':
    unittest.main()
