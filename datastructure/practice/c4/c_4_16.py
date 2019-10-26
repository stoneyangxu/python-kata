import unittest


def reverse_str(s, start, end):
    if start == end:
        return
    s[start], s[end] = s[end], s[start]
    reverse_str(s, start + 1, end - 1)


def reverse_s(s):
    r = list(s)
    reverse_str(r, 0, len(s) - 1)
    return "".join(r)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = "pots&pans"
        self.assertEqual("snap&stop", reverse_s(s))


if __name__ == '__main__':
    unittest.main()
