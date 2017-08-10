#!/usr/bin/python
from person import Person
from sorting_order import SortingOrder
from sorting_criteria import SortingCriteria

def main():
  print_title()
  persons = create_list()
  print_list(persons)
  sorting_criteria = get_sorting_criteria()
  sorting_order = get_sorting_order()
  persons = sort_list(persons, sorting_criteria, sorting_order)
  print_list(persons)

def print_title():
  print("Exercise 41 - version 2 - advanced sorting")
  print("")

def print_list(persons):
  print("Number of persons: %d" % (len(persons)))
  for p in persons:
    print("%s \t %s \t %d" % (p.firstname, p.lastname, p.salary))

def get_sorting_criteria():
  selected = False
  sorting_criteria = ''
  while not selected:
    try:
      print("Select the sorting criteria:")
      print("1 - Firstname")
      print("2 - Lastname")
      print("3 - Salary")
      user_input = int(input("Your choice: "))
      if user_input >= 1 and user_input< 4:
        selected = True
    except ValueError:
      print("ERROR: Wrong sorting criteria")
  sorting_criteria = SortingCriteria(user_input)
  return sorting_criteria

def get_sorting_order():
  selected = False
  sorting_order = ''
  while not selected:
    try:
      print("Select the sorting order:")
      print("1 - Ascending")
      print("2 - Descending")
      user_input = int(input("Your choice: "))
      if user_input == 1 or user_input == 2:
        selected = True
    except ValueError:
      print("ERROR: Wrong sorting order")
  sorting_order = SortingOrder(user_input)
  return sorting_order
  
def create_list():
  persons = []
  persons.append(create_person("Pelle","Emilsson",1234567))
  persons.append(create_person("Lasse","Larsson",76542321))
  persons.append(create_person("Martin","Baeumer",1234567))
  persons.append(create_person("Pelle","Adamsson",1234567))
  persons.append(create_person("Mats","Bertilsson",1234567))
  persons.append(create_person("Pelle","Caesar",1234567))
  persons.append(create_person("Marcus","Danielsson",1234567))
  persons.append(create_person("Pelle","Fredriksson",1234567))
  persons.append(create_person("Pelle","Gustavsson",1234567))
  persons.append(create_person("Pelle","Henriksson",1234567))
  persons.append(create_person("Pelle","Harrysson",1234567))
  persons.append(create_person("Ida","Rikardsson",1234567))
  persons.append(create_person("Ida","Sigurdsson",1234567))
  persons.append(create_person("Inga","Oscarsson",1234567))
  persons.append(create_person("Jakob","Ivarsson",1234567))
  persons.append(create_person("Adam","Jakobsson",1234567))
  persons.append(create_person("Ida","Karlsson",1234567))
  persons.append(create_person("Bertil","Ivarsson",1234567))
  persons.append(create_person("Christian","Martinsson",1234567))
  persons.append(create_person("Christer","Nilsson",1234567))
  persons.append(create_person("Per","Persson",1234567))
  persons.append(create_person("Johan","Rikardsson",1234567))
  persons.append(create_person("Johan","Sigurdsson",1234567))
  persons.append(create_person("Stefan","Tomasson",1234567))
  persons.append(create_person("Sigurd","Urbansson",1234567))
  persons.append(create_person("Ida","Viktorsson",1234567))
  persons.append(create_person("Ida","Wilhelmsson",1234567))
  return persons

def create_person(firstname, lastname, salary):
  person = Person(firstname, lastname, salary)
  return person

def sort_list(persons, sorting_criteria, sorting_order):
  i = 0
  while i <= len(persons) - 1:
    j = i + 1
    while j <= len(persons) - 1:
      #print("index: i: %d j: %d" % (i, j))
      #print("comparing %s to %s" % (persons[i].lastname, persons[j].lastname))
      if sorting_criteria == SortingCriteria.LASTNAME:  
        if sorting_order == SortingOrder.ASCENDING:  
          if persons[i].lastname > persons[j].lastname:   
            persons = swap_persons(persons, i, j)
        elif sorting_order == SortingOrder.DESCENDING:
          if persons[i].lastname < persons[j].lastname:   
            persons = swap_persons(persons, i, j)
      elif sorting_criteria == SortingCriteria.FIRSTNAME:
        if sorting_order == SortingOrder.ASCENDING:  
          if persons[i].firstname > persons[j].firstname:   
            persons = swap_persons(persons, i, j)
        elif sorting_order == SortingOrder.DESCENDING:
          if persons[i].firstname < persons[j].firstname:   
            persons = swap_persons(persons, i, j)
      elif sorting_criteria == SortingCriteria.SALARY:
        if sorting_order == SortingOrder.ASCENDING:  
          if persons[i].salary > persons[j].salary:   
            persons = swap_persons(persons, i, j)
        elif sorting_order == SortingOrder.DESCENDING:
          if persons[i].salary < persons[j].salary:   
            persons = swap_persons(persons, i, j)
      j = j + 1
    i = i + 1
  return persons

def swap_persons(persons, i, j):
  swap = persons[i]
  persons[i] = persons[j]
  persons[j] = swap
  return persons
  
if __name__ == '__main__':
  main()
