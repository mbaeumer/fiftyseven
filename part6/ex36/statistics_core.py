#!/usr/bin/python
import statistics
import math

def min(numbers):
  min = numbers[0]
  for number in numbers:
    if number < min:
      min = number
  return min

def max(numbers):
  max = numbers[0]
  for number in numbers:
    if number > max:
      max = number
  return max

def mean(numbers):
  total = 0
  for number in numbers:
    total = total + number
  return total / len(numbers)

def customstdDev(numbers):
  #return statistics.stdev(numbers)
  my_mean = mean(numbers)
  squared_values = []
  for number in numbers:
    diff = number - my_mean
    squared_value = diff * diff
    squared_values.append(squared_value)
  squared_mean = mean(squared_values)
  result = math.sqrt(squared_mean)
  result = round(result, 2)
  return result

def statisticsstdDev(numbers):
  result = statistics.stdev(numbers) 
  print("from statistics module: %f" % (result))
  result = round(result, 2)
  return result  
  
