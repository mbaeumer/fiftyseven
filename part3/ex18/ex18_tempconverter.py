#!/usr/bin/python
from tempconverter import get_celsius
from tempconverter import get_fahrenheit

print("Exercise 18: Temperature converter")
print("")
target = ""
while target != "C" and target != "F":
  print("Press C to convert from Fahrenheit to Celsius")
  print("Press F to convert from Celsius to Fahrenheit")
  target = input("Your choice: ")

try:
  base_temp = "Fahrenheit"
  if target == "F":
    base_temp = "Celsius" 
  base_temp_value = float(input("Please enter the temperature in %s: " % (base_temp)))
  
  result = 0
  if target == "F":
    result = get_fahrenheit(base_temp_value)
  else:
    result = get_celsius(base_temp_value)

  print("The result: %f" % (result))
except ValueError as ex:
  print("Please enter a valid temperature!")

