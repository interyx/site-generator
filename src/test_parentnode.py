import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def setUp(self):
        self.testParent = ParentNode(tag="a", props={"href": "google.com"}, children = [
            LeafNode("p", "A paragraph"),
            LeafNode("b", "bold text")])
        self.children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Normal text"),
        ]

    def testNoValue(self):
        """Ensure the ParentNode's `value` field is None"""
        node = ParentNode(tag="p", props=None, children=self.children)
        self.assertIsNone(node.value)

    def testHasChildren(self):
        """Ensure the ParentNode has children (even if the list is empty)"""
        node = ParentNode(tag="p", props=None, children=None)
        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertTrue('Parent must have at least one child; children must be a list' in str(context.exception))

    def testChildrenIsList(self):
        """Ensure the Children attribute is a list"""
        node = ParentNode(tag="p", props=None, children=self.children[0])
        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertTrue('Parent must have at least one child; children must be a list' in str(context.exception))

    def testHasTag(self):
        """Parent must have a tag"""
        node = ParentNode(tag=None, props=None, children=self.children)
        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertTrue('Parent must have a tag' in str(context.exception))

    def testSingleChild(self):
        node = ParentNode(tag="p", props=None, children=[self.children[0]])
        test = "<p><b>Bold text</b></p>"
        self.assertEqual(node.to_html(), test)

    def testMultipleChildren(self):
        node = ParentNode(tag="p", props=None, children=self.children)
        test = "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), test)

    def testNestedParents(self):
        node = ParentNode(tag="p", props=None, children=self.children)
        node.children.append(self.testParent)
        test = '<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text<a href="google.com"><p>A paragraph</p><b>bold text</b></a></p>'
        self.assertEqual(node.to_html(), test)
