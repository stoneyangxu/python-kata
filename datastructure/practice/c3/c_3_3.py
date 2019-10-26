import unittest
import matplotlib.pyplot as plt


def f_40n2(n):
    return 40 * (n ** 2)


def f_2n3(n):
    return 2 * (n ** 3)


def find_n():
    i = 0
    while True:
        if f_40n2(i) < f_2n3(i):
            break
        i += 1
    return i


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(21, find_n())

        x = range(find_n() * 2)

        seq_1 = [f_40n2(i) for i in x]
        seq_2 = [f_2n3(i) for i in x]

        plt.plot(x, seq_1, label='40n^2')
        plt.plot(x, seq_2, label='2n^3')

        plt.legend()
        plt.show()


if __name__ == '__main__':
    unittest.main()
