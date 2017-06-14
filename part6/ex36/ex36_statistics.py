#!/usr/bin/python
from statistics_core import mean
from statistics_core import min
from statistics_core import max
from statistics_core import customstdDev

def main():
  print_title()
  numbers = get_input()
  if len(numbers) > 0:
    print("Min: %d" % min(numbers))
    print("Max: %d" % max(numbers))
    print("Mean: %f" % mean(numbers))
    print("Std Dev: %f" % customstdDev(numbers))
  
def print_title():
  print("Exercise 36: Statistics")

def get_input():
  numbers = []
  finished =  False
  while not finished:
    try:
      number = input("Enter a number: ")
      if number != "done":
        numbers.append(int(number))
      else:
        finished = True
    except ValueError:
      print("ERROR: Please enter a valid number!")
  return numbers 

if __name__ == '__main__':
  main()
