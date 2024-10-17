import unittest
from src.util import *


class TestMarkdownBlocks(unittest.TestCase):

    def test_single_block(self):
        text = "# This is a heading"
        result = ["# This is a heading"]
        self.assertEqual(result, markdown_to_blocks(text))

    def test_two_blocks(self):
        text = "# This is a heading\n\nThis is a paragraph of text.  It has some **bold** and *italic* words in it."
        result = [
            "# This is a heading",
            "This is a paragraph of text.  It has some **bold** and *italic* words in it."
        ]
        self.assertEqual(result, markdown_to_blocks(text))

    def test_three_blocks(self):
        text = "# This is a heading\n\nThis is a paragraph of text with **bold** and *italics*\n\n* This is the first list item in a list block\n* This is the second list item\n* This is the third list item"
        result = [
            "# This is a heading",
            "This is a paragraph of text with **bold** and *italics*",
            "* This is the first list item in a list block\n* This is the second list item\n* This is the third list item"
        ]
        self.assertEqual(result, markdown_to_blocks(text))

    def test_strip_space(self):
        text = " # This is a heading \n\nThis is a paragraph of text with **bold** and *italic* \n\n I'm a little teapot, short and stout "
        result = [
            "# This is a heading",
            "This is a paragraph of text with **bold** and *italic*",
            "I'm a little teapot, short and stout"
        ]
        self.assertEqual(result, markdown_to_blocks(text))

    def test_strip_extra_blocks(self):
        text = "# Heading 1\n\n\n# Heading 2\n\nTeapot"
        result = [
            "# Heading 1",
            "# Heading 2",
            "Teapot"
        ]
        self.assertEqual(result, markdown_to_blocks(text))
