import unittest
import math
from datastructure.oop.progression.test_progression import Progression

class SqrtProgression(Progression):
    def __init__(self, start=0):
        super().__init__(start)

    def _advance(self):
        self._current = math.sqrt(self._current)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p = SqrtProgression(65536)
        l = [next(p) for i in range(6)]
        self.assertEqual([65536, 256, 16, 4, 2, math.sqrt(2)], l)


if __name__ == '__main__':
    unittest.main()
