import unittest

from textnode import TextNode
from constants import *
from util import *

class TestSplitImageNode(unittest.TestCase):
    def setUp(self):
        self.singleImageNode = TextNode(
            "This is text with an image ![rick roll](www.imgur.com/rick/roll) and that's all that's in here", TEXT_TYPE_TEXT
        )

    def testSingleImage(self):
        result = [
            TextNode("This is text with an image ", TEXT_TYPE_TEXT),
            TextNode("rick roll", TEXT_TYPE_IMAGE, "www.imgur.com/rick/roll"),
            TextNode(" and that's all that's in here", TEXT_TYPE_TEXT)
        ]
        self.assertEqual(result, split_nodes_image([self.singleImageNode]))

    def testMultipleImages(self):
        node = TextNode(
            "This is text with an image ![rick roll](www.imgur.com/rick/roll) and a picture of ![obi wan](https://handsome.lol) and some extra text to make sure we're splitting properly", TEXT_TYPE_TEXT
        )
        result = [
            TextNode("This is text with an image ", TEXT_TYPE_TEXT),
            TextNode("rick roll", TEXT_TYPE_IMAGE, "www.imgur.com/rick/roll"),
            TextNode(" and a picture of ", TEXT_TYPE_TEXT),
            TextNode("obi wan", TEXT_TYPE_IMAGE, "https://handsome.lol"),
            TextNode(" and some extra text to make sure we're splitting properly", TEXT_TYPE_TEXT)
        ]
        print(f"List of nodes: {split_nodes_image([node])}")
        self.assertEqual(result, split_nodes_image([node]))
