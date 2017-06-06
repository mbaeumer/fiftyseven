#!/usr/bin/python

def main():
  print_title()
  employees = init_employee_list()
  print_employee_list(employees)
  selected = get_employee_to_delete()
  if selected in employees:
    employees = delete_employee(selected, employees)
    print_employee_list(employees)
  else:
    print("Sorry, the employee '%s' does not exist!" % (selected))
    
  

def print_title():
  print("Exercise 34: Employee list")
  print("")

def init_employee_list():
  employees = []
  employees.append('John Doe')
  employees.append('Bill Gates')
  employees.append('Steve Jobs')
  employees.append('Linus Thorvald')
  return employees

def print_employee_list(employees):
  print("There are %d employees:" % (len(employees)))
  for employee in employees:
    print(employee)

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


if __name__ == '__main__':
  main()
