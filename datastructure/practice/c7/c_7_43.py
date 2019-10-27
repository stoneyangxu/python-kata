import unittest
from datastructure.links.PositionList import PositionList


class MyTestCase(unittest.TestCase):
    def test_something(self):
        L = PositionList()
        L.add_last(1)
        L.add_last(2)
        L.add_last(3)
        L.add_last(4)
        L.add_last(5)
        L.add_last(6)
        L.add_last(7)

        L.shuffle()

        r = [k for k in L]

        self.assertEqual([1, 5, 2, 6, 3, 7, 4], r)


if __name__ == '__main__':
    unittest.main()
