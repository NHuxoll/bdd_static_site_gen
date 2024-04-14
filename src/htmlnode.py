from typing import List, Dict


class HTMLNode:

    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: List | None = None,
        props: Dict[str, str] | None = None,
    ):

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props: Dict[str, str] | None = None):
        if not value:
            raise ValueError("All leaf nodes require a value")

        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.tag is None:
            return self.value
        elif self.value is None:
            raise ValueError("Invalid HTML: no value")
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props: Dict[str, str] | None = None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children:{self.children}, {self.props})"
