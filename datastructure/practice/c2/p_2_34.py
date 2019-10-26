from os import listdir
from collections import defaultdict
import matplotlib.pyplot as plt


def statistic():
    words = defaultdict(int)
    for path in listdir("."):
        with open(path, "r") as f:
            for line in f:
                for word in line.split():
                    count = words[word]
                    words[word] = count + 1

    top5 = sorted(words.items(), key=lambda x: x[1], reverse=True)[:5]

    print(top5)

    names = tuple(t[0] for t in top5)
    freqs = tuple(t[1] for t in top5)

    print(names, freqs)

    plt.bar(range(5), freqs, 0.25)
    plt.title('Words frequency')
    plt.xticks(range(5), names)
    plt.show()


if __name__ == '__main__':
    statistic()
