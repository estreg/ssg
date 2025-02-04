import unittest
from extractmarkdown import extract_markdown_images, extract_markdown_links

class TestMarkdownExtraction(unittest.TestCase):
    def test_basic_image_extraction(self):
        text = "![test image](test.jpg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("test image", "test.jpg")])

    def test_basic_link_extraction(self):
        text = "[test link](test.com)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("test link", "test.com")])

    def test_multi_image_extraction(self):
        text = "first ![test image](test.jpg) and than ![test2 image](test2.jpg)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("test image", "test.jpg"), ("test2 image", "test2.jpg")])

if __name__ == '__main__':
    unittest.main()