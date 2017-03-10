#!/usr/bin/python

def get_bmi(weight, length):
  result =  (weight/length/length)*10000
  result = round(result, 1)
  return result

def capture_weight():
  weight = float(input("Enter your weight: "))
  return weight

def capture_length():
  length = float(input("Enter yor length: "))
  return length

def get_bmi_level(bmi):
  result = "Your result is ok"
  if bmi < 18.5:
    result = "You are underweight"
  elif bmi > 25:
    result = "You are overweight"
  return result
    
