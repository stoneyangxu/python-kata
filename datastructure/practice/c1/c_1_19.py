import unittest


def generate_characters() -> list:
    return [chr(i) for i in range(ord('a'), ord('z') + 1)]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(generate_characters(),
                         ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                          't', 'u', 'v', 'w', 'x', 'y', 'z'])


if __name__ == '__main__':
    unittest.main()
