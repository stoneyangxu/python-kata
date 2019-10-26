import time


def log_call(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print("Before calling func:")
        return_value = func(*args, **kwargs)
        print("After calling func: {} {}".format(func.__name__, time.time() - start))
        return return_value

    return wrapper


@log_call
def time1():
    print("Called time1")


@log_call
def time2(a, b):
    print("Called time2: {} {}".format(a, b))


def main():
    time1()
    time2(1, 2)


if __name__ == '__main__':
    main()
