import sys

if __name__ == '__main__':
    data = []
    current_size = sys.getsizeof(data)
    for i in range(200):
        length = len(data)
        size = sys.getsizeof(data)
        if size != current_size:
            print(i, end=" ")
            current_size = size
        data.append(i)
