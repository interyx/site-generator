from leafnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case("text"):
            return LeafNode(value=text_node.text)
        case("bold"):
            return LeafNode(value=text_node.text, tag="b")
        case("italic"):
            return LeafNode(value=text_node.text, tag="i")
        case("code"):
            return LeafNode(value=text_node.text, tag="code")
        case("link"):
            return LeafNode(value=text_node.text, tag="a", props={"href": text_node.url})
        case("image"):
            return LeafNode(value="", tag="img", props={"href": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("invalid text type")

