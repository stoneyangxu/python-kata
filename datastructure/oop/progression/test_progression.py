import unittest
from abc import ABC, abstractmethod


class Progression(ABC):

    def __init__(self, start=0):
        self._current = start

    @abstractmethod
    def _advance(self):
        pass

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def str(self, n):
        return " ".join(str(next(self)) for i in range(n))


class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment


class GeometricProgression(Progression):

    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base


class FibonacciProgression(Progression):

    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current


class MyTestCase(unittest.TestCase):
    def test_arithmetic_progression(self):
        progression = ArithmeticProgression()
        self.assertEqual(progression.str(5), "0 1 2 3 4")

        progression = ArithmeticProgression(2)
        self.assertEqual(progression.str(5), "0 2 4 6 8")

        progression = ArithmeticProgression(2, 3)
        self.assertEqual(progression.str(5), "3 5 7 9 11")

    def test_geometric_progression(self):
        progression = GeometricProgression()
        self.assertEqual(progression.str(5), "1 2 4 8 16")

        progression = GeometricProgression(3)
        self.assertEqual(progression.str(5), "1 3 9 27 81")

        progression = GeometricProgression(2, 3)
        self.assertEqual(progression.str(5), "3 6 12 24 48")

    def test_fibonacci_progression(self):
        progression = FibonacciProgression()
        self.assertEqual(progression.str(5), "0 1 1 2 3")

        progression = FibonacciProgression(3)
        self.assertEqual(progression.str(5), "3 1 4 5 9")

        progression = FibonacciProgression(2, 3)
        self.assertEqual(progression.str(5), "2 3 5 8 13")


if __name__ == '__main__':
    unittest.main()
