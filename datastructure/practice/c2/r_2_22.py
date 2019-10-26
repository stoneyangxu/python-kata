import unittest
from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, i):
        pass

    def __contains__(self, val):
        for i in range(len(self)):
            if self[i] == val:
                return True
        return False

    def index(self, val):
        for i in range(len(self)):
            if self[i] == val:
                return i
        raise ValueError("value not in sequence")

    def count(self, val):
        k = 0
        for i in range(len(self)):
            if self[i] == val:
                k += 1
        return k

    def __eq__(self, other):
        if len(self) != len(other):
            return False

        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
