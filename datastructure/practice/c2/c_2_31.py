import unittest
from datastructure.oop.progression.test_progression import Progression


class AbsProgression(Progression):
    def __init__(self, first=0, second=0):
        super().__init__(first)
        self._prev = first + second

    def _advance(self):
        self._prev, self._current = self._current, abs(self._prev - self._current)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p = AbsProgression(2, 200)
        l = [next(p) for i in range(5)]
        self.assertEqual([2, 200, 198, 2, 196], l)


if __name__ == '__main__':
    unittest.main()
