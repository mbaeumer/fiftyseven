#!/usr/bin/python

class ShoppingCartItem:
  def __init__(self, quantity, price):
    self.quantity = quantity
    self.price = price

  def displayItem(self):
    print("Quantity: %d, Price: %f" % (self.quantity, self.price))

