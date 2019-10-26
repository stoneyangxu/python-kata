import random


def random_birthday():
    return random.randint(1, 365)


def generate_person_list(n):
    return [random_birthday() for i in range(n)]


def has_same_birthday(person_list):
    s = set()
    for n in person_list:
        if n in s:
            return True
        else:
            s.add(n)
    return False


def main():
    for n in range(5, 105, 5):
        same_count = 0
        total = 0
        for i in range(10000):
            if has_same_birthday(generate_person_list(n)):
                same_count += 1
            total += 1
        print("n = {0:3d}, percent: {1:2.2f}%".format(n, same_count / total * 100))


if __name__ == '__main__':
    main()
