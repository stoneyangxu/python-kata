import unittest
from datastructure.links.LinkedDeque import LinkedDeque

class MyTestCase(unittest.TestCase):
    def test_something(self):
        linked_deque = LinkedDeque()
        linked_deque.insert_last(1)
        linked_deque.insert_last(2)
        linked_deque.insert_last(3)

        self.assertEqual([1, 2, 3], linked_deque.to_list())

        reversed(linked_deque)

        self.assertEqual([3, 2, 1], linked_deque.to_list())


if __name__ == '__main__':
    unittest.main()
