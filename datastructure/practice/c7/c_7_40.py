import unittest
from datastructure.links.FavoritesListMTF import FavoritesListMTF


class MyTestCase(unittest.TestCase):
    def test_something(self):
        favorites = FavoritesListMTF()
        favorites.access('a')
        favorites.access('b')
        favorites.access('c')
        favorites.access('d')
        favorites.access('e')
        favorites.access('f')
        favorites.access('a')
        favorites.access('c')
        favorites.access('f')
        favorites.access('b')
        favorites.access('d')
        favorites.access('e')

        r = [k for k in favorites.top(6)]
        self.assertEqual(['e', 'd', 'b', 'f', 'c', 'a'], r)
        self.assertEqual(6, len(favorites))

        favorites.keeps(3)

        r = [k for k in favorites.top(3)]
        self.assertEqual(3, len(favorites))
        self.assertEqual(['e', 'd', 'b'], r)


if __name__ == '__main__':
    unittest.main()
