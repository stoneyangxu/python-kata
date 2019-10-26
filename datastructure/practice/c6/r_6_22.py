import unittest
from collections import deque


def post_expr(exp):
    number_stack = deque()
    operator_stack = deque()

    chars = list(exp)

    result = []
    sub = []

    for c in chars:
        if c == " " or c == '(':
            continue
        if c == ")":
            sub.append(number_stack.pop())
            sub.append(number_stack.pop())
            sub.append(operator_stack.pop())
            result.append("".join(sub))
            sub.clear()
        elif _is_operator(c):
            operator_stack.append(c)
        else:
            number_stack.append(c)


    return "".join(result)


def _is_operator(c):
    return c in {"+", "-", "*", "/"}


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expr = "((5 + 2) * (8 - 3)) / 4"
        self.assertEqual("52+83-*4/", post_expr(expr))


if __name__ == '__main__':
    unittest.main()
