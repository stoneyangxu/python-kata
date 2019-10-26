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

    def __eq__(self, other):
        return self._data == other._data

    def __ne__(self, other):
        return not self._data == other._data


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.v = Vector(5)

    def test_init(self):
        self.assertEqual(str(self.v), "(0, 0, 0, 0, 0)")

    def test_setitem(self):
        self.v[2] = 10
        self.assertEqual(str(self.v), "(0, 0, 10, 0, 0)")

    def test_getitem(self):
        self.v[2] = 10
        self.assertEqual(self.v[2], 10)

    def test_len(self):
        self.assertEqual(len(self.v), 5)

    def test_add(self):
        self.v[1] = 23
        self.v[-1] = 45

        u = self.v + self.v
        self.assertEqual(str(u), "(0, 46, 0, 0, 90)")

        u = self.v + u
        self.assertEqual(str(u), "(0, 69, 0, 0, 135)")

    def test_invalid_add(self):
        other = Vector(3)
        with self.assertRaises(ValueError) as e:
            u = self.v + other

        self.assertEqual(e.exception.args[0], "dimensions must agree")

    def test_equal(self):
        self.v[1] = 23

        other = Vector(5)
        self.assertNotEqual(self.v, other)

        other[1] = 23
        self.assertEqual(self.v, other)


if __name__ == '__main__':
    unittest.main()
