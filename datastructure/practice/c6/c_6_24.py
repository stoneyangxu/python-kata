import unittest
from collections import deque


class StackWithQueue:

    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def push(self, e):
        self._data.append(e)

    def pop(self):
        return self._data.pop()

    def top(self):
        if len(self._data) == 0:
            raise IndexError("Stack is empty")
        return self._data[-1]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        stack = StackWithQueue()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(3, len(stack))
        self.assertEqual(3, stack.top())
        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())
        self.assertEqual(0, len(stack))


if __name__ == '__main__':
    unittest.main()
