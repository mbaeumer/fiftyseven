#!/usr/bin/python
from paint_calculator import get_area
from paint_calculator import calculate_paint

print("Exercise 9: Paint calculator")
print("")

try:
  length = int(input("Length: "))
  width = int(input("Width: "))
  
  if length < 0 or width < 0:
    raise ValueError 

  area = get_area(length, width)  
  paint = calculate_paint(area)

  print("You will need to purchase %d gallons of paint to cover %d square feet" % (paint, area))
except ValueError as ex:
  print("Terminated due to failed input!")
