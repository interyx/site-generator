import unittest
from leafnode import LeafNode
from htmlnode import HTMLNode

class TestLeafNode(unittest.TestCase):

    def testChild(self):
        node = LeafNode("p", "this is a paragraph of text")
        self.assertIsNone(node.children)

    def testTag(self):
        node = LeafNode("p", "This is a paragraph of text")
        result = '<p>This is a paragraph of text</p>'
        self.assertEqual(node.to_html(), result)

    def testNoTag(self):
        node = LeafNode(tag=None, value="I am raw text!", props={"href": "https://www.google.com"})
        result = 'I am raw text!'
        self.assertEqual(node.to_html(), result)

    def testValue(self):
        node = LeafNode(tag = None, value = None, props = None)
        with self.assertRaises(ValueError):
            node.to_html()

    def testProps(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        result = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), result)

if __name__ == '__main__':
    unittest.main()
