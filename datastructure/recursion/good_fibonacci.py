def good_fibnacci(n):
    if n <= 1:
        return n, 0
    a, b = good_fibnacci(n - 1)
    return a + b, a


if __name__ == '__main__':
    n, prev = good_fibnacci(10)
    print(n)
