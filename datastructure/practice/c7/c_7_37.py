import unittest
from datastructure.links.PositionList import PositionList


def has_sum_equals(position_list, V):
    if position_list.is_empty():
        return None

    sum_dict = {}
    current = position_list.first()

    while current is not None:
        if current.element() in sum_dict:
            return sum_dict[current.element()], current
        sum_dict[V - current.element()] = current
        current = position_list.after(current)
    return None


class MyTestCase(unittest.TestCase):
    def test_something(self):
        position_list = PositionList()
        position_list.add_last(1)
        p = position_list.add_last(3)
        position_list.add_last(4)
        q = position_list.add_last(7)
        position_list.add_last(5)

        self.assertEqual(None, has_sum_equals(position_list, 22))
        self.assertEqual((p, q), has_sum_equals(position_list, 10))


if __name__ == '__main__':
    unittest.main()
