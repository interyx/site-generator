import unittest
from src.generator import *
from src.mdutil import *


class TestGenerator(unittest.TestCase):

    def test_paragraph(self):
        text = "This is a block of paragraph text without special formatting."
        result = "<p>This is a block of paragraph text without special formatting.</p>"
        self.assertEqual(result, process_paragraph(text).to_html())

    def test_paragraph_multiple_styles(self):
        text = "This paragraph has **bold** text, inline `code` sections, and some *italics*"
        result = "<p>This paragraph has <b>bold</b> text, inline <code>code</code> sections, and some <i>italics</i></p>"
        self.assertEqual(result, process_paragraph(text).to_html())

    def test_heading(self):
        text = "# This is a level 1 heading"
        result = "<h1>This is a level 1 heading</h1>"
        self.assertEqual(result, process_heading(text).to_html())

    def test_heading_styles(self):
        text = "#### This is a level 4 heading with **bold** text for some reason"
        result = (
            "<h4>This is a level 4 heading with <b>bold</b> text for some reason</h4>"
        )
        self.assertEqual(result, process_heading(text).to_html())

    def test_code_block(self):
        text = """```#include <stdio.h>
int main() {
    print("Hello, world!");
    return 0;
}```"""
        result = '<pre><code>#include <stdio.h>\nint main() {\n    print("Hello, world!");\n    return 0;\n}</code></pre>'
        self.assertEqual(result, process_code(text).to_html())

    def test_quotes(self):
        text = "> America is built on speed.\n> Hot, nasty, badass speed.\n> - Eleanor Roosevelt"
        result = "<blockquote>America is built on speed.\nHot, nasty, badass speed.\n- Eleanor Roosevelt</blockquote>"
        self.assertEqual(result, process_quote(text).to_html())

    def test_unordered_list(self):
        text = "- Frankenstein's Monster\n- Dracula\n- The Mummy\n- The Invisible Man"
        result = "<ul><li>Frankenstein's Monster</li><li>Dracula</li><li>The Mummy</li><li>The Invisible Man</li></ul>"
        self.assertEqual(result, process_unordered_list(text).to_html())

    def test_one_unordered_list(self):
        text = "- Frankenstein"
        result = "<ul><li>Frankenstein</li></ul>"
        self.assertEqual(result, process_unordered_list(text).to_html())

    def test_asterisk_list(self):
        text = "* Dell\n* Alienware\n* Packard-Bell"
        result = "<ul><li>Dell</li><li>Alienware</li><li>Packard-Bell</li></ul>"
        self.assertEqual(result, process_unordered_list(text).to_html())

    def test_ordered_list(self):
        text = "1. Iron Man\n2. Captain America\n3. Incredible Hulk"
        result = (
            "<ol><li>Iron Man</li><li>Captain America</li><li>Incredible Hulk</li></ol>"
        )
        self.assertEqual(result, process_ordered_list(text).to_html())

    def test_markdown_2html_simple(self):
        markdown = "This is a simple paragraph tag"
        result = "<div><p>This is a simple paragraph tag</p></div>"
        self.assertEqual(result, markdown_to_html_node(markdown).to_html())

    def test_markdown_2html_2p(self):
        markdown = "Simple paragraph block\n\nSecond simple paragraph block"
        result = "<div><p>Simple paragraph block</p><p>Second simple paragraph block</p></div>"
        self.assertEqual(result, markdown_to_html_node(markdown).to_html())

    def test_markdown_2html_p_code(self):
        markdown = 'Paragraph block\n\n```print("Hello, World!")```'
        result = '<div><p>Paragraph block</p><pre><code>print("Hello, World!")</code></pre></div>'
        self.assertEqual(result, markdown_to_html_node(markdown).to_html())

    def test_paragraph_quote(self):
        markdown = "Paragraph block\nSecond line of paragraph\n\n> Four score and seven years ago,\n> America ran on Dunkin'"
        result = "<div><p>Paragraph block\nSecond line of paragraph</p><blockquote>Four score and seven years ago,\nAmerica ran on Dunkin'</blockquote></div>"
        self.assertEqual(result, markdown_to_html_node(markdown).to_html())

    def test_quote_list(self):
        markdown = "> What is a man?\n> A miserable little pile of secrets\n\n* Castlevania\n* Castlevania II: Simon's Quest\n* Castlevania III: A Different One"
        result = "<div><blockquote>What is a man?\nA miserable little pile of secrets</blockquote><ul><li>Castlevania</li><li>Castlevania II: Simon's Quest</li><li>Castlevania III: A Different One</li></ul></div>"
        self.assertEqual(result, markdown_to_html_node(markdown).to_html())

    def test_code_ol(self):
        markdown = "```it's some code in a block```\n\n1. A New Hope\n2. Empire Strikes Back\n3. Return of the Jedi"
        result = "<div><pre><code>it's some code in a block</code></pre><ol><li>A New Hope</li><li>Empire Strikes Back</li><li>Return of the Jedi</li></ol></div>"
        self.assertEqual(result, markdown_to_html_node(markdown).to_html())

    def test_heading_paragraph(self):
        markdown = "# Heading 1\n\nParagraph 1"
        result = "<div><h1>Heading 1</h1><p>Paragraph 1</p></div>"
        self.assertEqual(result, markdown_to_html_node(markdown).to_html())

    def test_headings_paragraphs(self):
        markdown = "## Heading 2\n\nParagraph 1\n\n#### Heading 4\n\nParagraph with **bold** and *italic* text"
        result = "<div><h2>Heading 2</h2><p>Paragraph 1</p><h4>Heading 4</h4><p>Paragraph with <b>bold</b> and <i>italic</i> text</p></div>"
        self.assertEqual(result, markdown_to_html_node(markdown).to_html())

    def test_extract_title(self):
        markdown = "# Hello"
        result = "Hello"
        self.assertEqual(result, extract_title(markdown))

    def test_extract_title_multi(self):
        markdown = "## H2\n\n### H3\n\nParagraph\n\n# Hello"
        result = "Hello"
        self.assertEqual(result, extract_title(markdown))

    def test_no_title(self):
        markdown = "Some text\n\n## H2\n\n```code```"
        with self.assertRaises(Exception):
            extract_title(markdown)
