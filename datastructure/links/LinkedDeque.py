import unittest
from datastructure.stack_queue.Empty import Empty


class _DoubleLinkBase:
    class _Node:
        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._tailer = self._Node(None, None, None)
        self._header._next = self._tailer
        self._tailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def __reversed__(self):
        current = self._header
        while current is not None:
            prev = current._prev
            next = current._next

            current._prev = next
            current._next = prev

            current = next

        self._header, self._tailer = self._tailer, self._header

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


class LinkedDeque(_DoubleLinkBase):

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._tailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._tailer._prev, self._tailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._tailer._prev)

    def to_list(self):
        if self.is_empty():
            return []
        seq = []
        current = self._header._next
        while current != self._tailer:
            seq.append(current._element)
            current = current._next
        return seq


class MyTestCase(unittest.TestCase):
    def test_something(self):
        queue = LinkedDeque()

        self.assertEqual(True, queue.is_empty())

        queue.insert_first(1)
        queue.insert_last(2)
        queue.insert_last(3)

        self.assertEqual(False, queue.is_empty())
        self.assertEqual(3, len(queue))
        self.assertEqual(1, queue.first())
        self.assertEqual(3, queue.last())
        self.assertEqual(1, queue.delete_first())
        self.assertEqual(2, queue.delete_first())
        self.assertEqual(3, queue.delete_last())

        self.assertEqual(True, queue.is_empty())


if __name__ == '__main__':
    unittest.main()
