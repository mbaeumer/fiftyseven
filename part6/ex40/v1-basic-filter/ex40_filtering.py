#!/usr/bin/python
from datahandler import create_list
from datahandler import filter_list
from prettytable import PrettyTable

def main():
  print_title()
  employees = create_list()
  print_result(employees)
  criteria = select_criteria()
  word = get_filter_word()
  if len(word) > 0:
    employees = filter_list(employees, get_criteria(criteria), word)
    print_result(employees)
  else:
    print("ERROR! You did not enter a word")

def print_result(employees):
  e = employees[0]
  table = PrettyTable(e.keys()) 
  for empl in employees:
    values = empl.values()
    table.add_row(values)
  print(table)

def print_title():
  print("Exercise 40: Filtering values")
  print("")

def select_criteria():
  selected = False
  choice = 0
  while not selected:
    try:
      print("Select a filtering criteria:")
      print("1 - First name")
      print("2 - Last name")
      print("3 - Position")
      print("4 - Date")

      choice = int(input("Your choice: "))
      if choice >=1 and choice < 5:
        selected = True
    except ValueError:
      print("ERROR: Wrong choice!") 
  return choice

def get_filter_word():
  return input("Enter a word: ")

def get_criteria(key):
  criteria = 'firstname'
  if key == 2:
    criteria = 'lastname'
  elif key == 3:
    criteria = 'position'
  elif key == 4:
    criteria = 'separation_date'
  return criteria

if __name__ == '__main__':
  main()
