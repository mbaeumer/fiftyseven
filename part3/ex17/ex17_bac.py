#!/usr/bin/python
from bac_capture_input import capture_gender
from bac_capture_input import capture_ounces
from bac_capture_input import capture_weight
from bac_capture_input import capture_hours
from bac_calculator import calculate_bac

print("Exercise 17: BAC calculation")
print("")

gender = capture_gender()
ounces = capture_ounces()
weight = capture_weight()
hours = capture_hours()
result = calculate_bac(gender, ounces, weight, hours)

print("The result is %f " % (result))
