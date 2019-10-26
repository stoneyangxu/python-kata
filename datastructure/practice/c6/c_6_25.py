import unittest
from datastructure.stack_queue.ArrayStack import ArrayStack


class QueueWithTwoStack:

    def __init__(self):
        self._stack1 = ArrayStack()
        self._stack2 = ArrayStack()

    def __len__(self):
        return len(self._stack1) + len(self._stack2)

    def enqueue(self, e):
        self.__dump(self._stack2, self._stack1)
        self._stack1.push(e)

    def dequeue(self):
        self.__dump(self._stack1, self._stack2)
        return self._stack2.pop()

    def first(self):
        self.__dump(self._stack1, self._stack2)
        return self._stack2.top()

    def is_empty(self):
        return len(self) == 0

    @staticmethod
    def __dump(source, dist):
        while len(source) != 0:
            dist.push(source.pop())


class MyTestCase(unittest.TestCase):
    def test_something(self):
        queue = QueueWithTwoStack()
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
