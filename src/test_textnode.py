import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_dif(self):
        node = TextNode("This is slanted text", TextType.ITALIC)
        node2 = TextNode("This is code text", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_urls(self):
        node = TextNode("boot.dev", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("boot,dev", TextType.LINK, "http://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_none(self):
        node = TextNode("This is an unlinked website", TextType.LINK)
        node2 = TextNode("This is an unlinked website", TextType.LINK, None)
        self.assertEqual(node, node2)

    def test_same(self):
        node = TextNode("Picture of Spongebob Squarepants", TextType.IMAGE)
        node2 = TextNode("Picture of Spongebob Squarepants", TextType.IMAGE)
        self.assertEqual(node, node2)



if __name__ == "__main__":
    unittest.main()