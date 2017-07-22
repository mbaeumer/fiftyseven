#!/usr/bin/python

def create_list():
  employees = []
  employees.append(create_dictionary("Bob", "Marley", "guitar", "1970-05-11"))
  employees.append(create_dictionary("Mick", "Jagger", "vocals", ''))
  employees.append(create_dictionary("Ringo", "Starr", "drums", "1975-06-15"))
  return employees

def create_dictionary(firstname, lastname, position, separation_date):
  employee = {}
  employee['firstname'] = firstname
  employee['lastname'] = lastname
  employee['position'] = position
  employee['separation_date'] = separation_date
  return employee

def filter_list(employees, criteria, word):
  result = []
  for e in employees:
    if word in e[criteria]:
      result.append(e)
  return result
