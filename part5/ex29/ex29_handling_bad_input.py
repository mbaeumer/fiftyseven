#!/usr/bin/python

def main():
  print_title()
  rate = capture_input()
  result = calc_rate_of_return(rate)
  print_result(result)
  
def print_title():
  print("Exercise 29: Handling bad input")
  print("")

def print_result(result):
  print("It will take %d years to double your investment." % (result))

def calc_rate_of_return(rate):
  return 72/rate

def capture_input():
  rate = 0
  correct = False
  while not correct: 
    try:
      rate = int(input("What is the rate of return?  "))
      if rate == 0:
        print("ERROR: The rate must not be 0!")
      else:
        correct = True
    except ValueError:
      print("ERROR: Please enter an integer value!")
  return rate

if __name__ == '__main__':
  main() 
