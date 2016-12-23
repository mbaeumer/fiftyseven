#!/usr/bin/python
from pizza_calculator import get_total_slices
from pizza_calculator import get_slices_per_person
from pizza_calculator import get_leftovers
from pluralization import get_pieces
from pluralization import get_proper_be
from pluralization import get_pizzas

print("Exercise 8: Pizza exercise")
print("")
try:
  num_people = int(input("How many people? "))
  num_pizza = int(input("How many pizzas? "))

  if num_people < 0:
    print("Please enter a valid number of people!")
    raise ValueError

  if num_pizza < 1:
    print("Please enter a valid number of pizzas!")
    raise ValueError

  print("%d people with %d %s" % (num_people, num_pizza, get_pizzas(num_pizza)))

  total_slices = get_total_slices(num_pizza)
  slices_per_person = get_slices_per_person(total_slices, num_people)
  leftovers = get_leftovers(total_slices, num_people)
  
  print("Each person gets %d %s of pizza." % (slices_per_person, get_pieces(slices_per_person)))
  print("There %s %d leftover %s." % (get_proper_be(leftovers), leftovers, get_pieces(leftovers)))

except ValueError as ex:
  print("Terminated due to fatal input!")

