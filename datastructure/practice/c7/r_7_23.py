import unittest
from datastructure.links.FavoritesList import FavoritesList


class MyTestCase(unittest.TestCase):
    def test_something(self):
        favorites_list = FavoritesList()
        favorites_list.access("a")
        favorites_list.access("b")
        favorites_list.access("c")

        r = [n for n in favorites_list.top_count(3)]
        self.assertEqual([1, 1, 1], r)

        favorites_list.reset_counts()
        r = [n for n in favorites_list.top_count(3)]
        self.assertEqual([0, 0, 0], r)


if __name__ == '__main__':
    unittest.main()
