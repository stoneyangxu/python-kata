import unittest


def change(need, total):
    money = [100, 50, 20, 10, 5, 1, 0.5, 0.1]

    left = total - need

    result = {}
    for n in money:
        while left >= n:
            left -= n
            if n in result:
                result[n] = result[n] + 1
            else:
                result[n] = 1
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(change(1, 1), {})
        self.assertEqual(change(1, 10), {5: 1, 1: 4})
        self.assertEqual(change(14, 100), {1: 1, 5: 1, 10: 1, 20: 1, 50: 1})


if __name__ == '__main__':
    unittest.main()
