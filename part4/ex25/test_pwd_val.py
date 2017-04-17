#!/usr/bin/python
import unittest
from passwordstrength import PasswordStrength
from pwd_val import validatePassword

class PasswordStrengthCheckerTest(unittest.TestCase):
  def test_very_weak(self):
    self.assertTrue(validatePassword('12345') == PasswordStrength.VERY_WEAK)

  def test_very_weak(self):
    self.assertTrue(validatePassword('abcdef') == PasswordStrength.WEAK)

  def test_strong_v1(self):
    self.assertTrue(validatePassword('abcdef1') == PasswordStrength.STRONG)

  def test_strong_v2(self):
    self.assertTrue(validatePassword('123456f') == PasswordStrength.STRONG)

  def test_very_strong(self):
    print(validatePassword('123456#f'))
    self.assertTrue(validatePassword('123456#f') == PasswordStrength.VERY_STRONG)


if __name__ == '__main__':
  unittest.main()
