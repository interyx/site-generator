import unittest
from textnode import *
from leafnode import LeafNode
from util import *
from constants import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TEXT_TYPE_BOLD)
        node2 = TextNode("This is a text node", TEXT_TYPE_BOLD)
        self.assertEqual(node, node2)

    def test_ineq(self):
        node = TextNode("This is a text node", TEXT_TYPE_ITALIC)
        node2 = TextNode("This is a text node", TEXT_TYPE_BOLD)
        self.assertNotEqual(node, node2)

    def test_none(self):
        node = TextNode("this is a text node", TEXT_TYPE_BOLD)
        self.assertIsNone(node.url)

    def test_url(self):
        node = TextNode("this is a text node", TEXT_TYPE_BOLD, "http://www.twitch.tv")
        self.assertIsNotNone(node.url)

    def test_convert_text_type_text(self):
        node = TextNode("this is a text node", TEXT_TYPE_TEXT)
        test_result = LeafNode(value="this is a text node").to_html()
        value = text_node_to_html_node(node).to_html()
        self.assertEqual(test_result, value)

    def test_convert_text_type_bold(self):
        node = TextNode("this is a text node", TEXT_TYPE_BOLD)
        test_result = LeafNode(value="this is a text node", tag="b").to_html()
        value = text_node_to_html_node(node).to_html()
        self.assertEqual(test_result, value)

    def test_convert_text_type_italic(self):
        node = TextNode("this is an italic node", TEXT_TYPE_ITALIC)
        test_result = LeafNode(value="this is an italic node", tag="i").to_html()
        value = text_node_to_html_node(node).to_html()
        self.assertEqual(test_result, value)

    def test_convert_text_type_code(self):
        node = TextNode("this is a code node", TEXT_TYPE_CODE)
        test_result = LeafNode(value="this is a code node", tag="code").to_html()
        value = text_node_to_html_node(node).to_html()
        self.assertEqual(test_result, value)

    def test_convert_text_type_link(self):
        node = TextNode("google.com", TEXT_TYPE_LINK, "http://www.google.com")
        test_result = LeafNode(value="google.com", tag="a", props={"href": "http://www.google.com"}).to_html()
        value = text_node_to_html_node(node).to_html()
        self.assertEqual(test_result, value)

    def test_convert_text_type_image(self):
        node = TextNode("a picture of a swan", TEXT_TYPE_IMAGE, "http://tumblr.com/100")
        test_result = LeafNode(value="", tag="img", props={"href": "http://tumblr.com/100", "alt": "a picture of a swan"}).to_html()
        value = text_node_to_html_node(node).to_html()
        self.assertEqual(test_result, value)

    def test_convert_text_type_other(self):
        node = TextNode("some kind of nonsense", "strong")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

