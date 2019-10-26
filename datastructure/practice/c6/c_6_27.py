import unittest
from datastructure.stack_queue.ArrayStack import ArrayStack
from datastructure.stack_queue.ArrayQueue import ArrayQueue


def find_x(S, Q, x):
    if len(S) == 0:
        return []
    r = S.pop()
    while r != x and not S.is_empty():
        Q.enqueue(r)
        r = S.pop()
    if r != x:
        return []
    else:
        result = []
        while len(Q) != 0:
            result.append(Q.dequeue())
        result.append(x)
        return result


class MyTestCase(unittest.TestCase):
    def test_find(self):
        S = ArrayStack()
        S.push(1)
        S.push(2)
        S.push(3)
        S.push(4)
        S.push(5)

        Q = ArrayQueue()

        self.assertEqual([5, 4], find_x(S, Q, 4))

    def test_not_find(self):
        S = ArrayStack()
        S.push(1)
        S.push(2)
        S.push(3)
        S.push(4)
        S.push(5)

        Q = ArrayQueue()

        self.assertEqual([], find_x(S, Q, 6))


if __name__ == '__main__':
    unittest.main()
