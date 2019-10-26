import random


def make_a_mistake(s):
    index = random.randint(0, len(s) - 1)
    c = s[index]
    while not ord('A') <= ord(c) <= ord('z'):
        index = random.randint(0, len(s) - 1)
        c = s[index]

    new_c = chr(random.randint(ord('A'), ord('z')))
    chars = list(s)
    chars[index] = new_c
    return "".join(chars)


def main():
    template = "I will never spam my friends again."

    error_count = 0
    for i in range(100):
        make_mistake = bool(random.randint(0, 1)) if error_count < 8 else False
        if make_mistake:
            error_count += 1
            print(make_a_mistake(template))
        else:
            print(template)

    pass


if __name__ == '__main__':
    main()
