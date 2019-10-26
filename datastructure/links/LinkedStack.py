import unittest
from datastructure.links.Node import Node
from datastructure.stack_queue.Empty import Empty


class LinkedStack:

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = Node(e, self._head)
        self._size += 1

    def pop(self):
        if self._head is None:
            raise Empty("Stack is empty")
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        return e

    def top(self):
        if self._head is None:
            raise Empty("Stack is empty")
        return self._head._element


class MyTestCase(unittest.TestCase):
    def test_something(self):
        stack = LinkedStack()

        self.assertEqual(True, stack.is_empty())
        self.assertEqual(0, len(stack))

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(False, stack.is_empty())
        self.assertEqual(3, len(stack))

        self.assertEqual(3, stack.top())
        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())

        self.assertEqual(True, stack.is_empty())
        self.assertEqual(0, len(stack))


if __name__ == '__main__':
    unittest.main()
