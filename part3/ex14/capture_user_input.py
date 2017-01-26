#!/usr/bin/python

def get_order_value():
  try:
    value = int(input("What is the order value? "))
    if value < 0:
      raise ValueError('Invalid order amount')
    return value
  except ValueError as ex:
    raise ValueError('Invalid order value')

def get_state():
  state = input("What is the state? ")
  if state == '':
    raise ValueError('Invalid state')
  return state
