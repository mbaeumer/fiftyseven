#/usr/bin/python

def calculate_bac(gender, amount, weight, hours):
  r = 0.73
  if gender == "w":
    r = 0.66
  bac = (amount * 5.14/(weight * r)) - 0.015 * hours
  return bac
