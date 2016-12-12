import unittest
from area_calculator import convert_to_m2
from area_calculator import get_area

class Exercise7TestCase(unittest.TestCase):
  def test_convert_to_m2(self):
    print(convert_to_m2(300))
    self.assertTrue(convert_to_m2(300) == 27.870912)

  def test_get_area(self):
    self.assertTrue(get_area(15,20) == 300)

if __name__ == '__main__':
  unittest.main()
