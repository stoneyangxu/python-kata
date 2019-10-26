import time

if __name__ == '__main__':
    seq_a = [i for i in range(1000000)]
    seq_b = [i for i in range(1000001, 2000000)]

    start = time.time()
    for k in seq_b:
        seq_a.append(k)
    print('append: {:3f}'.format(time.time() - start))

    seq_a = [i for i in range(1000000)]
    seq_b = [i for i in range(1000001, 2000000)]

    start = time.time()
    seq_a.extend(seq_b)
    print('expend: {:3f}'.format(time.time() - start))
