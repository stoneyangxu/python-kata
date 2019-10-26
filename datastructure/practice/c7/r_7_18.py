import unittest
from datastructure.links.FavoritesListMTF import FavoritesListMTF

class MyTestCase(unittest.TestCase):
    def test_something(self):
        favorites = FavoritesListMTF()
        favorites.access("f")
        favorites.access("e")
        favorites.access("d")
        favorites.access("c")
        favorites.access("b")
        favorites.access("a")

        r = [k for k in favorites.top(len(favorites))]
        self.assertEqual(['a', 'b', 'c', 'd', 'e', 'f'], r)

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

        r = [k for k in favorites.top(len(favorites))]
        self.assertEqual(['e', 'd', 'b', 'f', 'c', 'a'], r)



if __name__ == '__main__':
    unittest.main()
