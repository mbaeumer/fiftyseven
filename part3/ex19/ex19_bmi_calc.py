#!/usr/bin/python
from bmi_calc_core import get_bmi
from bmi_calc_core import capture_weight
from bmi_calc_core import capture_length
from bmi_calc_core import get_bmi_level

print("Exercise 19: BMI Calculator")
print("")
try:
  isInputCorrect = True
  weight = capture_weight()
  if weight < 0:
    print("The weight mut bee larger than 0!")
    isInputCorrect = False

  length = capture_length()
  if length < 0:
    print("The length must be larger than 0!")
    isInputCorrect = False
  
  if isInputCorrect:
    bmi = get_bmi(weight, length)
    print("Your BMI is %f" % (bmi))
    print(get_bmi_level(bmi))
except ValueError as ex:
  print("Enter a correct value for weight and length")
