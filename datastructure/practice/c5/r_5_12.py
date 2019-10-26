import unittest


def sum_matrix(matrix):
    return sum(sum(line) for line in matrix)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        matrix = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
        self.assertEqual(30, sum_matrix(matrix))


if __name__ == '__main__':
    unittest.main()
