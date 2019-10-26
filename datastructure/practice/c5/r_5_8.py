import time


def pop_time(n, cal_k):
    seq = [i for i in range(n)]

    start = time.time()

    for i in range(n):
        seq.pop(cal_k(len(seq)))

    return time.time() - start


if __name__ == '__main__':
    n_list = [100, 1000, 10000, 100000, 1000000]

    print("-" * 20)
    print("k = 0")
    for n in n_list:
        time_cost = pop_time(n, lambda len: 0)
        print("n = {:8d} costs: {:.3f}".format(n, time_cost))

    print("-" * 20)
    print("k = n // 2")
    for n in n_list:
        time_cost = pop_time(n, lambda len: len // 2)
        print("n = {:8d} costs: {:.3f}".format(n, time_cost))

    print("-" * 20)
    print("k = n - 1")
    for n in n_list:
        time_cost = pop_time(n, lambda len: len - 1)
        print("n = {:8d} costs: {:.3f}".format(n, time_cost))

# --------------------
# k = 0
# n =      100 costs: 0.000
# n =     1000 costs: 0.001
# n =    10000 costs: 0.025
# n =   100000 costs: 1.919
# n =  1000000 costs: 349.762
# --------------------
# k = n // 2
# n =      100 costs: 0.000
# n =     1000 costs: 0.000
# n =    10000 costs: 0.008
# n =   100000 costs: 0.838
# n =  1000000 costs: 124.893
# --------------------
# k = n - 1
# n =      100 costs: 0.000
# n =     1000 costs: 0.000
# n =    10000 costs: 0.003
# n =   100000 costs: 0.032
# n =  1000000 costs: 0.333
