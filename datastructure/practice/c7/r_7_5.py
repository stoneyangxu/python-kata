import unittest

from datastructure.links.CircularQueue import CircularQueue


def count_nodes(queue):
    if queue.is_empty():
        return 0
    head = queue._tail

    queue.rotate()
    count = 1

    current = head._next
    while current != head:
        count += 1
        current = current._next
    return count


class MyTestCase(unittest.TestCase):
    def test_swap_single(self):
        queue = CircularQueue()

        self.assertEqual(True, queue.is_empty())

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        count_nodes(queue)

        self.assertEqual(0, count_nodes(CircularQueue()))
        self.assertEqual(3, count_nodes(queue))


if __name__ == '__main__':
    unittest.main()
