#!/usr/bin/python
import datetime

def current_year():
  now = datetime.datetime.now()
  year = now.year
  return year  

print("Exercise 6: Retirement calculator")
print("")
try:
  age = int(input("What is your current age? "))
  retirement_age = int(input("At what age would you like to retire? "))
  if retirement_age < age:
    print("You should be retired already!")
  else:
    remaining_years = retirement_age - age
    year = current_year()
    retirement_year = year + remaining_years 
    print("You have %d years left until you can retire." % (remaining_years))
    print("It is %d, so you can retire in %d" % (year, retirement_year))
except ValueError as ex:
  print("Please enter a valid age")
