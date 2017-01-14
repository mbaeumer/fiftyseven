#!/usr/bin/python

def calculate(principal, rate, years):
  result = principal * (1 + (rate/100)*years)
  return result
