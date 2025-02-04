import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    # the base case : equals get treated equally
    def test_eq(self):                                          
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_none_url(self):
        node = TextNode("text", TextType.BOLD, None)
        node2 = TextNode("text", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_eq_with_empty_text(self):
        node = TextNode("", TextType.BOLD)
        node2 = TextNode("", TextType.BOLD)
        self.assertEqual(node, node2)
# testing standard non-equal nodes
    def test_noteq_diff_typ(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_noteq_diff_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node2", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_noteq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.example.de")
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_noteq_one_url_one_none(self):
        node = TextNode("text", TextType.BOLD, "https://boot.dev")
        node2 = TextNode("text", TextType.BOLD, None)
        self.assertNotEqual(node, node2)
    
# implemented some edge cases with boots to test for realy robust code :)
    def test_eq_long_text(self):
        long_text = "This is a very long text " * 1000  # Creates a 23,000 character string   /// tests also a little the performance
        node = TextNode(long_text, TextType.BOLD)
        node2 = TextNode(long_text, TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_special_chars(self):
        special_text = "Hello 🐻! Contains $pecial #chars@ and émojis" # also a test for internationalization
        node = TextNode(special_text, TextType.BOLD)
        node2 = TextNode(special_text, TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_noteq_none_type(self):
        node = TextNode("text", None)
        node2 = TextNode("text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_noteq_malformed_urls(self):
        node = TextNode("text", TextType.LINK, "https://good.url")
        node2 = TextNode("text", TextType.LINK, "not_a_valid_url")
        self.assertNotEqual(node, node2)

        
if __name__ == "__main__":
    unittest.main()