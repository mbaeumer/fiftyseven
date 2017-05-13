#!/usr/bin/python
import unittest
from core import calculateMonths

class TestCalc(unittest.TestCase):
  def test_calc(self):
    self.assertTrue(calculateMonths(5000, 12, 100) == 70)

if __name__ == '__main__':
  unittest.main()
