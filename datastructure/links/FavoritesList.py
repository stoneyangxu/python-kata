import unittest
from datastructure.links.PositionList import PositionList


class FavoritesList:
    class _Item:
        __slots__ = "_value", "_count"

        def __init__(self, e):
            self._value = e
            self._count = 0

    def __init__(self):
        self._data = PositionList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def access(self, e):
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)

    def top_count(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._count
            walk = self._data.after(walk)

    def clear(self):
        if self.is_empty():
            return
        current = self._data.first()
        while current is not None:
            to_be_deleted = current
            current = self._data.after(current)
            self._data.delete(to_be_deleted)

    def reset_counts(self):
        if self.is_empty():
            return
        current = self._data.first()
        while current is not None:
            current.element()._count = 0
            current = self._data.after(current)

    def _find_position(self, e):
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while walk != self._data.first() and cnt > self._data.before(walk).element()._count:
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        favorites_list = FavoritesList()

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
