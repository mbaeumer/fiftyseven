#!/usr/bin/python
import unittest
from unittest import mock
import capture_user_input  
import tax_calculator

class TestTaxCalculator(unittest.TestCase):
  def test_valid_order_value(self):
    with mock.patch('builtins.input', return_value = 150 ):
      self.assertTrue(capture_user_input.get_order_value() == 150)

  def test_invalid_order_value(self):
    with mock.patch('builtins.input', return_value = '2.5'):
      self.assertRaises(ValueError, capture_user_input.get_order_value)

  def test_negative_order_value(self):
    with mock.patch('builtins.input', return_value = -5):
      self.assertRaises(ValueError, capture_user_input.get_order_value)

  def test_valid_state(self):
    with mock.patch('builtins.input', return_value = 'WI'):
      self.assertTrue(capture_user_input.get_state() == 'WI')

  def test_state_undefined(self):
    with mock.patch('builtins.input', return_value = ''):
      self.assertRaises(ValueError, capture_user_input.get_state)
  
  def test_calculate_tax_WI(self):
    self.assertTrue(tax_calculator.calculate_tax(10, 'WI') == 0.55)

if __name__ == '__main__':
  unittest.main()
