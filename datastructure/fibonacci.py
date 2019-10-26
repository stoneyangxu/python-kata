def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count <= n:
        yield a
        a, b = b, a + b
        count += 1


if __name__ == '__main__':
    print(vars(fibonacci))
    for x in fibonacci(10):
        print(x, end=" ")