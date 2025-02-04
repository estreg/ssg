import unittest
from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):
    def test_create_leaf_node(self):                                            # Test to create basic LeafNode
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, world!")

    def test_leaf_node_no_tag(self):                                            # This test verifies that a LeafNode can be created with no tag (None) but still must have a value.
        node = LeafNode(None, "Text")
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "Text")

    def test_render_no_tag(self):                                               # This test checks that when we call .to_html() on a tagless node, it returns just the value without any HTML tags.
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_render_html(self):                                                 # This test verifies that:
        node = LeafNode("p", "This is a paragraph of text.")                            # The tag is properly wrapped in angle brackets. 
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")         # There's both an opening and closing tag.
                                                                                        # The value appears between the tags
    
    def test_render_html_with_attributes(self):                                 # Like the Test befor only with attributes (props)
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_no_value_raises_error(self):                                       # This test verifies that:
        with self.assertRaises(ValueError): # The with self.assertRaises(ValueError):   # Creating a LeafNode with no value (None).
            node = LeafNode("p", None)      # syntax is how we test that an exception   # Trying to render it with to_html().
            node.to_html()                  # is properly raised.                       # Should raise a ValueError.


if __name__ == "__main__":
    unittest.main()