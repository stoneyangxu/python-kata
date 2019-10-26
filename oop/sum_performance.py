import timeit


def by_add(seq):
    amount = 0
    for n in seq:
        amount += n
    return amount


def by_sum(seq):
    return sum(seq)


if __name__ == '__main__':
    total_time = 0
    s = [i for i in range(10000)]
    print(timeit.timeit('by_add(s)', number=10000, setup="from __main__ import by_add; s=range(10000)"))
    print(timeit.timeit('by_sum(s)', number=10000, setup="from __main__ import by_sum; s=range(10000)"))

