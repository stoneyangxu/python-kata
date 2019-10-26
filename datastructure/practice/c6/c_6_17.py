import unittest
from datastructure.stack_queue.Empty import Empty
from datastructure.stack_queue.Full import Full


class ArrayStack:

    def __init__(self, maxlen=None):
        self._data = [None] * maxlen if maxlen is not None else []
        self._maxlen = maxlen
        self._current = 0

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        if self._maxlen is not None:
            return self._current == 0
        else:
            return len(self._data) == 0

    def push(self, e):
        if self._maxlen is None:
            self._data.append(e)
        else:
            if self._current >= self._maxlen:
                raise Full("Stack is full")
            else:
                self._data[self._current] = e
                self._current += 1

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        if self._maxlen is not None:
            return self._data[self._current - 1]
        else:
            return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        if self._maxlen is not None:
            self._data[self._current - 1] = None
            self._current -= 1
            return self._data[self._current - 1]
        else:
            return self._data.pop()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        stack = ArrayStack(2)
        stack.push(1)
        stack.push(2)

        with self.assertRaises(Full):
            stack.push(3)

        self.assertEqual(2, stack.top())
        self.assertEqual(1, stack.pop())
        self.assertEqual(True, stack.is_empty())


if __name__ == '__main__':
    unittest.main()
