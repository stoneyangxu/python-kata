import unittest


def reverse_list(seq: list) -> list:
    result = []
    i = len(seq) - 1
    while i >= 0:
        result.append(seq[i])
        i -= 1

    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])


if __name__ == '__main__':
    unittest.main()
