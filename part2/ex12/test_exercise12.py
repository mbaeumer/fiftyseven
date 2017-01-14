#!/usr/bin/python
import unittest
from unittest import mock
import capture_user_input #import get_principal 
from calculate_interest import calculate

class TestInterestCalculator(unittest.TestCase):
  def test_valid_principal(self):
    with mock.patch('builtins.input', return_value = 1500 ):
      self.assertTrue(capture_user_input.get_principal() == 1500)

  def test_invalid_principal(self):
    with mock.patch('builtins.input', return_value = 'test'):
      self.assertRaises(ValueError, capture_user_input.get_principal)

  def test_valid_interest_rate(self):
    with mock.patch('builtins.input', return_value = 2.5):
      self.assertTrue(capture_user_input.get_interest_rate() == 2.5)

  def test_invalid_interest_rate(self):
    with mock.patch('builtins.input', return_value = 'test'):
      self.assertRaises(ValueError, capture_user_input.get_interest_rate)

  def test_valid_year(self):
    with mock.patch('builtins.input', return_value = 5):
      self.assertTrue(capture_user_input.get_years() == 5)

  def test_year_float(self):
    with mock.patch('builtins.input', return_value = '4.5'):
      self.assertRaises(ValueError, capture_user_input.get_years)

  def test_year_string(self):
    with mock.patch('builtins.input', return_value = 'test'):
      self.assertRaises(ValueError, capture_user_input.get_years) 

  def test_calculate(self):
    self.assertTrue(calculate(1500, 4.3, 4) == 1758)

if __name__ == '__main__':
  unittest.main()
