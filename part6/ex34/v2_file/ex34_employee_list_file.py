#!/usr/bin/python

def main():
  print_title()
  employees = init_employee_list()
  if len(employees) > 0:
    print_employee_list(employees)
    selected = get_employee_to_delete()
    print (selected in employees)
    if selected in employees:
      employees = delete_employee(selected, employees)
      print_employee_list(employees)
      writeToFile(employees)
    else:
      print("Sorry, the employee '%s' does not exist!" % (selected))
  else:
    print("Sorry! No names were processed!")

def print_title():
  print("Exercise 34: Employee list (using file as data source)")
  print("")

def init_employee_list():
  employees = []
  try:
    file = open("employees.txt", "r")
    for line in file:
      line = line[:-1]
      employees.append(line)
    file.close()
  except FileNotFoundError:
    print("ERROR: The file does not exist")
  return employees

def print_employee_list(employees):
  print("There are %d employees:" % (len(employees)))
  for employee in employees:
    print("%s - %d" % (employee, len(employee)))

def delete_employee(empl, employees):
  index = 0
  found = False
  for employee in employees:
    index = index + 1
    if employee == empl:
      found = True
      break
  if found:
    del employees[index-1]
  return employees

def get_employee_to_delete():
  employee=""
  while len(employee) == 0:
    employee = input("Enter an employee name to delete: ")
  return employee

def writeToFile(employees):
  file = open("employees.txt", "w")
  for employee in employees:
    file.write(employee)
    file.write("\n")

if __name__ == '__main__':
  main()
