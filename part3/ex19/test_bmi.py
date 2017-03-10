#!/usr/bin/python
import unittest
from bmi_calc_core import get_bmi
from bmi_calc_core import get_bmi_level

class TestBMI(unittest.TestCase):
  def test_get_bmi(self):
    self.assertTrue(get_bmi(16.9, 105.4) == 15.2)

  def test_get_bmi_level_underweight(self):
    self.assertTrue(get_bmi_level(16) == "You are underweight")

  def test_get_bmi_level_normal(self):
    self.assertTrue(get_bmi_level(19) == "Your result is ok")

  def test_get_bmi_level_overweight(self):
    self.assertTrue(get_bmi_level(30) == "You are overweight")

if __name__ == '__main__':
  unittest.main()
