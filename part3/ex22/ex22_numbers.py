#!/usr/bin/python

print("Exercise 22: Comparing numbers")
print("")

numbers = []
user_input = ""
while user_input != "X":
  try:
    user_input = input("Enter a number (X=Cancel): ")
    number = int(user_input)
    if numbers.count(number) == 0:
      numbers.append(number)
    else:
      print("The number %s exists. Skipped!" % (number))
  except ValueError as ex:
    if user_input != "X":
      print("Please enter a valid number!")

max = numbers[0]
for number in numbers:
  if number > max:
    max = number
print("The largest element in the list is %d" % (max))
