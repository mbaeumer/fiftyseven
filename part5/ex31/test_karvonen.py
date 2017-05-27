#!/usr/bin/python
import unittest
from karvonen_calculator import calculate_target_heart_rate

class TestKarvonen(unittest.TestCase):
  def test_calculation(self):
    intensity = 55
    resting_heart_rate = 65
    age = 22
    result = calculate_target_heart_rate(intensity, resting_heart_rate, age)
    print("result: %d" % (result))
    self.assertTrue(calculate_target_heart_rate(intensity, resting_heart_rate, age) == 138)


if __name__ == '__main__':
  unittest.main()
