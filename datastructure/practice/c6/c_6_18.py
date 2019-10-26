import unittest
from datastructure.stack_queue.ArrayStack import ArrayStack


def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())


class MyTestCase(unittest.TestCase):
    def test_something(self):
        S = ArrayStack()
        S.push(1)
        S.push(2)
        S.push(3)

        temp1 = ArrayStack()
        temp2 = ArrayStack()


        transfer(S, temp1)
        transfer(temp1, temp2)
        transfer(temp2, S)

        self.assertEqual(1, S.pop())
        self.assertEqual(2, S.pop())
        self.assertEqual(3, S.pop())


if __name__ == '__main__':
    unittest.main()
