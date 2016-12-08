#!/usr/bin/python

print("Exercise 5: simple math")
print("")
try:
  str_a = input("Enter the first number: ")
  str_b = input("Enter the second number: ")
  a = int(str_a)
  b = int(str_b)
  addition = a+b
  subtraction = a-b
  multiplication = a*b
  division = a/b

  print("%s+%s=%d\n%s-%s=%d\n%s*%s=%d\n%s/%s=%d" % (str_a,str_b,addition,str_a,str_b,subtraction,str_a,str_b,multiplication,str_a,str_b,division))
except ValueError as ex:
  print("Please enter a valid number!")
except ZeroDivisionError as ex:
  print("The second number must not be 0!") 
