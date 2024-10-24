import os
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


def process_heading(text):
    level = text.count("#")
    text = filter(lambda x: x != "#", text)
    text = "".join(text).strip()
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
        if block_type == MD_TYPE_QUOTE:
            nodes.append(process_quote(block))
        if block_type == MD_TYPE_UL:
            nodes.append(process_unordered_list(block))
        if block_type == MD_TYPE_OL:
            nodes.append(process_ordered_list(block))
        if block_type == MD_TYPE_H:
            nodes.append(process_heading(block))
    return ParentNode(tag="div", children=nodes)


def generate_page(src, tmp_path, dst):
    print(f"Generating page from {src} to {dst} using {tmp_path}")
    src_exists = os.path.exists(src)
    tmp_exists = os.path.exists(tmp_path)
    if not src_exists or not tmp_exists:
        raise Exception(
            "Required files missing.  Please ensure all files exist and try again."
        )
    with open(tmp_path) as f:
        template = f.read()
    with open(src) as f:
        content = f.read()
    content_html = markdown_to_html_node(content).to_html()
    title = extract_title(content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content_html)
    dir = os.path.dirname(dst)
    if not os.path.exists(dir):
        os.mkdirs(dir)
    with open(dst, "a") as f:
        f.write(template)


"""
This function will behave similarly to copy_dir
> Scan current directory for ".md" files
> For each file found, convert to HTML, write to public directory
> If a folder is found, append the name to the src path and dst path & call again
"""


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        new_ext = item.replace(".md", ".html")
        dst_path = os.path.join(dest_dir_path, new_ext)
        if os.path.isfile(item_path):
            generate_page(item_path, template_path, dst_path)
        if os.path.isdir(item_path):
            os.mkdir(dst_path)
            generate_pages_recursive(item_path, template_path, dst_path)
