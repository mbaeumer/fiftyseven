#!/usr/bin/pthon
from capture_input import capture_age
from capture_input import capture_resting_heart_rate
from karvonen_calculator import calculate_target_heart_rate

def main():
  print_title()
  run()

def print_title():
  print("Exercise 31: Karvonen heart rate")
  print("")

def run():
  age = capture_age()
  heart_rate = capture_resting_heart_rate()
  
  steps = 5
  start_intensity = 55
  end_intensity = 100
  i = start_intensity

  while i <= end_intensity:
    result = calculate_target_heart_rate(i, heart_rate, age)
    print("%d  -- %d bpm" % (i, result))
    i = i + steps 


if __name__ == '__main__':
  main()

