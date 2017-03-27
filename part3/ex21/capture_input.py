#!/usr/bin/python

def capture_month_number():
  month = 0
  while month < 1 or month > 12:
    try: 
      month = int(input("Enter the number of the month: "))
    except ValueError as ex:
      month = 0
  return str(month)
