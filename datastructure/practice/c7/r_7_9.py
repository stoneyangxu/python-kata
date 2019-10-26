import unittest
from datastructure.links.LinkedDeque import LinkedDeque


def merge_link(L, M):
    if L.is_empty():
        return M
    if M.is_empty():
        return L

    last_L = L._tailer._prev
    first_M = M._header._next

    last_L._next = first_M
    first_M._prev = last_L

    L._tailer = M._tailer

    return L



class MyTestCase(unittest.TestCase):
    def test_something(self):
        L = LinkedDeque()
        L.insert_last(1)
        L.insert_last(2)
        L.insert_last(3)

        M = LinkedDeque()
        M.insert_last(4)
        M.insert_last(5)

        self.assertEqual([1, 2, 3], L.to_list())
        self.assertEqual([4, 5], M.to_list())
        self.assertEqual([1, 2, 3, 4, 5], merge_link(L, M).to_list())


if __name__ == '__main__':
    unittest.main()
