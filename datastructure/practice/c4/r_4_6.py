import unittest
import matplotlib.pyplot as plt


def harmonic_number(n):
    if n == 1:
        return 1
    return 1 / n + harmonic_number(n - 1)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, harmonic_number(1))
        self.assertEqual(1.5, harmonic_number(2))
        self.assertEqual(1.5 + 1 / 3, harmonic_number(3))

        s = [harmonic_number(i) for i in range(1, 100)]

        plt.plot(range(1, 100), s, label="Harmonic Number")
        plt.legend()
        plt.show()


if __name__ == '__main__':
    unittest.main()
