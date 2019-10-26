def factors(n):
    k = 1
    while k ** 2 < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k ** 2 == n:
        yield k


if __name__ == '__main__':
    for x in factors(100):
        print(x, end=" ")
