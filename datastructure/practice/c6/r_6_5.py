import unittest
from datastructure.stack_queue.ArrayStack import ArrayStack


def reverse(seq):
    stack = ArrayStack()
    for n in seq:
        stack.push(n)
    result = []
    while not stack.is_empty():
        result.append(stack.pop())
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        seq = [1, 2, 3]
        self.assertEqual([3, 2, 1], reverse(seq))


if __name__ == '__main__':
    unittest.main()
