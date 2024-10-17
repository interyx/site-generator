import unittest

from src.textnode import TextNode
from src.constants import *
from src.util import *


class TestSplitLinkNode(unittest.TestCase):
    def setUp(self):
        self.single_link_node = TextNode(
            "This is text with a link [rick roll](www.imgur.com/rick/roll) and that's all that's in here",
            TEXT_TYPE_TEXT,
        )
        self.multi_link_node = TextNode(
            "This is text with a link [rick roll](www.imgur.com/rick/roll) and a link to [obi wan](https://handsome.lol) and some extra text to make sure we're splitting properly",
            TEXT_TYPE_TEXT,
        )
        self.null_link_node = TextNode(
            "This text doesn't have any links in it", TEXT_TYPE_TEXT
        )
        self.mixed_node = TextNode(
            "This is text with an image ![rick roll](www.imgur.com/rick/roll) and a link to [a website](www.a-website.com) and some extra text",
            TEXT_TYPE_TEXT,
        )

    def test_single_link(self):
        result = [
            TextNode("This is text with a link ", TEXT_TYPE_TEXT),
            TextNode("rick roll", TEXT_TYPE_LINK, "www.imgur.com/rick/roll"),
            TextNode(" and that's all that's in here", TEXT_TYPE_TEXT),
        ]
        self.assertEqual(result, split_nodes_link([self.single_link_node]))

    def test_multiple_links(self):
        result = [
            TextNode("This is text with a link ", TEXT_TYPE_TEXT),
            TextNode("rick roll", TEXT_TYPE_LINK, "www.imgur.com/rick/roll"),
            TextNode(" and a link to ", TEXT_TYPE_TEXT),
            TextNode("obi wan", TEXT_TYPE_LINK, "https://handsome.lol"),
            TextNode(
                " and some extra text to make sure we're splitting properly",
                TEXT_TYPE_TEXT,
            ),
        ]
        self.assertEqual(result, split_nodes_link([self.multi_link_node]))

    def test_mixed_node(self):
        result = [
            TextNode(
                "This is text with an image ![rick roll](www.imgur.com/rick/roll) and a link to ",
                TEXT_TYPE_TEXT,
            ),
            TextNode("a website", TEXT_TYPE_LINK, "www.a-website.com"),
            TextNode(" and some extra text", TEXT_TYPE_TEXT),
        ]
        self.assertEqual(result, split_nodes_link([self.mixed_node]))

    def test_null_node(self):
        result = [TextNode("This text doesn't have any links in it", TEXT_TYPE_TEXT)]
        self.assertEqual(result, split_nodes_link([self.null_link_node]))
