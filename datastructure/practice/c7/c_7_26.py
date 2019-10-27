import unittest
from datastructure.links.LinkedQueue import LinkedQueue


class MyTestCase(unittest.TestCase):
    def test_something(self):
        queue1 = LinkedQueue()
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)

        queue2 = LinkedQueue()
        queue2.enqueue(4)
        queue2.enqueue(5)

        self.assertEqual([1, 2, 3], queue1.to_list())
        self.assertEqual([4, 5], queue2.to_list())

        queue1.concatenate(queue2)
        self.assertEqual([1, 2, 3, 4, 5], queue1.to_list())
        self.assertEqual([], queue2.to_list())




if __name__ == '__main__':
    unittest.main()
