import matplotlib.pyplot as plt
import math


def f_8n(n):
    return 8 * n


def f_4nlogn(n):
    return 4 * n * math.log2(n)


def f_2n2(n):
    return 2 * (n ** 2)


def f_n3(n):
    return n ** 3


def f_2n(n):
    return 2 ** n


if __name__ == '__main__':
    seq_8n = []
    seq_4nlogn = []
    seq_2n2 = []
    seq_n3 = []
    seq_2n = []

    x = range(1, 12)

    for i in x:
        seq_8n.append(f_8n(i))
        seq_4nlogn.append(f_4nlogn(i))
        seq_2n2.append(f_2n2(i))
        seq_n3.append(f_n3(i))
        seq_2n.append(f_2n(i))

    plt.plot(x, seq_8n, label='8n')
    plt.plot(x, seq_4nlogn, label='4nlog(n)')
    plt.plot(x, seq_2n2, label='2n^2')
    plt.plot(x, seq_n3, label='n^3')
    plt.plot(x, seq_2n, label='2^n')

    plt.legend()

    plt.show()

