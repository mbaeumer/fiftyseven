#!/usr/bin/python
from CurrencyConverter import CurrencyConverter

def get_as_currency(value):
  return '{:,.2f}'.format(value)

print("Exercise 11: Currency converter - v1")
print("")
try:
  value_in_euros = float(input("How many euros: "))
  conversion_rate = float(input("Conversion rate: "))
  converter = CurrencyConverter()
  value_in_dollars = converter.calculate(value_in_euros, conversion_rate)
  print("Value in dollars: %s " % (get_as_currency(value_in_dollars)))
except ValueError as ex:
  print("Sorry, you entered wrong values!")

  

