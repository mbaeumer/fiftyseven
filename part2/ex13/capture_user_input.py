#!/usr/bin/python

def get_principal():
  try:
    principal = float(input("Enter the principal: "))
    return principal
  except ValueError as ex:
    raise ValueError('Invalid principal')

def get_interest_rate():
  try:
    rate = float(input("Enter the interest rate: "))
    return rate
  except ValueError as ex:
    raise ValueError('Invalid input for interest rate')

def get_years():
  try:
    years = int(input("Enter the number of years: "))
    return years
  except ValueError as ex:
    raise ValueError('Invalid value for years')
  except TypeError as e:
    raise TypeError

def get_compound_times():
  try:
    compound_times = int(input("How many times will the interest be compounded?"))
    return compound_times
  except ValueError as ex:
    raise ValueError
