import unittest
from src.generator import *

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
        text = "This is a level 1 heading"
        result = "<h1>This is a level 1 heading</h1>"
        self.assertEqual(result, process_heading(text, 1).to_html())

    def test_heading_styles(self):
        text = "This is a level 4 heading with **bold** text for some reason"
        result = "<h4>This is a level 4 heading with <b>bold</b> text for some reason</h4>"
        self.assertEqual(result, process_heading(text, 4).to_html())

    def test_code_block(self):
        text = """```#include <stdio.h>
int main() {
    print("Hello, world!");
    return 0;
}```"""
        result = "<pre><code>#include <stdio.h>\nint main() {\n    print(\"Hello, world!\");\n    return 0;\n}</code></pre>"
        self.assertEqual(result, process_code(text).to_html())

    def test_quotes(self):
        text="> America is built on speed.\n> Hot, nasty, badass speed.\n> - Eleanor Roosevelt"
        result = "<blockquote>America is built on speed.\nHot, nasty, badass speed.\n- Eleanor Roosevelt</blockquote>"
        self.assertEqual(result, process_quote(text).to_html())

    def test_unordered_list(self):
        text = "- Frankenstein's Monster\n- Dracula\n- The Mummy\n- The Invisible Man"
        result="<ul><li>Frankenstein's Monster</li><li>Dracula</li><li>The Mummy</li><li>The Invisible Man</li></ul>"
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
        result = "<ol><li>Iron Man</li><li>Captain America</li><li>Incredible Hulk</li></ol>"
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
        markdown = "Paragraph block\n\n```print(\"Hello, World!\")```"
        result = "<div><p>Paragraph block</p><pre><code>print(\"Hello, World!\")</code></pre></div>"
        self.assertEqual(result, markdown_to_html_node(markdown).to_html())
