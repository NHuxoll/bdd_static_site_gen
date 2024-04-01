from typing import List, Dict

class HTMLNode:
    
    def __init__(self, tag: str | None = None, value: str | None = None, children: List | None =None, props: Dict[str,str] | None = None):

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
    def __init__(self, tag: str | None = None, value:str | None = None,props: Dict[str,str] | None = None):
        if not value:
            raise ValueError("All leaf nodes require a value")
    
        super().__init__(tag=tag,value=value,props=props)
        
    def to_html(self):
        if self.tag == None:
            return f"{self.value}"
        elif self.tag == "p":
            return f"<{self.tag}>{self.value}</{self.tag}>"
        elif self.tag == "a":
            for prop in self.props:
                return f"<{self.tag} {prop}=\"{self.props[prop]}\">{self.value}</{self.tag}>"
        else:
            return ""
            
