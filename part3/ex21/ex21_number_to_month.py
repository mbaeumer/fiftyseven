#!/usr/bin/python
from month_calculator import init_month_table
from month_calculator import get_month
from capture_input import capture_month_number

print("Exercise 21: Number to month")
print("")

months = init_month_table()
month = capture_month_number()
result = get_month(months, month)
print("The name of the month is %s" % (result))
