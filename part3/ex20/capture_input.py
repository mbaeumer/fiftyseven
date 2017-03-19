#!/usr/bin/python

def capture_country():
  country = ""
  while country != "1" and country != "2" and country != "3" and country != "4" and country != "5" and country != "X":
    print("Select a country:")
    print("----------------")
    print("Sweden - 1")
    print("Denmark - 2")
    print("Norway - 3")
    print("Finland - 4")
    print("Germany - 5")
    country = input("Your choice (X=Cancel): ")
  return country

def capture_order_value():
  try:
    value = float(input("Enter the order value: "))
    if value < 0:
      raise ValueError("Negative order value is not allowed!")
    return value
  except ValueError as ex:
    raise ValueError("Invalid order value!")

