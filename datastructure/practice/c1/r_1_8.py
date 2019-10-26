import unittest


def positive_index(s: str, k: int) -> int:
    return len(s) + k


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = "hello world"
        self.assertEqual(positive_index(s, -1), 10)


if __name__ == '__main__':
    unittest.main()
