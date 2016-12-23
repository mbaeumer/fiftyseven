#!/usr/bin/python

def get_pieces(num_pieces):
  result = ""
  if num_pieces < 2:
    result = "piece"
  else:
    result = "pieces"
  return result

def get_proper_be(num_leftovers):
  result = "are"
  if num_leftovers == 1:
    result = "is"
  return result

def get_pizzas(num_pizzas):
  result = "pizzas"
  if num_pizzas == 1:
    result = "pizza"
  return result

