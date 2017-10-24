#!/usr/bin/python
from requestutil import get_raw_data
from astronaut import Astronaut
from prettytable import PrettyTable
from nameutil import handle_name

def main():
  print_title()
  url = "http://api.open-notify.org/astros.json"
  raw_data = get_raw_data(url)
  print(raw_data)
  astronauts = create_astronauts(raw_data)
  

  print_result(get_printable_astronauts(astronauts))

def print_title():
  print("Exercise 47: Who is in space?\n")

def create_astronauts(raw_data):
  astronauts = []
  for item in raw_data['people']:
    astronaut = handle_name(item['name'])
    astronaut.craft = item['craft']
    astronauts.append(astronaut)
  return astronauts

def get_printable_astronauts(astronauts):
  printable_astronauts = []
  for a in astronauts:
    printable_astronauts.append(a.to_dict())
  return printable_astronauts

def print_result(astronauts):
  astronaut = astronauts[0]
  table = PrettyTable(astronaut.keys())
  for astronaut in astronauts:
    values = astronaut.values()
    table.add_row(values)
  print(table)

if __name__ == '__main__':
  main()
