import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_create_parent_node(self):                                            # Test to create basic ParentNode
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text")
        ]
        node = ParentNode("p", children)
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.children, children)
    
    def test_parent_node_to_html(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text")
        ]
        node = ParentNode("p", children)
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text</p>"
        )

    def test_none_tag_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "text")]).to_html()

    def test_none_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None).to_html()
    
    def test_nested_parent_nodes(self):
        # Test parent nodes nested inside other parent nodes
        inner_node = ParentNode("div", [
            LeafNode("span", "Inner text")
        ])
        outer_node = ParentNode("section", [
            LeafNode("p", "First paragraph"),
            inner_node,
            LeafNode("p", "Last paragraph")
        ])
        self.assertEqual(
            outer_node.to_html(),
            "<section><p>First paragraph</p><div><span>Inner text</span></div><p>Last paragraph</p></section>"
        )

    def test_parent_node_with_props(self):
        # Test parent nodes with properties
        node = ParentNode(
            "div",
            [LeafNode("p", "Hello")],
            {"class": "greeting", "id": "welcome"}
        )
        self.assertEqual(
            node.to_html(),
            '<div class="greeting" id="welcome"><p>Hello</p></div>'
        )

    def test_multiple_children(self):
        # Test parent node with multiple children
        node = ParentNode("div", [
            LeafNode("p", "First"),
            LeafNode("p", "Second"),
            LeafNode("p", "Third"),
            LeafNode(None, "Raw text"),
            LeafNode("span", "Last")
        ])
        self.assertEqual(
            node.to_html(),
            "<div><p>First</p><p>Second</p><p>Third</p>Raw text<span>Last</span></div>"
        )

def test_deeply_nested_structure(self):
    # Test a more complex nested structure
    node = ParentNode("div", [
        ParentNode("header", [
            LeafNode("h1", "Title")
        ]),
        ParentNode("main", [
            ParentNode("article", [
                LeafNode("h2", "Article heading"),
                LeafNode("p", "Article content")
            ])
        ])
    ])
    self.assertEqual(
        node.to_html(),
        "<div><header><h1>Title</h1></header><main><article><h2>Article heading</h2><p>Article content</p></article></main></div>"
    )