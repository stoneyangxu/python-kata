import unittest
from datastructure.links.PositionList import PositionList


class MyTestCase(unittest.TestCase):
    def test_something(self):
        position_list = PositionList()
        position_list.add_last(1)
        position_list.add_last(2)
        p = position_list.add_last(3)

        r = [e for e in position_list]
        self.assertEqual([1, 2, 3], r)

        position_list.move_to_front(p)
        r = [e for e in position_list]
        self.assertEqual([3, 1, 2], r)


if __name__ == '__main__':
    unittest.main()
