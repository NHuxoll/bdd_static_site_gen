from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url= None):
        self.text = text 
        self.text_type = text_type
        self.url = url 

    def __eq__(self, __value: object) -> bool:
        if self.url == __value.url and self.text == __value.text and self.text_type == __value.text_type:
            return True 
        else:
            return False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
        if text_node.text_type == text_type_text:
            return LeafNode(None, text_node.text)
        if text_node.text_type == text_type_bold:
            return LeafNode("b", text_node.text)
        if text_node.text_type == text_type_italic:
            return LeafNode("i", text_node.text)
        if text_node.text_type == text_type_code:
            return LeafNode("code", text_node.text)
        if text_node.text_type == text_type_link:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        if text_node.text_type == text_type_image:
            return LeafNode("img", "",{"src": text_node.url, "alt": text_node.text})
        raise ValueError(f"Invalid text type: ")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return_list = []
    for o_node in old_nodes:
        tmp = []
        split = o_node.text.split(delimiter)
        for index, split_node in enumerate(split):
            if index % 2 == 0:
                tmp.append(TextNode(split_node, text_type_text))
            else:
                if delimiter == "**":
                    tmp.append(TextNode(split_node, text_type_bold))
                if delimiter == "*":
                    tmp.append(TextNode(split_node, text_type_italic))
                if delimiter == "'":
                    tmp.append(TextNode(split_node, text_type_code))
        return_list.extend(tmp)
    return return_list

