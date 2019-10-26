import unittest

vowels = {'a', 'e', 'i', 'o', 'u'}

def to_int(c):
    return 1 if c in vowels else 0

def get_vowel_amount(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return to_int(s)
    return to_int(s[0]) + get_vowel_amount(s[1:])


def more_vowel(s):
    vowel_amount = get_vowel_amount(s)
    return vowel_amount > len(s) - vowel_amount


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, more_vowel("aob"))
        self.assertEqual(False, more_vowel("abc"))
        self.assertEqual(False, more_vowel("abco"))


if __name__ == '__main__':
    unittest.main()
