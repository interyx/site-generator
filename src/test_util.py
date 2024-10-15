import unittest
from util import *
from constants import *
from leafnode import LeafNode
from htmlnode import HTMLNode


class TestSplitNode(unittest.TestCase):
    def test_nodes_list(self):
        node = LeafNode(value="some text")
        with self.assertRaises(ValueError):
            split_nodes_delimiter(node, "`", TEXT_TYPE_CODE)

    def test_pass_other_nodes(self):
        node = LeafNode(value="some text")
        node2 = HTMLNode(value="some text")
        results = [node, node2]
        self.assertTrue(results == split_nodes_delimiter(results, "`", TEXT_TYPE_CODE))

    def test_bold_text_nodes(self):
        node = TextNode("this is **bold** text", TEXT_TYPE_TEXT)
        results = [
            TextNode("this is ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(" text", TEXT_TYPE_TEXT),
        ]
        self.assertTrue(results == split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD))

    def test_italic_text_nodes(self):
        node = TextNode("this is an *italic* text", TEXT_TYPE_TEXT)
        result = [
            TextNode("this is an ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(" text", TEXT_TYPE_TEXT),
        ]
        self.assertTrue(result == split_nodes_delimiter([node], "*", TEXT_TYPE_ITALIC))

    def test_code_text_nodes(self):
        node = TextNode("this is some `code` text", TEXT_TYPE_TEXT)
        result = [
            TextNode("this is some ", TEXT_TYPE_TEXT),
            TextNode("code", TEXT_TYPE_CODE),
            TextNode(" text", TEXT_TYPE_TEXT),
        ]
        self.assertTrue(result == split_nodes_delimiter([node], "`", TEXT_TYPE_CODE))

    def test_multiple_bold_nodes(self):
        node = TextNode(
            "I have **bolded** more than **one** section of text", TEXT_TYPE_TEXT
        )
        result = [
            TextNode("I have ", TEXT_TYPE_TEXT),
            TextNode("bolded", TEXT_TYPE_BOLD),
            TextNode(" more than ", TEXT_TYPE_TEXT),
            TextNode("one", TEXT_TYPE_BOLD),
            TextNode(" section of text", TEXT_TYPE_TEXT),
        ]
        self.assertTrue(result == split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD))

    def test_node_at_end(self):
        node = TextNode("I have written some `code`", TEXT_TYPE_TEXT)
        result = [
            TextNode("I have written some ", TEXT_TYPE_TEXT),
            TextNode("code", TEXT_TYPE_CODE)
        ]
        calc = split_nodes_delimiter([node], '`', TEXT_TYPE_CODE)
        self.assertEqual(result, calc) 


    def test_successive_calls(self):
        node = TextNode("This is a **bold** and an *italic* node", TEXT_TYPE_TEXT)
        result = [
            TextNode("This is a ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(" and an ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(" node", TEXT_TYPE_TEXT),
        ]
        nodes = split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD)
        nodes = split_nodes_delimiter(nodes, "*", TEXT_TYPE_ITALIC)
        self.assertEqual(result, nodes)

    def test_keep_old_node_types(self):
        nodes = [
            TextNode("this is a ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode("node that contains an *italic* string", TEXT_TYPE_TEXT),
        ]
        results = [
            TextNode("this is a ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode("node that contains an ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(" string", TEXT_TYPE_TEXT),
        ]
        self.assertEqual(results, split_nodes_delimiter(nodes, "*", TEXT_TYPE_ITALIC))

    def test_unpaired_nodes(self):
        node = TextNode("This is a **mistake I have made", TEXT_TYPE_TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD)
