import timeit
import matplotlib.pyplot as plt

if __name__ == '__main__':
    size_list = []
    time_list = []
    for size in range(1000, 100000, 1000):
        seq = [i for i in range(size)]

        t = timeit.timeit('sum(s)', number=1000, setup="s=range({})".format(size))
        size_list.append(size)
        time_list.append(t * 1000)
        print("size: {}, time: {}".format(size, t * 1000))

    fig, ax = plt.subplots()
    ax.scatter(size_list, time_list)
    plt.show()

