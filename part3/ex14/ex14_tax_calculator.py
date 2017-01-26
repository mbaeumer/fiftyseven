#!/usr/bin/python
from capture_user_input import get_order_value
from capture_user_input import get_state
from tax_calculator import calculate_tax
from tax_calculator import calculate_total

print("Exercise 14: Tax calculator")
print()

try:
  order_value = get_order_value()
  state = get_state()

  result = calculate_tax(order_value, state)
  total = calculate_total(order_value, result)

  output = ""
  if state == 'WI':
    output = "The subtotal is %f \n" % (order_value)
    output += "The tax is %f \n" % (result)
  output += "The total is %f" % (total)

  print(output)  

except ValueError as ex:
  print("Error: Invalid user input!")

