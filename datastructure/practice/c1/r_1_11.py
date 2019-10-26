import unittest


def r_1_11() -> list:
    return [2 ** n for n in range(0, 9)]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(r_1_11(), [1, 2, 4, 8, 16, 32, 64, 128, 256])


if __name__ == '__main__':
    unittest.main()
