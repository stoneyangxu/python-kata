import unittest
from collections import deque


class QueueAdapter:

    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def add_first(self, e):
        self._data.appendleft(e)

    def add_last(self, e):
        self._data.append(e)

    def delete_first(self):
        return self._data.popleft()

    def delete_last(self):
        return self._data.pop()

    def first(self):
        return self._data[0]

    def last(self):
        return self._data[-1]


    pass


class MyTestCase(unittest.TestCase):
    def test_something(self):
        q = QueueAdapter()
        q.add_first(1)
        q.add_last(2)
        q.add_last(3)

        self.assertEqual(1, q.first())
        self.assertEqual(3, q.last())
        self.assertEqual(1, q.delete_first())
        self.assertEqual(3, q.delete_last())
        self.assertEqual(1, len(q))
        self.assertEqual(2, q.delete_first())

        with self.assertRaises(IndexError):
            q.delete_first()


if __name__ == '__main__':
    unittest.main()
