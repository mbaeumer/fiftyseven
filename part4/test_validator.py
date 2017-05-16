#!/usr/bin/python
import unittest
from input_validator import isZipValid

class ValidatorTest(unittest.TestCase):
  def test_isZipValid(self):
    self.assertTrue(isZipValid('12345'))
  


if __name__ == '__main__':
  unittest.main()

