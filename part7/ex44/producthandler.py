#!/usr/bin/python
from product import Product

def search_for_product(searchterm, products):
  result = ''
  for p in products:
    if p.name.lower() == searchterm.lower():
      result = p

  return result

def show_product_info(product):
  print("Product information")
  print("Name: %s " % (product.name))
  print("Price: %f " % (product.price))
  print("Quantity: %d " % (product.quantity))

