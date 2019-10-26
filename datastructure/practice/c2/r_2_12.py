import unittest


class Vector:

    def __init__(self, size):
        self._data = [0] * size

    def __str__(self):
        return "({})".format(str(self._data)[1:-1])

    def __setitem__(self, i, value):
        self._data[i] = value

    def __getitem__(self, i):
        return self._data[i]

    def __len__(self):
        return len(self._data)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        r = Vector(len(self))
        for i in range(len(self)):
            r[i] = self[i] + other[i]
        return r

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        r = Vector(len(self))
        for i in range(len(self)):
            r[i] = self[i] - other[i]
        return r

    def __eq__(self, other):
        return self._data == other._data

    def __ne__(self, other):
        return not self._data == other._data

    def __neg__(self):
        r = Vector(len(self))
        for i in range(len(self)):
            r[i] = -self[i]
        return r

    def __mul__(self, k):
        r = Vector(len(self))
        for i in range(len(self)):
            r[i] = self[i] * k
        return r


class MyTestCase(unittest.TestCase):
    def test_something(self):
        u = Vector(5) + [5, 3, 10, -2, 1]
        r = u * 3

        self.assertEqual(str(r), "(15, 9, 30, -6, 3)")


if __name__ == '__main__':
    unittest.main()
