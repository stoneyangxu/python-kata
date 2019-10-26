import unittest


def keep_words(s) -> str:
    start = ord('A')
    end = ord('z')
    words = [c for c in s if start <= ord(c) <= end or c == ' ']
    return "".join(words)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(keep_words(""), "")
        self.assertEqual(keep_words("Let's try, Mike."), "Lets try Mike")


if __name__ == '__main__':
    unittest.main()
