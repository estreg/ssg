from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum): # Each enum member should have a NAME and a value.
    TEXT = "text"       # This represents normal, plain text
    BOLD = "bold"       # For bold text (usually marked with ** or __ in Markdown)
    ITALIC = "italic"   # For italic text (usually marked with * or _ in Markdown)
    CODE = "code"       # For inline code (usually marked with backticks ` in Markdown)
    LINK = "link"       # For [hyperlinks](like this) in the text
    IMAGE = "image"     # For image references in the text

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text, {})
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text, {})
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text, {})
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text, {})
    elif text_node.text_type == TextType.LINK:
        props = {"href": text_node.url}
        return LeafNode("a", text_node.text, props)
    elif text_node.text_type == TextType.IMAGE:
        props = {"src": text_node.url, "alt": text_node.text} 
        return LeafNode("img", "", props)
    else:
        raise ValueError(f"Invalid text type: {text_node.text_type}")