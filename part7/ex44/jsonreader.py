#!/usr/bin/python
import json
from product import Product

def read_json_file(filename):
  with open(filename) as data_file:    
    data = json.load(data_file)
  products_json = data["products"]
  products = []
  for p in products_json:
    product = Product(p['name'], p['price'], p['quantity'])
    products.append(product)
  return products

