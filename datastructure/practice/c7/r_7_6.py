import unittest
from datastructure.links.CircularQueue import CircularQueue


def from_same_queue(x, y):
    next_node = x._next
    while x != next_node:
        if next_node == y:
            return True
        next_node = next_node._next
    return False


class MyTestCase(unittest.TestCase):
    def test_something(self):
        queue1 = CircularQueue()
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        queue1.enqueue(4)

        x = queue1._tail
        y = x._next._next

        self.assertEqual(True, from_same_queue(x, y))

        queue2 = CircularQueue()
        queue2.enqueue(1)
        queue2.enqueue(2)
        queue2.enqueue(3)

        z = queue2._tail
        self.assertEqual(False, from_same_queue(x, z))


if __name__ == '__main__':
    unittest.main()
