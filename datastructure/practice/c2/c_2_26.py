import unittest


class ReversedSequenceIterator:

    def __init__(self, sequence):
        self._seq = sequence
        self._index = len(sequence) - 1

    def __next__(self):
        if self._index < 0:
            raise StopIteration
        current = self._seq[self._index]
        self._index -= 1
        return current

    def __iter__(self):
        return self


class MyTestCase(unittest.TestCase):
    def test_something(self):
        l = [1, 2, 3, 4, 5]

        iter = ReversedSequenceIterator(l)

        self.assertEqual(5, next(iter))
        self.assertEqual(4, next(iter))
        self.assertEqual(3, next(iter))
        self.assertEqual(2, next(iter))
        self.assertEqual(1, next(iter))

        with self.assertRaises(StopIteration):
            next(iter)


if __name__ == '__main__':
    unittest.main()
