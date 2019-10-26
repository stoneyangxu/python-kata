import unittest


def sum_matrix(matrix):
    amount = 0
    for line in matrix:
        for k in line:
            amount += k
    return amount


class MyTestCase(unittest.TestCase):
    def test_something(self):
        matrix = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
        self.assertEqual(30, sum_matrix(matrix))


if __name__ == '__main__':
    unittest.main()
