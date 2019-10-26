import unittest
import time


class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("step cannot be 0")

        if stop is None:
            start, stop = 0, start

        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, i):
        if i < 0:
            i += len(self)
        if not 0 <= i < self._length:
            raise IndexError("index out of range")
        return self._start + i * self._step

    def __contains__(self, val):
        return (val - self._start) % self._step == 0


class MyTestCase(unittest.TestCase):
    def test_something(self):
        start = time.time()
        print(2 in Range(100000000))
        time1 = time.time()
        print(9999999 in Range(100000000))
        time2 = time.time()

        print(time2 - time1, time1 - start, (time2 - time1) // (time1 - start))


if __name__ == '__main__':
    unittest.main()
