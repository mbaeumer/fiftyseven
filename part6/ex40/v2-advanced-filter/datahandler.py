#!/usr/bin/python
from stringfilteroption import StringFilterOption
from datefilteroption import DateFilterOption
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

def create_list():
  employees = []
  employees.append(create_dictionary("Bob", "Marley", "guitar", datetime(2016, 12, 31)))
  employees.append(create_dictionary("Mick", "Jagger", "vocals", datetime(2017, 5, 23)))
  employees.append(create_dictionary("Ringo", "Starr", "vocals", datetime(2017, 6, 16)))
  employees.append(create_dictionary("Jane", "Doe", "vocals", datetime(2017, 7, 15)))
  employees.append(create_dictionary("Bruce", "Willis", "actor", datetime(2017, 2, 17)))
  employees.append(create_dictionary("John", "Johnsson", "vocals", datetime(2017, 3, 18)))
  return employees

def create_dictionary(firstname, lastname, position, birth_date):
  employee = {}
  employee['firstname'] = firstname
  employee['lastname'] = lastname
  employee['position'] = position
  employee['birth_date'] = birth_date
  return employee

def filter_list(employees, criteria_as_word, string_filter_option, date_filter_option, word):
  print("Criteria as word " + criteria_as_word)
  result = []
  for e in employees:
    if string_filter_option != '':
      if string_filter_option == StringFilterOption.STARTSWITH:
        if e[criteria_as_word].startswith(word):
          result.append(e)
      elif string_filter_option == StringFilterOption.ENDSWITH:
        if e[criteria_as_word].endswith(word):
          result.append(e)
      elif string_filter_option == StringFilterOption.CONTAINS:
        if word in e[criteria_as_word]:
          result.append(e)
    elif date_filter_option != '':
      today = datetime.now()
      if date_filter_option == DateFilterOption.LASTSIXMONTHS:
        start = today + relativedelta(months=-6) 
        date = e[criteria_as_word]
        if start < date and date <=today:
          result.append(e)
      elif date_filter_option == DateFilterOption.LASTTWOWEEKS:
        start = today + relativedelta(weeks=-2) 
        date = e[criteria_as_word]
        if start<=date<=today:
          result.append(e)
  return result
