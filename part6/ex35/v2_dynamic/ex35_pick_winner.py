#!/usr/bin/python
import random
from winner import Winner

def main():
  print_title()
  names = get_names()
  while len(names) > 0:
    winner = get_winner(names)
    print("The winner is: %s" % (winner.name))
    del names[winner.id]

def print_title():
  print("Exercise 35: Pick a winner")
  print("")

def get_winner(names):
  index = random.randint(0, len(names)-1)
  winner = Winner(index, names[index]) 
  return winner

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
