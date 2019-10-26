import unittest
from datastructure.stack_queue.ArrayStack import ArrayStack


def is_matched_html(raw):
    S = ArrayStack()
    j = raw.find("<")
    while j != -1:
        k = raw.find(">", j + 1)
        if k == -1:
            return False
        tag = raw[j + 1:k]
        if not tag.startswith("/"):
            if " " in tag:
                S.push(tag[:tag.find(" ")])
            else:
                S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find("<", k + 1)
    return True


class MyTestCase(unittest.TestCase):
    def test_something(self):
        raw = """
            <html>
                <body>
                    <h1>Title</h1>
                    <h2 style="display: none">Content</h2>
                </body>
            </html>
        """

        self.assertEqual(True, is_matched_html(raw))


if __name__ == '__main__':
    unittest.main()
