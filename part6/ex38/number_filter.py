#!/usr/bin/python

def filter_even_numbers(row):
  entries = row.split(" ")
  numbers = []
  for entry in entries:
    try:
      number = int(entry)
      if number % 2 == 0:
        numbers.append(number)
    except ValueError:
      print("INFO: Wrong input")
  return numbers
