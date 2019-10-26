import os


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            total += disk_usage(os.path.join(path, filename))
    print("{0:<10}".format(total), path)
    return total


if __name__ == '__main__':
    disk_usage("/Users/xuyang/Documents/xmind")
