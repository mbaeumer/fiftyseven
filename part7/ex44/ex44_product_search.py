#!/usr/bin/python
from jsonreader import read_json_file
from jsonwriter import write_json_file
from product import Product
from inputhandler import get_string_input
from inputhandler import get_boolean_input
from inputhandler import get_int_input
from inputhandler import get_product_info
from producthandler import search_for_product
from producthandler import show_product_info

def main():
  print_title()
  products = read_json_file("products.json") 
  print_product_list(products)

  searchterm = get_string_input("What are you looking for? ")
  product = search_for_product(searchterm, products)
  if product != '':
    show_product_info(product)
  else:
    print("Sorry, the product could not be found!")
    product = get_product_info(searchterm)
    products.append(product)
    write_json_file("products.json", prepare_data_to_write(products))
    print("Finished writing data...")
    print_product_list(products)

def prepare_data_to_write(products):
  products_dict = []
  for p in products:
    products_dict.append(p.to_dict())
  data = {"products": products_dict}
  return data  

def print_product_list(products):
  for p in products:
    print("%s %d %d " % (p.name, p.price, p.quantity))

def create_dummy_product():
  product = Product("Dummy IPad", 3400, 44)
  return product

def print_title():
  print("Exercise 44: Product search")
  print("")

if __name__ == '__main__':
  main()
