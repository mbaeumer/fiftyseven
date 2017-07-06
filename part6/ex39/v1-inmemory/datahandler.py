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

def sort_list(employees, sorting_key):
  sorted = []
  sorted.append(employees[0])
  index = 1
  while index < len(employees):
    empl = employees[index]
    sorted_index = 0
    inserted = False
    for sorted_empl in sorted:
      if empl[sorting_key] <= sorted_empl[sorting_key]:
        sorted.insert(sorted_index, empl)
        inserted = True
        break
      sorted_index = sorted_index + 1
    if not inserted:
      sorted.append(empl)
    index = index + 1
  return sorted
