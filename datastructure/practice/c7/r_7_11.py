import unittest
from datastructure.links.PositionList import PositionList


def find_max_value(position_list):
    if position_list.is_empty():
        raise ValueError("Position list is empty")

    current = position_list.first()
    max_value = current.element()
    while current is not None:
        max_value = max(max_value, current.element())
        current = position_list.after(current)
    return max_value


class MyTestCase(unittest.TestCase):
    def test_something(self):
        position_list = PositionList()
        position_list.add_last(4)
        position_list.add_last(2)
        position_list.add_last(3)
        position_list.add_last(5)
        position_list.add_last(1)

        self.assertEqual(5, find_max_value(position_list))


if __name__ == '__main__':
    unittest.main()
