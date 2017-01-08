#!/usr/bin/python

def get_as_currency(value):
  return '{:,.2f}'.format(value)

def init_conversion_rates():
  conversion_rates = {}
  conversion_rates['us'] = 1.05
  conversion_rates['ch'] = 1.07
  conversion_rates['se'] = 9.55
  conversion_rates['no'] = 9.00
  return conversion_rates
  
def retrieve_value_in_euros():
  try:
    euros = float(input("How many euros? "))
  except ValueError as ex:
    raise ValueError
  return euros

def retrieve_user_input_conversion_rate():
  choice = ""
  while choice != "A" and choice != "B" and choice != "C" and choice != "D":
    print("SEK - A")
    print("US Dollars - B")
    print("Swiss Franc - C")
    print("NOK - D")
    print("---------------")
    choice = input("Your choice: ")
  return choice

def retrieve_conversion_rate(choice, conversion_rates):
  if choice == "A":
    return conversion_rates['se']
  elif choice == "B":
    return conversion_rates['us']
  elif choice == "C":
    return conversion_rates['ch']
  elif choice == "D":
    return conversion_rates['no']

def get_currency_name(choice):
  if choice == "A":
    return "Swedish Krona"
  elif choice == "B":
    return "US dollars"
  elif choice == "C":
    return "Swiss Franc"
  elif choice == "D":
    return "Norwegian Krone"

def calculate(euros, conversion_rate):
  return euros * conversion_rate

print("Exercise 11 - version 2")
print("")
conversion_rates = init_conversion_rates()
try:
  euros = retrieve_value_in_euros()
  choice = retrieve_user_input_conversion_rate()
  conversion_rate = retrieve_conversion_rate(choice, conversion_rates)
  result = calculate(euros, conversion_rate)
  print("%s euros at an exchange rate of %s is %s %s" % (get_as_currency(euros), get_as_currency(conversion_rate), get_as_currency(result), get_currency_name(choice)))
except ValueError as ex:
  print("Sorry, you entered a wrong value!")




