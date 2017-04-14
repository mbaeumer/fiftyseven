#/usr/bin/python
import unittest
from anagram import isAnagram

class AnagramTest(unittest.TestCase):
  def test_empty_string(self):
    self.assertFalse(isAnagram("", "test"))
  
  def test_unequal_string(self):
    self.assertFalse(isAnagram("test", "test2"))
  
  def test_true(self):
    self.assertTrue(isAnagram("note", "tone"))

  def test_true(self):
    self.assertTrue(isAnagram("two", "wot"))

  def test_false(self):
    self.assertFalse(isAnagram("note", "nott"))



if __name__ == '__main__':
  unittest.main()
