import unittest
from statistics_core import min
from statistics_core import max
from statistics_core import mean
from statistics_core import customstdDev
from statistics_core import statisticsstdDev

class StatisticsTest(unittest.TestCase):
  def test_min(self):
    numbers = self.create_number_list()
    self.assertTrue(min(numbers) == 100 )

  def test_max(self):
    numbers = self.create_number_list()
    self.assertTrue(max(numbers) == 1000 )

  def test_mean(self):
    numbers = self.create_number_list()
    self.assertTrue(mean(numbers) == 400 )
  
  def test_customstdev(self):
    numbers = self.create_small_number_list()
    self.assertTrue(customstdDev(numbers) == 3.54)
   
  def test_statisticsstdev(self):
    numbers = self.create_small_number_list()
    self.assertTrue(statisticsstdDev(numbers) == 3.54)
 
  def create_number_list(self):
    numbers = []
    numbers.append(100)
    numbers.append(200)
    numbers.append(1000)
    numbers.append(300)
    return numbers 

  def create_small_number_list(self):
    numbers = []
    numbers.append(1)
    numbers.append(2)
    numbers.append(10)
    numbers.append(3)
    return numbers
  
if __name__ == '__main__':
  unittest.main()



