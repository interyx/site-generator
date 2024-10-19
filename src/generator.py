from src.constants import *
from src.leafnode import LeafNode
from src.textnode import TextNode
from src.parentnode import ParentNode
from src.util import *
from src.mdutil import *

def text_to_children(text):
    nodes = text_to_textnodes(text)
    text_nodes = []
    for node in nodes:
        text_nodes.append(text_node_to_html_node(node))
    return text_nodes

def process_paragraph(text):
    text_nodes = text_to_children(text)
        
    return ParentNode(tag="p", children=text_nodes)

def process_heading(text, level):
    text_nodes = text_to_children(text)

    return ParentNode(tag=f"h{level}", children=text_nodes)

def process_code(text):
    text = text.replace("```", "")
    node = LeafNode(value=text)
    code_block = ParentNode(tag="code", children=[node])
    return ParentNode(tag="pre", children=[code_block])

def process_quote(text):
    text = text.replace("> ", "")
    nodes = text_to_children(text)

    return ParentNode(tag="blockquote", children=nodes)
    
def process_unordered_list(text):
    lines = text.replace("- ", "").replace("* ", "").split("\n")
    ul = []
    for line in lines:
        child_nodes = text_to_children(line)
        ul.append(ParentNode(tag="li", children=child_nodes))
    return ParentNode(tag="ul", children=ul)

def process_ordered_list(text):
    lines = text.split("\n")
    fixed_lines = [line[3:] for line in lines]
    final_list = []
    for line in fixed_lines:
        child_nodes = text_to_children(line)
        final_list.append(ParentNode(tag="li", children=child_nodes))
    return ParentNode(tag="ol", children=final_list)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == MD_TYPE_P:
            nodes.append(process_paragraph(block))
        if block_type == MD_TYPE_CODE:
            nodes.append(process_code(block))
    return ParentNode(tag="div", children=nodes)
