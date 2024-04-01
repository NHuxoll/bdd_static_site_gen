import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_props_p(self):
        node = LeafNode(
            "p",
            "This is a paragraph of text",
        )
        self.assertEqual(
            node.props_to_html(),
            '<p>This is a paragraph of text</p>"',
        )

    def test_to_html_props_a(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.de"}
        )
        self.assertEqual(
            node.props_to_html(),
            '<a href="https://www.google.de">Click me!</a>"',
        )
    def test_no_tag(self):
        with self.assertRaises(ValueError):
            node = LeafNode()



if __name__ == "__main__":
    unittest.main()
