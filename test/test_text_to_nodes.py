import unittest
from src.textnode import *
from src.util import *
from src.constants import *


class TestTextToTextNodes(unittest.TestCase):

    def test_create_text_node(self):
        text = "this is a regular text node"
        result = [TextNode("this is a regular text node", TEXT_TYPE_TEXT)]
        self.assertEqual(result, text_to_textnodes(text))

    def test_split_bold_node(self):
        text = "this is a **bold** text node"
        result = [
            TextNode("this is a ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(" text node", TEXT_TYPE_TEXT),
        ]
        self.assertEqual(result, text_to_textnodes(text))

    def test_split_italic_bold_node(self):
        text = "this is a **bold** and *italic* text node"
        result = [
            TextNode("this is a ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(" and ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(" text node", TEXT_TYPE_TEXT),
        ]
        self.assertEqual(result, text_to_textnodes(text))

    def test_split_italic_bold_code_node(self):
        text = "this is a **bold**, an *italic*, and some `code`"
        result = [
            TextNode("this is a ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(", an ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(", and some ", TEXT_TYPE_TEXT),
            TextNode("code", TEXT_TYPE_CODE),
        ]
        self.assertEqual(result, text_to_textnodes(text))

    def test_split_delimiters_and_image(self):
        text = "this is a **bold**, an *italic*, a `code block`, and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = [
            TextNode("this is a ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(", an ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(", a ", TEXT_TYPE_TEXT),
            TextNode("code block", TEXT_TYPE_CODE),
            TextNode(", and an ", TEXT_TYPE_TEXT),
            TextNode("obi wan image", TEXT_TYPE_IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(result, text_to_textnodes(text))

    def test_all_splits(self):
        text = "this is a **bold**, an *italic*, a `code block`, an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](www.lolol.io)"
        result = [
            TextNode("this is a ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(", an ", TEXT_TYPE_TEXT),
            TextNode("italic", TEXT_TYPE_ITALIC),
            TextNode(", a ", TEXT_TYPE_TEXT),
            TextNode("code block", TEXT_TYPE_CODE),
            TextNode(", an ", TEXT_TYPE_TEXT),
            TextNode("obi wan image", TEXT_TYPE_IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TEXT_TYPE_TEXT),
            TextNode("link", TEXT_TYPE_LINK, "www.lolol.io")

        ]
        self.assertEqual(result, text_to_textnodes(text))
