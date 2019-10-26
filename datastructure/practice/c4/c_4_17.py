import unittest


def is_plalindrome(s):
    if len(s) > 1:
        if s[0] != s[-1]:
            return False
        else:
            return is_plalindrome(s[1:-1])
    else:
        return True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, is_plalindrome("aba"))
        self.assertEqual(False, is_plalindrome("abc"))


if __name__ == '__main__':
    unittest.main()
