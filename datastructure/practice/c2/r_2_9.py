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


class MyTestCase(unittest.TestCase):
    def test_something(self):
        u = Vector(3)
        u[0] = 6
        u[2] = 5

        v = Vector(3)
        v[0] = 1
        v[1] = 2

        r = u - v

        self.assertEqual(str(r), "(5, -2, 5)")


if __name__ == '__main__':
    unittest.main()
