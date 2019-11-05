import unittest
from datastructure.tree.LinkedBinaryTree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    def __init__(self, token, left=None, right=None):
        super().__init__()
        if not isinstance(token, str):
            raise TypeError("Token must be a string")
        self._add_root(token)
        if left is not None:
            if token not in "+-*/":
                raise ValueError("token must be valid operator")
            self._attach(self.root(), left, right)

    def __str__(self):
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return "".join(pieces)

    def _parenthesize_recur(self, p, result):
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append("(")
            self._parenthesize_recur(self.left(p), result)
            result.append(str(p.element()))
            self._parenthesize_recur(self.right(p), result)
            result.append(")")

    def evaluate(self):
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        if self.is_leaf(p):
            return float(p.element())
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '*':
                return left_val * right_val
            else:
                return left_val / right_val

    @staticmethod
    def build_expression_tree(tokens):
        S = []
        for t in tokens:
            if t == ' ':
                continue
            elif t in '+-*/':
                S.append(t)
            elif t not in '()':
                S.append(ExpressionTree(t))
            elif t == ')':
                right = S.pop()
                op = S.pop()
                left = S.pop()
                S.append(ExpressionTree(op, left, right))
        return S.pop()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expression_tree = ExpressionTree.build_expression_tree("(((3 + 1) * 4) / ((9 - 5) + 2))")
        self.assertEqual((((3 + 1) * 4) / ((9 - 5) + 2)), expression_tree.evaluate())


if __name__ == '__main__':
    unittest.main()
