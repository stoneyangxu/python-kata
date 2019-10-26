import unittest

from datastructure.links.make_link import make_link, from_link
from datastructure.links.Node import Node


def swap_single(L, x, y):
    if x is y:
        return

    head = Node(None, L)

    pre_x = head
    while pre_x._next != x:
        pre_x = pre_x._next

    pre_y = head
    while pre_y._next != y:
        pre_y = pre_y._next

    next_x = x._next
    next_y = y._next

    pre_x._next = y
    y._next = next_x

    pre_y._next = x
    x._next = next_y


class MyTestCase(unittest.TestCase):
    def test_swap_single(self):
        L = make_link([1, 2, 3, 4, 5])

        x = L._next
        y = x._next._next

        swap_single(L, x, y)

        self.assertEqual([1, 4, 3, 2, 5], from_link(L))


if __name__ == '__main__':
    unittest.main()
