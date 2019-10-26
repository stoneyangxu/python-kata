import unittest
from datastructure.links.PositionList import PositionList
from datastructure.links.FavoritesList import FavoritesList


class FavoritesListMTF(FavoritesList):

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        temp = PositionList()
        for item in self._data:
            temp.add_last(item)

        for j in range(k):
            high_pos = temp.first()
            walk = temp.after(high_pos)
            while walk is not None:
                if walk.element()._count > high_pos.element()._count:
                    high_pos = walk
                walk = temp.after(walk)
            yield high_pos.element()._value
            temp.delete(high_pos)

    def _move_up(self, p):
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        favorites_list = FavoritesListMTF()

        self.assertEqual(True, favorites_list.is_empty())

        favorites_list.access("A")
        favorites_list.access("B")
        favorites_list.access("B")
        favorites_list.access("B")
        favorites_list.access("C")
        favorites_list.access("C")

        self.assertEqual(False, favorites_list.is_empty())
        self.assertEqual(3, len(favorites_list))

        top2 = [k for k in favorites_list.top(2)]
        self.assertEqual(['B', 'C'], top2)

        favorites_list.remove("B")
        top2 = [k for k in favorites_list.top(2)]
        self.assertEqual(['C', 'A'], top2)


if __name__ == '__main__':
    unittest.main()
