#!/usr/bin/python

def capture_integers(count=5):
  i = 0
  numbers = []
  while i < count:
    try:
      number = int(input("Enter a number: "))
      numbers.append(number)
      i = i + 1
    except ValueError:
      print("Add a valid number")
  return numbers

def capture_count():
  count = 0
  correct = False
  while not correct:
    try:
      count = int(input("How many numbers you want to enter: "))
      if count < 1:
        raise ValueError
      correct = True 
    except ValueError:
      print("Please type a valid number!")
  return count

def calc_total(numbers):
  total = 0
  for number in numbers:
    total = total + number  
  return total


print("Exercise 28: Adding numbers")
print()

print("Static addition: ")
numbers = capture_integers()
total = calc_total(numbers)
print("The total is %d." % (total))
print("")
print("Dynamic addition: ")
count = capture_count()
numbers = capture_integers(count)
total = calc_total(numbers)
print("The total is %d." % (total))


