#!/usr/bin/python
import unittest
from validation_error import ValidationError
from input_validator import isZipValid
from input_validator import isIdValid
from input_validator import isStringValid

class ValidatorTest(unittest.TestCase):
  def test_isZipValid_none(self):
    self.assertTrue(isZipValid('12345') == ValidationError.NONE)
  
  def test_isZipValid_notvalid_too_short(self):
    self.assertTrue(isZipValid('1234') == ValidationError.ZIP_NOT_VALID)

  def test_isZipValid_notvalid_alphanumeric(self):
    self.assertTrue(isZipValid('1234a') == ValidationError.ZIP_NOT_VALID)

  def test_isZipValid_empty(self):
    self.assertTrue(isZipValid('') == ValidationError.ZIP_EMPTY)

  def test_isIdValid_none(self):
    self.assertTrue(isIdValid('AB-1234') == ValidationError.NONE)

  def test_isIdValid_notvalid(self):
    self.assertTrue(isIdValid('ABC-1234') == ValidationError.ID_NOT_VALID)

  def test_isIdValid_empty(self):
    self.assertTrue(isIdValid('') == ValidationError.ID_EMPTY)

  def test_isFirstNameValid_empty(self):
    self.assertTrue(isStringValid('', True) == ValidationError.FIRSTNAME_EMPTY)
  
  def test_isFirstNameValid_too_short(self):
    self.assertTrue(isStringValid('M', True) == ValidationError.FIRSTNAME_NOT_VALID)
  
  def test_isFirstNameValid_alphanumeric(self):
    self.assertTrue(isStringValid('Martin2', True) == ValidationError.FIRSTNAME_NOT_VALID)
  
if __name__ == '__main__':
  unittest.main()

