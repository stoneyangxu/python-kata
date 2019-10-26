import unittest


def generate_seq() -> list:
    return [i * (i + 1) for i in range(10)]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(generate_seq(), [0, 2, 6, 12, 20, 30, 42, 56, 72, 90])


if __name__ == '__main__':
    unittest.main()
