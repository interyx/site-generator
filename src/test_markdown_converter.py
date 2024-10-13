import unittest

from util import *

class TestMarkdownConverter(unittest.TestCase):
    
    def test_single_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(result, extract_markdown_images(text))

    def test_multiple_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(result, extract_markdown_images(text))

    def test_mixed_link_image(self):
        text = "It's got a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and a link [to boot dev](https://www.youtube.com/@bootdotdev)"
        link_result = [
            ("to boot dev", "https://www.youtube.com/@bootdotdev")
        ]
        image_result = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif")
        ]
        self.assertEqual(link_result, extract_markdown_links(text))
        self.assertEqual(image_result, extract_markdown_images(text))


    def test_multiple_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)" 
        result = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(result, extract_markdown_links(text))
