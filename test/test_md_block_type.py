import unittest

from src.mdutil import *
from src.constants import *

class TestMDBlocks(unittest.TestCase):
    def test_h1(self):
        text = "# This is a heading"
        self.assertEqual(MD_TYPE_H, block_to_block_type(text))

    def test_h6(self):
        text = "###### This is a heading"
        self.assertEqual(MD_TYPE_H, block_to_block_type(text))

    def test_h7(self):
        text = "####### This is a heading"
        self.assertEqual(MD_TYPE_P, block_to_block_type(text))

    def test_codeblock(self):
        text = "```This is a code block```"
        self.assertEqual(MD_TYPE_CODE, block_to_block_type(text))

    def test_codeblock_wrong1(self):
        text = "``This is a code block```"
        self.assertEqual(MD_TYPE_P, block_to_block_type(text))

    def test_codeblock_wrong2(self):
        text = "```This is a code block``"
        self.assertEqual(MD_TYPE_P, block_to_block_type(text))

    def test_quote(self):
        text = "> I'm a quote"
        self.assertEqual(MD_TYPE_QUOTE, block_to_block_type(text))

    def test_quote_wrong1(self):
        text = "> I'm a quote\nBut I'm invalid markdown"
        self.assertEqual(MD_TYPE_P, block_to_block_type(text))

    def test_three_quotes(self):
        text = "> I'm a quote\n> Second quote line\n> Third quote line"
        self.assertEqual(MD_TYPE_QUOTE, block_to_block_type(text))

    def test_ul_one_item(self):
        text = "* I'm a list with one line"
        self.assertEqual(MD_TYPE_UL, block_to_block_type(text))

    def test_ul_one_item_wrong(self):
        text = "*I'm a list but I'm written wrong"
        self.assertEqual(MD_TYPE_P, block_to_block_type(text))

    def test_unordered_list(self):
        text = "* I'm a valid list\n* I have asterisks and a space"
        self.assertEqual(MD_TYPE_UL, block_to_block_type(text))
        
    def test_ul_second_line(self):
        text = "* I'm a valid list\nBut the second line is wrong"
        self.assertEqual(MD_TYPE_P, block_to_block_type(text))

    def test_ul_dash(self):
        text = "- I'm a valid list"
        self.assertEqual(MD_TYPE_UL, block_to_block_type(text))

    def test_ul_dash_wrong(self):
        text = "-I'm an invalid list"
        self.assertEqual(MD_TYPE_P, block_to_block_type(text))

    def test_two_dash_ul(self):
        text = "- I'm a valid list\nBut I have a second wrong item"
        self.assertEqual(MD_TYPE_P, block_to_block_type(text))

    def test_two_dash_ul_correct(self):
        text = "- I'm a valid list\n- With a second valid item"
        self.assertEqual(MD_TYPE_UL, block_to_block_type(text))

    def test_ordered_list(self):
        text = "1. I'm the first item in a list"
        self.assertEqual(MD_TYPE_OL, block_to_block_type(text))

    def test_ordered_list_wrong_format(self):
        text = "1. I'm the first item in a list\n2 I'm the second list item"
        self.assertEqual(MD_TYPE_P, block_to_block_type(text))

    def test_ordered_list_wrong_order(self):
        text = "1. I'm the first item\n3. I'm the second item\n2. I'm the third item"
        self.assertEqual(MD_TYPE_P, block_to_block_type(text))

    def test_ordered_list_correct_order(self):
        text = "1. One\n2. Two\n3. Three"
        self.assertEqual(MD_TYPE_OL, block_to_block_type(text))
