import unittest
from pwdgen_core import hasEnoughNumbers
from pwdgen_core import hasEnoughSpecialChars
import re

class PasswordGeneratorTest(unittest.TestCase):
  def test_has_enough_numbers(self):
    password = 'password12'
    min_numbers = 2
    self.assertTrue(hasEnoughNumbers(password, min_numbers))

  def test_has_enough_specials(self):
    password = 'password#!'
    min_specials = 2
    self.assertTrue(hasEnoughSpecialChars(password, min_specials))

  def test_has_not_enough_numbers(self):
    password = 'password12'
    min_numbers = 3
    self.assertFalse(hasEnoughNumbers(password, min_numbers))

if __name__== '__main__':
  unittest.main()

