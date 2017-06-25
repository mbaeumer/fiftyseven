#!/usr/bin/python
from pwdgen_core import generate_password

def main():
  print_title()
  min_length = capture_min_password_length()
  min_specials = capture_min_special_chars(min_length)
  min_numbers = capture_min_numbers(min_length, min_specials)
  password = generate_password(min_length, min_numbers, min_specials)

  print("Suggested password: %s " % (password))

def print_title():
  print("Exercise 37: Password generator")
  print("")

def capture_min_password_length():
  min_length = 0
  finished = False
  while not finished:
    try:
      min_length = int(input("What is the minimum length? "))
      if min_length <= 0:
        raise ValueError
      finished = True
    except ValueError:
      print("ERROR: Please enter a valid number!")
  return min_length

def capture_min_special_chars(min_length):
  min_specials = 0
  finished = False
  while not finished:
    try:
      min_specials = int(input("How many special characters? "))
      if min_specials < 0 or min_specials > min_length:
        raise ValueError
      finished = True
    except ValueError:
      print("ERROR: Please enter a valid number! ")
  return min_specials

def capture_min_numbers(min_length, min_special_chars):
  min_numbers = 0
  finished = False
  while not finished:
    try:
      min_numbers = int(input("How many numbers? "))
      if min_numbers <= 0 or min_numbers > min_length or min_numbers + min_special_chars > min_length:
        raise ValueError
      finished = True
    except ValueError:
      print("ERROR: Please enter a valid number")
  return min_numbers

if __name__ == '__main__':
  main()
