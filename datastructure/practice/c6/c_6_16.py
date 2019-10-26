import unittest
from datastructure.stack_queue.Empty import Empty
from datastructure.stack_queue.Full import Full


class ArrayStack:

    def __init__(self, maxlen=None):
        self._data = []
        self._maxlen = maxlen

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        if self._maxlen is not None and len(self._data) == self._maxlen:
            raise Full("Stack is full")
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        stack = ArrayStack(2)
        stack.push(1)
        stack.push(2)

        with self.assertRaises(Full):
            stack.push(3)


if __name__ == '__main__':
    unittest.main()
