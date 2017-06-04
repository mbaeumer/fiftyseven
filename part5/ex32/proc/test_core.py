#!/usr/bin/python
import unittest
from guess_number_core import generate_my_number
from guess_number_core import isValidGuess
from guess_number_core import validateGuess
from comparison_result import ComparisonResult
from level import Difficulty

class TestCore(unittest.TestCase):
  def test_generate_random_easy(self):
    level = Difficulty.EASY
    first = generate_my_number(level)
    second = generate_my_number(level)
    self.assertTrue(first < 11)
    self.assertTrue(second != first)
  
  def test_generate_random_medium(self):
    level = Difficulty.MEDIUM
    first = generate_my_number(level)
    second = generate_my_number(level)
    self.assertTrue(first < 51)
    self.assertTrue(second != first)

  def test_generate_random_hard(self):
    level = Difficulty.HARD
    first = generate_my_number(level)
    second = generate_my_number(level)
    self.assertTrue(first < 101)
    self.assertTrue(second != first)

  def test_valid_guess(self):
    self.assertTrue(isValidGuess(5) == True)

  def test_invalid_guess(self):
    self.assertFalse(isValidGuess('test') == True)

  def test_invalid_guess(self):
    self.assertFalse(isValidGuess('test') == True)

  def test_validate_guess_HIGHER(self):
    self.assertTrue(validateGuess(5, 7) == ComparisonResult.HIGHER)

  def test_validate_guess_LOWER(self):
    self.assertTrue(validateGuess(7, 5) == ComparisonResult.LOWER)

  def test_validate_guess_EQUAL(self):
    self.assertTrue(validateGuess(7, 7) == ComparisonResult.EQUAL)

if __name__ == '__main__':
  unittest.main()
