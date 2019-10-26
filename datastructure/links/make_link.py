import unittest
from datastructure.links.Node import Node


def make_link(seq):
    if len(seq) == 0:
        return None

    head = Node(seq[0], None)
    current = head

    for i in range(1, len(seq)):
        new_node = Node(seq[i], None)
        current._next = new_node
        current = new_node

    return head


def from_link(head):
    if head is None:
        return []
    result = []
    while head is not None:
        result.append(head._element)
        head = head._next
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # self.assertEqual(True, make_link([]) is None)
        # self.assertEqual([], from_link(None))

        seq = [1, 2, 3, 4, 5]
        head = make_link(seq)
        self.assertEqual([1, 2, 3, 4, 5], from_link(head))


if __name__ == '__main__':
    unittest.main()
