import unittest
from src.htmlnode import *

class TestHTMLNode(unittest.TestCase):

    def testTag(self):
        paragraph = HTMLNode(tag="p", value="This is a paragraph!")
        self.assertTrue(paragraph.tag == "p")

    def testValue(self):
        paragraph = HTMLNode(tag="p", value="This is a paragraph!")
        self.assertTrue(paragraph.value == "This is a paragraph!")

    def testProps(self):
        props = { "href": "https://www.google.com", "target": "_blank"}
        anchor = HTMLNode(tag="a", props=props)
        self.assertEqual(anchor.props_to_html(), 'href="https://www.google.com" target="_blank"')

