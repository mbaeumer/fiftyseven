import unittest
from paint_calculator import calculate_paint

class Exercise9TestCase(unittest.TestCase):
  def test_calculate_paint_350(self):
    self.assertTrue(calculate_paint(350) == 1)
  
  def test_calculate_paint_360(self):
    self.assertTrue(calculate_paint(360) == 2)

if __name__ == '__main__':
  unittest.main()
