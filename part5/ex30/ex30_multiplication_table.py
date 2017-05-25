#!/usr/bin/python

def main():
  print_title()
  print_multiplication_table()

def print_title():
  print("Exercise 30: Multiplication table")
  print("")
  
def print_multiplication_table():
  i = 0
  end = 13
  while i < end:
    j = 0
    while j < end:
      result = i * j
      print("%d * %d = %d" % (i, j, result))
      j = j + 1
    i = i + 1

if __name__ == '__main__':
  main()
