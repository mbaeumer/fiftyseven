#!/usr/bin/python
from area_calculator import convert_to_m2
from area_calculator import get_area

try:
  length = float(input("The length of the room in feet: "))
  width = float(input("The width of the room in feet: "))
  area = get_area(length, width)
  print("You entered dimensions of %f feet by %f feet" % (length, width))
  print("The area is\n")
  print("%f square feet" % (area))
  m2 = convert_to_m2(area)
  print("%f square meters" % (m2))
except ValueError as ex:
  print("Enter valid length and width!")
