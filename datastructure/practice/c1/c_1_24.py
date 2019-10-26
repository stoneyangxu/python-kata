import unittest


def count_vowel(s) -> int:
    vowels = set("aeiouAEIOU")
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(count_vowel(""), 0)
        self.assertEqual(count_vowel("a"), 1)
        self.assertEqual(count_vowel("ab"), 1)
        self.assertEqual(count_vowel("absspdiuopuifds"), 6)
        self.assertEqual(count_vowel("abssDJLKSAOuifds"), 5)


if __name__ == '__main__':
    unittest.main()
