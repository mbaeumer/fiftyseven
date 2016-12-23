import unittest
from pizza_calculator import get_total_slices
from pizza_calculator import get_slices_per_person
from pizza_calculator import get_leftovers
from pluralization import get_pieces
from pluralization import get_proper_be
from pluralization import get_pizzas

class Exercise8Test(unittest.TestCase):
  def test_totoal_slices(self):
    self.assertTrue(get_total_slices(2) == 16)

  def test_slices_per_person(self):
    self.assertTrue(get_slices_per_person(16,4) == 4)
  
  def test_leftover(self):
    self.assertTrue(get_leftovers(16,6) == 4)

  def test_get_pieces_multiple(self):
    self.assertTrue(get_pieces(8) == "pieces")

  def test_get_pieces_single(self):
    self.assertTrue(get_pieces(1) == "piece")
  
  def test_get_pizzas_multiple(self):
    self.assertTrue(get_pizzas(2) == "pizzas")

  def test_get_pizza_single(self):
    self.assertTrue(get_pizzas(1) == "pizza")

  def test_get_proper_be_is(self):
    self.assertTrue(get_proper_be(1) == "is")

  def test_get_proper_be_are(self):
    self.assertTrue(get_proper_be(2) == "are")

if __name__ == '__main__':
  unittest.main()
