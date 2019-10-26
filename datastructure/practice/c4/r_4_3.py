def power(x, n):
    print(f"power({x}, {n})")
    if n == 0:
        return 1
    partial = power(x, n // 2)
    result = partial * partial
    if n % 2 == 1:
        result *= x
    return result


if __name__ == '__main__':
    power(2, 18)
