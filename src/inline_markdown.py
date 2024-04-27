import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
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


def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
        else:
            for image in images:
                split = node.text.split(f"![{image[0]}]({image[1]})", 1)
                node.text = split[1]
                if not split or split[0] == "":
                    continue
                else:
                    new_nodes.append(TextNode(split[0], text_type_text, None))
                    new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            if node.text != "":
                new_nodes.append(node)
    return new_nodes


def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
        else:
            for link in links:
                split = node.text.split(f"[{link[0]}]({link[1]})", 1)
                node.text = split[1]
                if not split or split[0] == "":
                    continue
                else:
                    new_nodes.append(TextNode(split[0], text_type_text, None))
                    new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            if node.text != "":
                new_nodes.append(node)
    return new_nodes


def extract_markdown_images(text):
    image_list = []
    alt_and_image = r"!\[\s?\w+\s?\w+?\]\(\S+\.png\)"
    extracted_images = re.findall(alt_and_image, text)
    for image in extracted_images:
        alt = re.search(r"\!\[\s?\w+\s?\w+?\]", image).group(0)[2:-1]
        image_link = re.search(r"\(\w+\:\/\/(\w+.)+.png\)", image).group(0)[1:-1]
        image_list.append((alt, image_link))
    return image_list


def extract_markdown_links(text):
    link_list = []
    alt_and_link = r"[^!]\[\s?\w+\s?\w+?\]\(\S+\)"
    extracted_links = re.findall(alt_and_link, text)
    for links in extracted_links:
        alt = re.search(r"\[\s?\w+\s?\w+?\]", links).group(0)[1:-1]
        link = re.search(r"\(\w+\:?\/?/?(\w+.)+\)", links).group(0)[1:-1]
        link_list.append((alt, link))
    return link_list


def text_to_textnodes(text):
    nodes_list = [TextNode(text, text_type_text)]
    nodes_list = split_nodes_links(nodes_list)
    nodes_list = split_nodes_images(nodes_list)
    nodes_list = split_nodes_delimiter(nodes_list, "**", text_type_bold)
    nodes_list = split_nodes_delimiter(nodes_list, "*", text_type_italic)
    nodes_list = split_nodes_delimiter(nodes_list, "`", text_type_code)
    return nodes_list
