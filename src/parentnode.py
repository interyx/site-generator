from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, props=None, children=None):
        super().__init__(tag=tag, value=None, props=props, children=children)
        
    def to_html(self):
        if self.children is None or not isinstance(self.children, list):
            raise ValueError('Parent must have at least one child; children must be a list')
        if self.tag is None:
            raise ValueError('Parent must have a tag')
        html = ""
        props = ""
        for child in self.children:
            html += child.to_html()
        if self.props:
            props = " "
            for k,v in self.props.items():
                props += f'{k}="{v}" '
        return f"<{self.tag}{props.rstrip()}>{html}</{self.tag}>"


