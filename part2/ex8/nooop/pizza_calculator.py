#!/usr/bin/python

def get_total_slices(num_pizzas):
  result = num_pizzas*8
  return result

def get_slices_per_person(total_slices, num_people):
  result = total_slices/num_people
  return result

def get_leftovers(total_slices, num_people):
  result = total_slices % num_people
  return result
