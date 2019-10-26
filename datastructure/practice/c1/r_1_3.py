import unittest


def minmax(data) -> (int, int):
    """get (min, max) tuple in the list"""
    if len(data) == 0:
        return None
    min = data[0]
    max = data[1]
    for n in data:
        min = n if n < min else min
        max = n if n > max else max
    return (min, max)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        data = [1, 4, 2, 6, 23, 4, 2, 21]
        self.assertEqual(minmax([]), None)
        self.assertEqual(minmax(data), (1, 23))


if __name__ == '__main__':
    unittest.main()
