#!/usr/bin/python
import math 

def calculate(principal, rate, years, compound_times):
  result = principal * (((1 + (rate/(100*compound_times))) ** (compound_times * years)))
  result = round(result, 2) 
  return result
