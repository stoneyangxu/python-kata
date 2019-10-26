import unittest
from datastructure.stack_queue.Empty import Empty


class _DoubleLinkBase:
    class _Node:
        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._tailer = self._Node(None, None, None)
        self._header._next = self._tailer
        self._tailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element


class PositionList(_DoubleLinkBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._tailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._tailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def __reversed__(self):
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._tailer._prev, self._tailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

    def max(self):
        if self.is_empty():
            raise ValueError("Position list is empty")
        cursor = self.first()
        max_value = cursor.element()
        while cursor is not None:
            max_value = max(max_value, cursor.element())
            cursor = self.after(cursor)
        return max_value

    def find(self, e):
        if self.is_empty():
            return None
        return self._find(e, self.first())

    def _find(self, e, cursor):
        if cursor is None:
            return None
        if cursor.element() == e:
            return cursor
        return self._find(e, self.after(cursor))

    def move_to_front(self, p):
        original = self._validate(p)

        original._prev._next = original._next
        original._next._prev = original._prev

        original._prev = self._header
        original._next = self._header._next

        self._header._next = original

        print(self._header._element)

    @staticmethod
    def insertion_sort(L):
        if len(L) > 1:
            marker = L.first()
            while marker != L.last():
                pivot = L.after(marker)
                value = pivot.element()
                if value > marker.element():
                    marker = pivot
                else:
                    walk = marker
                    while walk != L.first() and L.before(walk).element() > value:
                        walk = L.before(walk)
                    L.delete(pivot)
                    L.add_before(walk, value)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        position_list = PositionList()

        self.assertEqual(True, position_list.is_empty())

        first = position_list.add_first(1)
        self.assertEqual(1, first.element())

        position_list.add_last(2)
        last = position_list.add_last(3)

        self.assertEqual(False, position_list.is_empty())
        self.assertEqual(3, len(position_list))

        self.assertEqual(3, last.element())

        first = position_list.add_before(first, 0)
        self.assertEqual(4, len(position_list))

        last = position_list.add_after(last, 4)
        self.assertEqual(5, len(position_list))

        seq = [n for n in position_list]
        self.assertEqual([0, 1, 2, 3, 4], seq)

        position_list.delete(first)
        position_list.delete(last)

        seq = [n for n in position_list]
        self.assertEqual([1, 2, 3], seq)

    def test_insertion_sort(self):
        position_list = PositionList()
        position_list.add_last(3)
        position_list.add_last(2)
        position_list.add_last(4)
        position_list.add_last(1)
        position_list.add_last(10)
        position_list.add_last(7)

        seq = [n for n in position_list]
        self.assertEqual([3, 2, 4, 1, 10, 7], seq)

        PositionList.insertion_sort(position_list)

        seq = [n for n in position_list]
        self.assertEqual([1, 2, 3, 4, 7, 10], seq)


if __name__ == '__main__':
    unittest.main()
