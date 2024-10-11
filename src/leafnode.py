from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        result = self.value
        props = ""
        if self.props and self.tag:
            props += super().props_to_html()
            result = f"<{self.tag} {props}>{result}</{self.tag}>"
        elif self.tag and not self.props:
            result = f"<{self.tag}>{result}</{self.tag}>"
        return result


