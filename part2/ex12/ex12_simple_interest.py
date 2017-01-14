#!/usr/bin/python
from capture_user_input import get_principal
from capture_user_input import get_interest_rate
from capture_user_input import get_years
from calculate_interest import calculate

print("Exercise12: Calculating simple interest")
print()

try:
  principal = get_principal()
  interest_rate = get_interest_rate()
  years = get_years()

  result = calculate(principal, interest_rate, years)
  
  print("After %d years at %f the investment will be worth %f " % (years, interest_rate, result))
except ValueError as ex:
  print("Error: Invalid user input!")

