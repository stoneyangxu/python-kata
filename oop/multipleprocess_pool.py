from multiprocessing.pool import Pool
import random

def prime_factor(value):
    factors = []
    for divisor in range(2, value - 1):
        quotient, remainder = divmod(value, divisor)
        if not remainder:
            factors.extend(prime_factor(divisor))
            factors.extend(prime_factor(quotient))
            break
        else:
            factors = [value]
    return factors


if __name__ == '__main__':
    pool = Pool()

    to_factor = [random.randint(10000, 5000000) for i in range(20)]
    results = pool.map(prime_factor, to_factor)
    for value, factors in zip(to_factor, results):
        print("The factors of {} are {}.".format(value, factors))