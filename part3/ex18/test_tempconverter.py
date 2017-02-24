#!/usr/bin/python
import unittest
from tempconverter import get_fahrenheit
from tempconverter import get_celsius

class TestTempConverter(unittest.TestCase):
  def test_get_fahrenheit(self):
    self.assertTrue(get_fahrenheit(0)==32)

  def test_get_celsius(self):
    self.assertTrue(get_celsius(32)==0)

if __name__ == '__main__':
  unittest.main()
