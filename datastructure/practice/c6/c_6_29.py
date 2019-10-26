import unittest
from datastructure.stack_queue.Empty import Empty
from datastructure.stack_queue.Full import Full


class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self, maxlen=None):
        self._data = [None] * (ArrayQueue.DEFAULT_CAPACITY if maxlen is None else maxlen)
        self._size = 0
        self._front = 0
        self._maxlen = maxlen

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            if self._maxlen is not None:
                raise Full("Queue is full")
            else:
                self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def rotate(self, e):
        r = self.dequeue()
        self.enqueue(e)
        return r

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


class MyTestCase(unittest.TestCase):
    def test_something(self):
        queue = ArrayQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(3, len(queue))

        self.assertEqual(1, queue.rotate(4))
        self.assertEqual(2, queue.rotate(5))
        self.assertEqual(3, queue.rotate(6))
        self.assertEqual(4, queue.rotate(7))
        self.assertEqual(5, queue.rotate(8))
        self.assertEqual(6, queue.rotate(9))

        self.assertEqual(3, len(queue))



if __name__ == '__main__':
    unittest.main()
