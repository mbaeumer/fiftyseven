#!/usr/bin/python
from datahandler import create_list
from datahandler import filter_list
from prettytable import PrettyTable
from filtercriteria import FilterCriteria
from datefilteroption import DateFilterOption
from stringfilteroption import StringFilterOption

def main():
  print_title()
  employees = create_list()
  print_result(employees)
  
  filter_criteria = select_criteria()
  print(filter_criteria)
  criteria_as_word = get_criteria_as_word(filter_criteria)
  string_filter_option = ''
  date_filter_option = ''
  term= ''
  if filter_criteria == FilterCriteria.BIRTHDATE:
    date_filter_option = select_date_filter_option()
    employees = filter_list(employees, criteria_as_word, string_filter_option, date_filter_option, term)
    print_result(employees)
    
  else:
    string_filter_option = select_string_filter_option()
    term = get_filter_term()
    if len(term) > 0:
      employees = filter_list(employees, criteria_as_word, string_filter_option, date_filter_option, term)
      print_result(employees)
    else:
      print("ERROR! You did not enter a term")

def print_result(employees):
  if len(employees) > 0:
    e = employees[0]
    table = PrettyTable(e.keys()) 
    for empl in employees:
      values = empl.values()
      table.add_row(values)
    print(table)
  else:
    print("No matches found!")

def print_title():
  print("Exercise 40: Filtering values with an advanced filter")
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
      print("4 - Birthdate")
      choice = int(input("Your choice: "))
      if choice >=1 and choice < 5:
        selected = True
    except ValueError:
      print("ERROR: Please select a valid criterion!") 
  return FilterCriteria(choice)

def select_string_filter_option():
  selected = False
  choice = 0
  while not selected:
    try:
      print("Select a filter option")
      print("1 - Starts with")
      print("2 - Ends with")
      print("3 - Contains")
      choice = int(input("Your choice: "))
      if choice >= 1 and choice < 4:
        selected = True
    except ValueError:
      print("ERROR: Please select a valid filter option")
  return StringFilterOption(choice)

def select_date_filter_option():
  selected = False
  choice = 0
  while not selected:
    try:
      print("Select a filter option")
      print("1 - Latest 6 months")
      print("2 - Last 2 weeks")
      choice = int(input("Your choice: "))
      if choice >= 1 and choice < 3:
        selected = True
    except ValueError:
      print("ERROR: Please select a valid option for date")
  return DateFilterOption(choice)

def get_criteria_as_word(criteria):
  criteria_as_word = 'firstname'
  if criteria == FilterCriteria.LASTNAME:
    criteria_as_word = 'lastname'
  elif criteria == FilterCriteria.POSITION:
    criteria_as_word = 'position'
  elif criteria == FilterCriteria.BIRTHDATE:
    criteria_as_word = 'birth_date'
  return criteria_as_word

def get_filter_term():
  term = input("Enter a term: ")
  return term

if __name__ == '__main__':
  main()
