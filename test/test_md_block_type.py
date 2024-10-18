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
