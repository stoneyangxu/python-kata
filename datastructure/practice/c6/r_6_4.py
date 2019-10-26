import unittest
from datastructure.stack_queue.ArrayStack import ArrayStack


def clear(S):
    if not S.is_empty():
        S.pop()
        clear(S)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        S = ArrayStack()

        S.push(1)
        S.push(2)
        S.push(3)

        clear(S)

        self.assertEqual(True, S.is_empty())


if __name__ == '__main__':
    unittest.main()
