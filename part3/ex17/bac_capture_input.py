#!/usr/bin/python

def capture_gender():
  gender = ""
  while not gender == "m" and not gender == "f":
    gender = input("Male or female? (m/f) ")
  return gender

def capture_ounces():
  inputCorrect = False
  while not inputCorrect:
    try:
      ounces = float(input("How many ounces did you drink? "))
      if ounces > 0:
        inputCorrect = True
    except ValueError as ex:
      inputCorrect = False
  return ounces

def capture_weight():
  inputCorrect = False
  while not inputCorrect:
    try:
      weight = float(input("What is your current weight? "))
      if weight > 0:
        inputCorrect = True
    except ValueError as ex:
      inputCorrect = False
  return weight

def capture_hours():
  inputCorrect = False
  while not inputCorrect:
    try:
      hours = int(input("How many hours since you drank? "))
      if hours > 0:
        inputCorrect = True
    except ValueError as ex:
      inputCorrect = False
  return hours


#result = (a * 5.14/W*r) - 0.015*H
#r = 0.73 men, 0.66 women 
