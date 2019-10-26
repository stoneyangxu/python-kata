import unittest

from datastructure.links.make_link import make_link


def link_size(L):
    if L is None:
        return 0
    return 1 + link_size(L._next)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(0, link_size(None))
        self.assertEqual(1, link_size(make_link([1])))
        self.assertEqual(3, link_size(make_link([1, 2, 3])))


if __name__ == '__main__':
    unittest.main()
