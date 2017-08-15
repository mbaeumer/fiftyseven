import unittest
from html_util import generate_html_tag
from html_util import generate_meta_tag
from html_util import generate_title

class HtmlUtilTest(unittest.TestCase):
  def test_generate_html_start_tag(self):
    expected = "<html>\n"
    actual = generate_html_tag("html", False, True)
    self.assertTrue(actual ==  expected)

  def test_generate_html_end_tag(self):
    expected = "</html>\n"
    actual = generate_html_tag("html", True, True)
    self.assertTrue(actual ==  expected)

  def test_generate_title_tag(self):
    expected = "<title>some title</title>\n"
    actual = generate_title("some title")
    self.assertTrue(actual ==  expected)

  def test_generate_meta_tag(self):
    expected = "<meta name=\"author\" content=\"John Doe\"/>" + "\n"
    actual = generate_meta_tag("John Doe")
    self.assertTrue(actual ==  expected)

if __name__ == '__main__':
  unittest.main()


