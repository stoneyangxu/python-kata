import unittest
import random


def custom_shuffle(data: list) -> list:
    original = data.copy()
    result = []

    while True:
        i = random.randint(0, len(original) - 1)
        result.append(original[i])
        del original[i]
        if not original:
            break

    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(custom_shuffle(data))
        print(custom_shuffle(data))
        print(custom_shuffle(data))
        print(custom_shuffle(data))
        print(custom_shuffle(data))
        print(custom_shuffle(data))
        print(custom_shuffle(data))
        print(custom_shuffle(data))
        print(custom_shuffle(data))
        print(custom_shuffle(data))


if __name__ == '__main__':
    unittest.main()
