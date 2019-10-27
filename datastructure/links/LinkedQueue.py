import unittest
from datastructure.links.Node import Node
from datastructure.stack_queue.Empty import Empty


class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        new_node = Node(e, None)
        if self._head is None:
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self._head is None:
            raise Empty("Queue is empty")
        r = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return r

    def to_list(self):
        if self.is_empty():
            return []
        result = []
        current = self._head
        # while current is not None:
        #     result.append(current._element)
        #     current = current._next

        self._to_list(current, result)

        return result

    def _to_list(self, current, result):
        if current is None:
            return
        result.append(current._element)
        self._to_list(current._next, result)

    def rotate(self):
        if self.is_empty():
            return
        current_head = self._head
        self._head = current_head._next
        self._tail._next = current_head
        self._tail = current_head
        current_head._next = None

    def concatenate(self, other_queue):
        if not isinstance(other_queue, LinkedQueue):
            raise TypeError("Other queue should be LinkedQueue")
        if other_queue.is_empty():
            return

        self._size += len(other_queue)
        self._tail._next = other_queue._head

        other_queue._head = None
        other_queue._tail = None
        other_queue._size = 0


class MyTestCase(unittest.TestCase):
    def test_something(self):
        queue = LinkedQueue()

        self.assertEqual(True, queue.is_empty())
        self.assertEqual(0, len(queue))

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(False, queue.is_empty())
        self.assertEqual(3, len(queue))

        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(3, queue.dequeue())


if __name__ == '__main__':
    unittest.main()
