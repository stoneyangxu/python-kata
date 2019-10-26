import time


def print_result(size):
    print('-' * 30)
    print("Size: {:8d}".format(size))

    start = time.time()
    r = ""
    for i in range(size):
        r += str(i)
    end = time.time()
    print('1. {:.3f}'.format(end - start))

    start = time.time()
    r = []
    for i in range(size):
        r.append(str(i))
    "".join(r)
    end = time.time()
    print('2. {:.3f}'.format(end - start))

    start = time.time()
    r = "".join([str(i) for i in range(size)])
    end = time.time()
    print('3. {:.3f}'.format(end - start))

    start = time.time()
    r = "".join(str(i) for i in range(size))
    end = time.time()
    print('4. {:.3f}'.format(end - start))


if __name__ == '__main__':
    size_list = [10000, 100000, 1000000, 10000000]
    for size in size_list:
        print_result(size)
