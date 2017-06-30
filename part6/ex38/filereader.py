#!/usr/bin/python
from number_filter import filter_even_numbers

def read_file(filename):
  numbers = []
  try:
    file = open(filename, "r")
    for row in file:
      filtered_values = filter_even_numbers(row)
      numbers.extend(filtered_values)
    file.close()
  except FileNotFoundError as e:
    print("The file does not exist!")
    raise FileNotFoundError
  return numbers
