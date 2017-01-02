#!/usr/bin/python
from shoppingcartitem import ShoppingCartItem

def enterItems():
  items = []
  userinput = ""
  while userinput != "X":
    try:
      price = input("Enter the price: ")
      quantity = input("Enter the quantity: ")
      if price != "X" and quantity != "X":
        num_price = float(price)
        num_quantity = int(quantity)

        if num_price < 0 or num_quantity < 0:
          raise ValueError
        item = ShoppingCartItem(num_quantity, num_price)
        items.append(item)
      else:
        userinput = "X"
    except ValueError as ex:
      print("Your input is invalid!")
  return items

def calculate_subtotal(items):
  print("Calculating the subtotal...")
  subtotal = 0
  for item in items:
    subtotal += item.quantity * item.price
  return subtotal

def calculate_tax(subtotal):
  result = subtotal * 5.5/100
  return float(result)


print("Exercise 10: Self checkout")
print("")
items = enterItems()
subtotal = calculate_subtotal(items)
print("Subtotal: %f" % (subtotal))
tax = calculate_tax(subtotal)
print("Tax: %f" % (tax))
total = subtotal + tax
print("Total: %f" % (total))
