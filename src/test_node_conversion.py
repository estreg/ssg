import unittest

from textnode import TextNode, TextType
from htmlnode import LeafNode
from textnode import text_node_to_html_node

class TestNodeConversion(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text")
        self.assertEqual(html_node.props, {})

    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
        self.assertEqual(html_node.props, {})

    def test_text_node_to_html_node_italic(self):
        node = TextNode("This is italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic")
        self.assertEqual(html_node.props, {})

    def test_text_node_to_html_node_code(self):
        node = TextNode("This is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")
        self.assertEqual(html_node.props, {})

    def test_text_node_to_html_node_link(self):
        node = TextNode("Click me", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})

    def test_text_node_to_html_node_image(self):
        node = TextNode("alt text", TextType.IMAGE, "https://boot.dev/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {
            "src": "https://boot.dev/image.png",
            "alt": "alt text"
        })

if __name__ == "__main__":
    unittest.main()