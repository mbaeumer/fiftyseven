#!/usr/bin/python
from driving_age_handler import init_driving_age_info
from driving_age_handler import print_driving_age_for_country

print("Exercise 16: Driving age checker")
print("")

try:
  age = int(input("Enter your age: "))
  if age < 0:
    raise ValueError
  driving_age_info = init_driving_age_info()
  print_driving_age_for_country(age, driving_age_info)

except ValueError as ex:
  print("Error! You did not enter a valid age")
