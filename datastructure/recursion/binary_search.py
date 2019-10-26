import unittest


def binary_search(data, target, low, high):

    if low > high:
        return -1
    mid = (high + low) // 2
    if data[mid] == target:
        return mid
    elif data[mid] < target:
        return binary_search(data, target, mid + 1, high)
    else:
        return binary_search(data, target, low, mid - 1)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]

        self.assertEqual(10, binary_search(data, 22, 0, len(data) - 1))


if __name__ == '__main__':
    unittest.main()
