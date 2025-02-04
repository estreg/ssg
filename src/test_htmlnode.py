import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):                                          # This tests the simplest case - a single prop. It checks if the method correctly:
    def test_props_to_html_with_href(self):                                     # Adds the leading space and formats the attribute as key="value"
        node = HTMLNode(props={"href": "https://www.boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev"')

    def test_props_to_html_with_multiple_props(self):                           # This tests multiple props. We accept either order
        node = HTMLNode(props={                                                 # because Python dictionaries don't guarantee order. It checks if:
            "href": "https://www.boot.dev",                                     # multiple attributes are separated by spaces, each attribute is correctly formatted
            "target": "_blank"                                                  # leading space is present
        })
        # Note: we could get either order since dictionaries don't maintain order
        # You might want to check if either possible string is correct
        result = node.props_to_html()
        possible1 = ' href="https://www.boot.dev" target="_blank"'
        possible2 = ' target="_blank" href="https://www.boot.dev"'
        self.assertTrue(result == possible1 or result == possible2)
    
    def test_props_to_html_with_none(self):                                     # This tests the case when props is None (default value). It should return an empty string.
        node = HTMLNode()  # props defaults to None
        self.assertEqual(node.props_to_html(), "")

    

if __name__ == "__main__":
    unittest.main()