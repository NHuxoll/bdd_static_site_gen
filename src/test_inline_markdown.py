import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
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
        node = TextNode("This is a text with a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node],"**",text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is a text with a ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes
        )
    def test_delim_bold_double(self):
        node = TextNode("This is a text with **two** words **bolded** not one", text_type_text)
        new_nodes = split_nodes_delimiter([node],"**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is a text with ", text_type_text),
                TextNode("two", text_type_bold),
                TextNode(" words ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" not one", text_type_text),

            ],
            new_nodes
        )
    def test_delim_bold_multi_word(self):
        node = TextNode("This is a text with **multiple words** in **bold** font", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
                [
                    TextNode("This is a text with ", text_type_text),
                    TextNode("multiple words", text_type_bold),
                    TextNode(" in ", text_type_text),
                    TextNode("bold", text_type_bold),
                    TextNode(" font", text_type_text),
                ],
            new_nodes
        )

    def test_delim_italic(self):
        node = TextNode("This is a text with a *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node],"*",text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is a text with a ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes
        )
    def test_delim_italic_double(self):
        node = TextNode("This is a text with *two* words *italiced* not one", text_type_text)
        new_nodes = split_nodes_delimiter([node],"*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is a text with ", text_type_text),
                TextNode("two", text_type_italic),
                TextNode(" words ", text_type_text),
                TextNode("italiced", text_type_italic),
                TextNode(" not one", text_type_text),

            ],
            new_nodes
        )
    def test_delim_italic_multi_word(self):
        node = TextNode("This is a text with *multiple words* in *italic* font", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
                [
                    TextNode("This is a text with ", text_type_text),
                    TextNode("multiple words", text_type_italic),
                    TextNode(" in ", text_type_text),
                    TextNode("italic", text_type_italic),
                    TextNode(" font", text_type_text),
                ],
            new_nodes
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )


    def test_node_code(self):
        pass

    def test_node_bold(self):
        pass

    def test_node_italic(self):
        pass
    def test_single_image(self):
        text = "This is an ![image](https://google.de/images/test.png)"
        extracted_image = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("image", "https://google.de/images/test.png")
            ],
            extracted_image
        )
    def test_multiple_images(self):
        text = "This is an ![image](https://google.de/images/test.png), this is also ![an Image](https://www.google.de/asdf/abc.png)"
        extracted_image = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("image", "https://google.de/images/test.png"),
                ("an Image", "https://www.google.de/asdf/abc.png")
            ],
            extracted_image
        )

    def test_link_as_image(self):
        text = "test [link](https://google.de) should return nothing"
        extracted_image = extract_markdown_images(text)
        assert extracted_image == []

    def test_single_link(self):
        text = "test [link](https://google.de/asdf/abc)"
        extracted_link = extract_markdown_links(text)
        assert extracted_link == [("link", "https://google.de/asdf/abc")]
    def test_multiple_links(self):
        text = "this has [multiple](www.google.de) [links](http://reddit.com/programmerhumor)"
        extracted_links = extract_markdown_links(text)
        self.assertListEqual(
            [("multiple", "www.google.de"),("links","http://reddit.com/programmerhumor")], extracted_links
        )
if __name__ == "__main__":
    unittest.main()