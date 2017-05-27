#!/usr/bin/python

def calculate_target_heart_rate(intensity, resting_heart_rate, age):
  return int((((220 - age) - resting_heart_rate) * intensity/100) + resting_heart_rate)
