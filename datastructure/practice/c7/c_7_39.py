import unittest
from datastructure.links.PositionList import PositionList


class PositionalQueue:
    def __init__(self):
        self._position_list = PositionList()

    def __len__(self):
        return len(self._position_list)

    def is_empty(self):
        return self._position_list.is_empty()

    def enqueue(self, e):
        return self._position_list.add_last(e)

    def dequeue(self):
        p = self._position_list.first()
        answer = p.element()
        self._position_list.delete(p)
        return answer


    def delete(self, p):
        self._position_list.delete(p)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        queue = PositionalQueue()

        self.assertEqual(True, queue.is_empty())

        queue.enqueue(1)
        p = queue.enqueue(2)
        queue.enqueue(3)

        queue.delete(p)

        self.assertEqual(False, queue.is_empty())
        self.assertEqual(2, len(queue))

        self.assertEqual(1, queue.dequeue())
        self.assertEqual(3, queue.dequeue())


if __name__ == '__main__':
    unittest.main()
