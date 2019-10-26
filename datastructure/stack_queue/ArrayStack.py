import unittest
from datastructure.stack_queue.Empty import Empty


class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
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
        stack = ArrayStack()
        self.assertEqual(True, stack.is_empty())

        stack.push(1)
        self.assertEqual(1, len(stack))
        self.assertEqual(1, stack.top())
        self.assertEqual(1, stack.pop())
        self.assertEqual(0, len(stack))

        with self.assertRaises(Empty):
            stack.pop()

        with self.assertRaises(Empty):
            stack.top()


if __name__ == '__main__':
    unittest.main()
