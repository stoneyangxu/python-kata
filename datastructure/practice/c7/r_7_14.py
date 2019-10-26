import unittest
from datastructure.links.PositionList import PositionList


class MyTestCase(unittest.TestCase):
    def test_something(self):
        position_list = PositionList()
        position_list.add_last(4)
        position_list.add_last(2)
        p = position_list.add_last(3)
        position_list.add_last(5)
        position_list.add_last(1)

        self.assertEqual(p, position_list.find(3))


if __name__ == '__main__':
    unittest.main()
