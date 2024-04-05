import unittest
from inline_markdown import (
    split_nodes_delimiter
)

from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code
)

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        pass
    def test_delim_bold_double(self):
        pass
    def test_delim_bold_multi_word(self):
        pass

    def test_delim_italic(self):
        pass

    def test_delim_italic_double(self):
        pass

    def test_delim_italic_multi_word(self):
        pass

    def test_delim_code(self):
        pass

    def test_node_code(self):
        pass

    def test_node_bold(self):
        pass

    def test_node_italic(self):
        pass

if __name__ == "__main__":
    unittest.main()
