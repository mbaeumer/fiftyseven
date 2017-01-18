#!/usr/bin/python
from capture_user_input import get_principal
from capture_user_input import get_interest_rate
from capture_user_input import get_years
from capture_user_input import get_compound_times
from calculate_interest import calculate

print("Exercise13: Calculating compound interest")
print()

try:
  principal = get_principal()
  interest_rate = get_interest_rate()
  years = get_years()
  compound_times = get_compound_times()

  result = calculate(principal, interest_rate, years, compound_times)
  
  print("After %d years and compounded %d times per year at %f the investment will be worth %f " % (years, compound_times, interest_rate, result))
except ValueError as ex:
  print("Error: Invalid user input!")

