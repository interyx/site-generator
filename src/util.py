from leafnode import LeafNode
from textnode import TextNode
from constants import *
import re


def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case "text":
            return LeafNode(value=text_node.text)
        case "bold":
            return LeafNode(value=text_node.text, tag="b")
        case "italic":
            return LeafNode(value=text_node.text, tag="i")
        case "code":
            return LeafNode(value=text_node.text, tag="code")
        case "link":
            return LeafNode(
                value=text_node.text, tag="a", props={"href": text_node.url}
            )
        case "image":
            return LeafNode(
                value="",
                tag="img",
                props={"href": text_node.url, "alt": text_node.text},
            )
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
            raise ValueError(
                "Unpaired formatting token detected.  Markdown requires your delimiter (*, **, `) be around the **entire** section of text to be bolded."
            )
        for index, node in enumerate(split_tokens):
            if index % 2 == 0:
                results.append(TextNode(split_tokens[index], TEXT_TYPE_TEXT))
            else:
                results.append(TextNode(split_tokens[index], text_type))

    return results


def extract_markdown_images(text):
    image = re.findall(r"!\[(.*?)]\((.*?)\)", text)
    return image


def extract_markdown_links(text):
    link = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return link


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        text = node.text
        if not images:
            new_nodes.append(node)
            continue
        for image in images:
            sections = text.split(f"![{image[0]}]({image[1]})", 1)
            new_nodes.append(TextNode(sections[0], TEXT_TYPE_TEXT))
            new_nodes.append(TextNode(image[0], TEXT_TYPE_IMAGE, image[1]))
            text = sections[1]
        if text:
            new_nodes.append(TextNode(text, TEXT_TYPE_TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        text = node.text
        if not links:
            new_nodes.append(node)
            continue
        for link in links:
            sections = text.split(f"[{link[0]}]({link[1]})", 1)
            new_nodes.append(TextNode(sections[0], TEXT_TYPE_TEXT))
            new_nodes.append(TextNode(link[0], TEXT_TYPE_LINK, link[1]))
            text = sections[1]
        if text:
            new_nodes.append(TextNode(text, TEXT_TYPE_TEXT))
    return new_nodes
