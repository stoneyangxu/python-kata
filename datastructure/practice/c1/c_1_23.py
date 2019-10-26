if __name__ == '__main__':
    try:
        seq = [1, 2, 3]
        print(seq[0])
        print(seq[1])
        print(seq[2])
        print(seq[3])
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")
