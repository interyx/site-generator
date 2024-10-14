import unittest

from textnode import TextNode
from constants import *
from util import *


class TestSplitImageNode(unittest.TestCase):
    def setUp(self):
        self.singleImageNode = TextNode(
            "This is text with an image ![rick roll](www.imgur.com/rick/roll) and that's all that's in here",
            TEXT_TYPE_TEXT,
        )
        self.multi_image_node = TextNode(
            "This is text with an image ![rick roll](www.imgur.com/rick/roll) and a picture of ![obi wan](https://handsome.lol) and some extra text to make sure we're splitting properly",
            TEXT_TYPE_TEXT,
        )
        self.null_image_node = TextNode(
            "This text doesn't have any links in it", TEXT_TYPE_TEXT
        )
        self.mixed_node = TextNode(
            "This is text with an image ![rick roll](www.imgur.com/rick/roll) and a link to [a website](www.a-website.com) and some extra text",
            TEXT_TYPE_TEXT,
        )

    def test_single_image(self):
        result = [
            TextNode("This is text with an image ", TEXT_TYPE_TEXT),
            TextNode("rick roll", TEXT_TYPE_IMAGE, "www.imgur.com/rick/roll"),
            TextNode(" and that's all that's in here", TEXT_TYPE_TEXT),
        ]
        self.assertEqual(result, split_nodes_image([self.singleImageNode]))

    def test_multiple_images(self):
        result = [
            TextNode("This is text with an image ", TEXT_TYPE_TEXT),
            TextNode("rick roll", TEXT_TYPE_IMAGE, "www.imgur.com/rick/roll"),
            TextNode(" and a picture of ", TEXT_TYPE_TEXT),
            TextNode("obi wan", TEXT_TYPE_IMAGE, "https://handsome.lol"),
            TextNode(
                " and some extra text to make sure we're splitting properly",
                TEXT_TYPE_TEXT,
            ),
        ]
        self.assertEqual(result, split_nodes_image([self.multi_image_node]))

    def test_mixed_node(self):

        result = [
            TextNode("This is text with an image ", TEXT_TYPE_TEXT),
            TextNode("rick roll", TEXT_TYPE_IMAGE, "www.imgur.com/rick/roll"),
            TextNode(
                " and a link to [a website](www.a-website.com) and some extra text",
                TEXT_TYPE_TEXT,
            ),
        ]
        self.assertEqual(result, split_nodes_image([self.mixed_node]))

    def test_null_node(self):
        result = [TextNode("This text doesn't have any links in it", TEXT_TYPE_TEXT)]
        self.assertEqual(result, split_nodes_image([self.null_image_node]))
