import unittest
from datastructure.stack_queue.ArrayStack import ArrayStack


def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())


class MyTestCase(unittest.TestCase):
    def test_something(self):
        S = ArrayStack()
        T = ArrayStack()

        S.push(1)
        S.push(2)
        S.push(3)

        transfer(S, T)

        self.assertEqual(1, T.pop())
        self.assertEqual(2, T.pop())
        self.assertEqual(3, T.pop())


if __name__ == '__main__':
    unittest.main()
