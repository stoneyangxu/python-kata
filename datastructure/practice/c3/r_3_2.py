import unittest
import math
import matplotlib.pyplot as plt


def f_8nlogn(n):
    return 8 * n * math.log2(n)


def f_2n2(n):
    return 2 * (n ** 2)


def find_n():
    i = 2
    while True:
        a1 = f_8nlogn(i)
        a2 = f_2n2(i)
        if a1 < a2:
            break
        i += 1
    return i


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(17, find_n())

        x = range(2, find_n() * 2)

        seq_1 = []
        seq_2 = []

        for i in x:
            seq_1.append(f_8nlogn(i))
            seq_2.append(f_2n2(i))

        plt.plot(x, seq_1, label='8nlog(n)')
        plt.plot(x, seq_2, label='2n^2')

        plt.legend()
        plt.show()


if __name__ == '__main__':
    unittest.main()
