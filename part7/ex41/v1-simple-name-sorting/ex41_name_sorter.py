#!/usr/bin/python
from person import Person

def main():
  print_title()
  persons = create_list()
  print_list(persons)
  persons = sort_list(persons)
  print_list(persons)

def print_title():
  print("Exercise 41 - version 1 - simple name sorting")
  print("")

def print_list(persons):
  print("Number of persons: %d" % (len(persons)))
  for p in persons:
    print("%s \t %s \t %d" % (p.firstname, p.lastname, p.salary))
  
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

def sort_list(persons):
  i = 0
  while i <= len(persons) - 1:
    j = i + 1
    while j <= len(persons) - 1:
      #print("index: i: %d j: %d" % (i, j))
      #print("comparing %s to %s" % (persons[i].lastname, persons[j].lastname))   
      if persons[i].lastname > persons[j].lastname:   
        swap = persons[i]
        persons[i] = persons[j]
        persons[j] = swap
      j = j + 1
    i = i + 1
  return persons

if __name__ == '__main__':
  main()
