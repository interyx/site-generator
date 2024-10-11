from leafnode import LeafNode
from textnode import TextNode
from constants import *

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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    results = []
    if not isinstance(old_nodes, list):
        raise ValueError("List of nodes required")

    for node in old_nodes:
        if not isinstance(node, TextNode):
            results.append(node)
            continue
        split_tokens = node.text.split(delimiter)
        if len(split_tokens) % 2 == 0:
            raise ValueError("Unpaired formatting token detected.  Markdown requires your delimiter (*, **, `) be around the **entire** section of text to be bolded.")
        for index, node in enumerate(split_tokens):
            if index % 2 == 0:
                results.append(TextNode(split_tokens[index], TEXT_TYPE_TEXT))
            else:
                results.append(TextNode(split_tokens[index], text_type))

    return results
