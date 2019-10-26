import unittest
import ctypes


class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    @staticmethod
    def _make_array(c):
        return (c * ctypes.py_object)()

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def pop(self):
        if self._n == 0:
            raise IndexError("empty list")
        item = self._A[self._n - 1]
        self._A[self._n - 1] = None
        self._n -= 1
        if self._n < self._capacity / 4:
            self._resize(self._capacity // 2 + 1)
        return item

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c


class MyTestCase(unittest.TestCase):
    def test_something(self):
        da = DynamicArray()
        for i in range(10):
            da.append(i)

        r = [i for i in da]
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], r)

        self.assertEqual(9, da.pop())
        self.assertEqual(8, da.pop())

        r = [i for i in da]
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7], r)


if __name__ == '__main__':
    unittest.main()
