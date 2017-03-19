#!/usr/bin/python
import math

def init_tax_table():
  tax_table = {}
  tax_table['1'] = 25 
  tax_table['2'] = 25
  tax_table['3'] = 25
  tax_table['4'] = 24
  tax_table['5'] = 19
  return tax_table

def calculate_tax(order_value, tax_rate):
  result = order_value * (tax_rate/100)
  result = round(result,2)
  return result

def get_tax_rate(tax_table, country):
  if country in tax_table:
    return tax_table[country]
  else:
    print("key: %s" % (country) )
    raise KeyError("The key does not exist")

def calculate_total(order_value, tax_value):
  total = round(order_value + tax_value,2)
  return total



