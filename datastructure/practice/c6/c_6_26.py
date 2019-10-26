import unittest
from collections import deque


class QueueWithDeque:

    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        return self._data.popleft()

    def first(self):
        return self._data[0]

    def is_empty(self):
        return len(self) == 0


class MyTestCase(unittest.TestCase):
    def test_something(self):
        queue = QueueWithDeque()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(3, len(queue))
        self.assertEqual(1, queue.first())
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(False, queue.is_empty())
        self.assertEqual(3, queue.dequeue())
        self.assertEqual(True, queue.is_empty())


if __name__ == '__main__':
    unittest.main()
