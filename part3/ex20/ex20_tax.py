#!/usr/bin/python
from capture_input import capture_country
from capture_input import capture_order_value 
from tax_calculator import init_tax_table
from tax_calculator import get_tax_rate
from tax_calculator import calculate_tax
from tax_calculator import calculate_total

print("Exercise 20: Tax calculator")
print("")

try:
  country_code = capture_country()
  if country_code != "X":
    order_value = capture_order_value()
    tax_table = init_tax_table()
    tax_rate = get_tax_rate(tax_table, country_code)
    tax_value = calculate_tax(order_value, tax_rate)
    total = calculate_total(order_value, tax_value)    
    print("Total: %f" % (total))

except ValueError as ex:
  print("Error! Please enter valid stuff!")

