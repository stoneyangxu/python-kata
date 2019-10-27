import unittest
from datastructure.links.LinkedQueue import LinkedQueue


class MyTestCase(unittest.TestCase):
    def test_something(self):
        queue = LinkedQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual([1, 2, 3], queue.to_list())


if __name__ == '__main__':
    unittest.main()
