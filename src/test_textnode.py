import unittest

from textnode import *
from leafnode import LeafNode

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

    def test_convert_text_type_text(self):
        node = TextNode("this is a text node", "text")
        test_result = LeafNode(value="this is a text node").to_html()
        value = text_node_to_html_node(node).to_html()
        self.assertEqual(test_result, value)

    def test_convert_text_type_bold(self):
        node = TextNode("this is a text node", "bold")
        test_result = LeafNode(value="this is a text node", tag="b").to_html()
        value = text_node_to_html_node(node).to_html()
        self.assertEqual(test_result, value)

    def test_convert_text_type_italic(self):
        node = TextNode("this is an italic node", "italic")
        test_result = LeafNode(value="this is an italic node", tag="i").to_html()
        value = text_node_to_html_node(node).to_html()
        self.assertEqual(test_result, value)

    def test_convert_text_type_code(self):
        node = TextNode("this is a code node", "code")
        test_result = LeafNode(value="this is a code node", tag="code").to_html()
        value = text_node_to_html_node(node).to_html()
        self.assertEqual(test_result, value)

    def test_convert_text_type_link(self):
        node = TextNode("google.com", "link", "http://www.google.com")
        test_result = LeafNode(value="google.com", tag="a", props={"href": "http://www.google.com"}).to_html()
        value = text_node_to_html_node(node).to_html()
        self.assertEqual(test_result, value)

    def test_convert_text_type_image(self):
        node = TextNode("a picture of a swan", "image", "http://tumblr.com/100")
        test_result = LeafNode(value="", tag="img", props={"href": "http://tumblr.com/100", "alt": "a picture of a swan"}).to_html()
        value = text_node_to_html_node(node).to_html()
        self.assertEqual(test_result, value)

    def test_convert_text_type_other(self):
        node = TextNode("some kind of nonsense", "strong")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()
