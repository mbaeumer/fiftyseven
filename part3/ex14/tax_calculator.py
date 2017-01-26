#!/usr/bin/python
import math

def calculate_tax(order_value, state):
  result = 0
  if state == "WI":
    result = order_value * (5.5/100)
    result = round(result, 2)
  return result

def calculate_total(order_value, tax_value):
  return order_value + tax_value
