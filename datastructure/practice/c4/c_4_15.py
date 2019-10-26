import unittest


def subsets(seq):
    if not seq:
        return [[]]
    subs = subsets(seq[1:])
    return subs + [[seq[0]] + s for s in subs]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = [1, 2, 3]
        print(subsets(s))
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
