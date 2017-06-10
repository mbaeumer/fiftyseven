#!/usr/bin/python
import random

def main():
  print_title()
  names = get_names()
  winner = get_winner(names)
  print("The winner is: %s" % (winner))

def print_title():
  print("Exercise 35: Pick a winner")
  print("")

def get_winner(names):
  index = random.randint(0, len(names)-1)
  return names[index]

def get_names():
  names = []
  while True:
    name = input("Enter a name: ")
    if len(name) == 0:
      break
    else:
      names.append(name)
  return names

if __name__ == '__main__':
  main()
