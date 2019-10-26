import sys

if __name__ == '__main__':
    data = []
    for i in range(30):
        length = len(data)
        size = sys.getsizeof(data)
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(length, size))
        data.append(i)
