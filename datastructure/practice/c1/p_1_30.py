import unittest


def count_division(n):
    count = 0
    while True:
        if n < 2:
            break
        n = n // 2
        count += 1
    return count


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(count_division(5), 2)
        self.assertEqual(count_division(10), 3)


if __name__ == '__main__':
    unittest.main()
