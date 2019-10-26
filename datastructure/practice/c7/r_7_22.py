import unittest
from datastructure.links.FavoritesList import FavoritesList

class MyTestCase(unittest.TestCase):
    def test_something(self):
        favorites_list = FavoritesList()
        favorites_list.access("a")
        favorites_list.access("b")
        favorites_list.access("c")

        self.assertEqual(3, len(favorites_list))

        favorites_list.clear()
        self.assertEqual(0, len(favorites_list))



if __name__ == '__main__':
    unittest.main()
