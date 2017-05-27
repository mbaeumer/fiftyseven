#!/usr/bin/python

def capture_age():
  correct = False
  age = 0
  while not correct:
    try:
      age = int(input("Your age: "))
      if age < 0 or age > 120:
        print("ERROR: Please enter a reasonable age!")
      else:
        correct = True
    except ValueError:
      print("ERROR: Please enter a numeric value!")
  return age

def capture_resting_heart_rate():
  correct = False
  heart_rate = 0
  while not correct:
    try:
      heart_rate = int(input("Your resting heart rate: "))
      if heart_rate < 40 or heart_rate > 160:
        print("ERROR: Please enter a reasonable heart rate!")
      else:
        correct = True
    except ValueError:
      print("ERROR: Please enter a numeric value!")
  return heart_rate
  
