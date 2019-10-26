import unittest
from datastructure.links.PositionList import PositionList


class MyTestCase(unittest.TestCase):
    def test_something(self):
        position_list = PositionList()
        position_list.add_last(4)
        position_list.add_last(2)
        position_list.add_last(3)

        r = [e for e in reversed(position_list)]

        self.assertEqual([3, 2, 4], r)


if __name__ == '__main__':
    unittest.main()
