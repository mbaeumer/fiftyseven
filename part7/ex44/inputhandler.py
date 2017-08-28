#!/usr/bin/python
from product import Product

def get_string_input(question):
  result = ''
  while len(result) == 0:
    result = input(question)
  return result

def get_boolean_input(question):
  alts = []
  alts.append("y")
  alts.append("n")
  answer = ''
  while answer not in alts:
    answer = input(question)
  return answer == 'y'

def get_int_input(question):
  result = 0
  correct = False
  while not correct:
    try:
      result = int(input(question))
      if result >= 0:
        correct = True
    except ValueError:
      print("ERROR: Please provide a correct value!")
  return result 

def get_float_input(question):
  result = 0
  correct = False
  while not correct:
    try:
      result = float(input(question))
      if result >= 0:
        correct = True
    except ValueError:
      print("ERROR: Please enter a correct value!")
  return result

def get_product_info(productname):
  product = ''
  price = get_float_input("What is the price? ")
  quantity = get_int_input("What is the quantity? ")
  product = Product(productname, price, quantity)
  return product
