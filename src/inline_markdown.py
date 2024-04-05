from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code )

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) %2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for index, split_node in enumerate(sections):
            if split_node == "":
                continue
            if index % 2 == 0:
                split_nodes.append(TextNode(split_node, text_type_text))
            else:
                split_nodes.append(TextNode(split_node, text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

