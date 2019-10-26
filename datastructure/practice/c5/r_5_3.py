import sys

if __name__ == '__main__':
    data = [i for i in range(100)]
    for i in range(100):
        data.remove(i)

        length = len(data)
        size = sys.getsizeof(data)
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(length, size))
