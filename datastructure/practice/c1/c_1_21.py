def reverse_input():
    inputs = []
    try:
        while True:
            line = input()
            inputs.append(line)
    except EOFError:
        pass

    length = len(inputs)
    for i in range(length):
        print(inputs[length - i - 1])


if __name__ == '__main__':
    reverse_input()
