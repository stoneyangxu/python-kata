import unittest
from datastructure.links.Node import Node


def from_second(head):
    if head is None:
        raise ValueError("Linked list is empty")
    return head._next


class MyTestCase(unittest.TestCase):
    def test_something(self):
        head = Node(0, None)
        current = head
        for i in range(1, 6):
            new_node = Node(i, None)
            current._next = new_node
            current = new_node

        second = from_second(head)

        result = []
        node = second
        while node is not None:
            result.append(node._element)
            node = node._next

        self.assertEqual([1, 2, 3, 4, 5], result)


if __name__ == '__main__':
    unittest.main()
