#!/usr/bin/python
import math

def get_area(length, width):
  return length*width

def calculate_paint(area):
  result = 0
  result = math.ceil(area / 350)
  return result
  
