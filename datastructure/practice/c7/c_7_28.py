import unittest
from datastructure.links.LinkedQueue import LinkedQueue


def reverse_node(node, next):
    if node is None:
        return next
    next_node = node._next
    node._next = next

    return reverse_node(next_node, node)


def reverse_queue(queue: LinkedQueue):
    if queue.is_empty():
        return queue
    queue._head = reverse_node(queue._head, None)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        queue = LinkedQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        reverse_queue(queue)

        self.assertEqual([3, 2, 1], queue.to_list())


if __name__ == '__main__':
    unittest.main()
