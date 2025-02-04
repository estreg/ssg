import unittest

from markdown_to_html import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from block_markdown import markdown_to_blocks, block_to_block_type

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ordlist = "ordered_list"
block_type_unordlist = "unordered_list"

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html_node(self):
        assert markdown_to_html_node("This is a paragraph").to_html() == "<div><p>This is a paragraph</p></div>"
   
        # Heading with different levels
        assert markdown_to_html_node("# Heading 1").to_html() == "<div><h1>Heading 1</h1></div>"
        assert markdown_to_html_node("## Heading 2").to_html() == "<div><h2>Heading 2</h2></div>"
        
        # Block quote
        assert markdown_to_html_node("> This is a quote").to_html() == "<div><blockquote>This is a quote</blockquote></div>"
        
        # Unordered list
        assert markdown_to_html_node("* List item").to_html() == "<div><ul><li>List item</li></ul></div>"
        
        # Ordered list
        assert markdown_to_html_node("1. First item").to_html() == "<div><ol><li>First item</li></ol></div>"
        
        # Multiple blocks
        multi_block = "# Header\n\nThis is a paragraph"
        expected_multi = "<div><h1>Header</h1><p>This is a paragraph</p></div>"
        assert markdown_to_html_node(multi_block).to_html() == expected_multi
    
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
    



if __name__ == "__main__":
    unittest.main()