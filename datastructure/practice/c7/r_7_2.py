import unittest
from datastructure.links.make_link import make_link
from datastructure.links.make_link import from_link


def connect_link(L, M):
    if L is None:
        return M

    head = L
    current = head
    while current._next is not None:
        current = current._next
    current._next = M

    return head


class MyTestCase(unittest.TestCase):
    def test_something(self):
        L = make_link([1, 2, 3])
        M = make_link([4, 5])
        self.assertEqual([1, 2, 3, 4, 5], from_link(connect_link(L, M)))

        self.assertEqual([4, 5], from_link(connect_link(None, make_link([4, 5]))))

        self.assertEqual([1, 2, 3], from_link(connect_link(make_link([1, 2, 3]), None)))

        self.assertEqual(None, connect_link(None, None))


if __name__ == '__main__':
    unittest.main()
