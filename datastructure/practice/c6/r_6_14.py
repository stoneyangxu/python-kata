import unittest
from collections import deque
from datastructure.stack_queue.ArrayStack import ArrayStack


def reorder(D):
    stack = ArrayStack()

    stack.push(D.pop())
    stack.push(D.pop())
    stack.push(D.pop())

    D.appendleft(D.pop())

    stack.push(D.pop())

    stack.push(D.popleft())

    stack.push(D.pop())
    stack.push(D.pop())
    stack.push(D.pop())

    while not stack.is_empty():
        D.append(stack.pop())


class MyTestCase(unittest.TestCase):
    def test_something(self):
        D = deque()
        for i in range(1, 9):
            D.append(i)

        reorder(D)

        self.assertEqual([1, 2, 3, 5, 4, 6, 7, 8], [n for n in D])


if __name__ == '__main__':
    unittest.main()
