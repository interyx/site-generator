import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_ineq(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_none(self):
        node = TextNode("this is a text node", "bold")
        self.assertIsNone(node.url)

    def test_url(self):
        node = TextNode("this is a text node", "bold", "http://www.twitch.tv")
        self.assertIsNotNone(node.url)


if __name__ == "__main__":
    unittest.main()
