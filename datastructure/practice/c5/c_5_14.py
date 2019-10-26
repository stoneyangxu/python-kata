import random


def random_list(seq):
    result = []

    while len(seq) > 0:
        result.append(seq.pop(random.randrange(len(seq))))

    return result


if __name__ == '__main__':
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    r = random_list(seq)
    print(r)
