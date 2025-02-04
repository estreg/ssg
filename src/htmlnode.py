class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join(f' {key}="{value}"' for key, value in self.props.items()) # List comprehension
                                                                                    # numbers = [str(x) for x in range(3)]  # Creates: ['0', '1', '2'] // uses []
                                                                                 # Generator expression
                                                                                    # numbers = (str(x) for x in range(3))  # Creates an iterator      // uses ()
                                                                                    # This translates to: "for each key-value pair in the props dictionary,
                                                                                    # create a string with a space, the key, equals sign, and the quoted value, then join all these strings together."
                                                                                    # the way i learned it "return "".join(map(lambda item: f' {item[0]}="{item[1]}"', self.props.items()))"
        
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props) # "setting the values" isnt necessary, but it helps to read the code for beginners like me.

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf node must have a value")
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node must have a tag")
        if self.children == None:
            raise ValueError("Children is missing a Value")
        return f"<{self.tag}{self.props_to_html()}>{''.join(map(lambda child: child.to_html(), self.children))}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"




    