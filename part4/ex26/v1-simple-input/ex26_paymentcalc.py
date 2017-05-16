#!/usr/bin/python
from core import calculateMonths

def capture_balance():
  finished = False
  while not finished:
    str_balance = input("What is the balance on the card? ")
    if str_balance != 'X':
      try:
        balance = float(str_balance)
        if balance < 0:
          print("ERROR: Please provide a positive value for the balance!")
        else:
          finished = True
          return balance
      except ValueError:
        print("ERROR: Please provide a correct value for the balance!")
    else:
      finished = True
      return str_balance

def capture_apr():
  finished = False
  while not finished:
    str_apr = input("What is the APR of the card? ")
    if str_apr != 'X':
      try:
        apr = int(str_apr)
        if apr < 0:
          print("ERROR: Please provide a positive value for the APR!")
        else:
          finished = True
          return apr
      except ValueError:
        print("ERROR: Please provide a correct value for the APR!")
    else:
      finished = True
      return str_apr

def capture_monthly_payment():
  finished = False
  while not finished:
    str_pay = input("What is the your monthly payment? ")
    if str_pay != 'X':
      try:
        pay = float(str_pay)
        if pay < 0:
          print("ERROR: Please provide a positive value for your monthly payment!")
        else:
          finished = True
          return pay
      except ValueError:
        print("ERROR: Please provide a correct value for your monthly payment!")
    else:
      finished = True
      return str_pay


print("Exercise 26: Payment calculator")
print("")
balance = 0
apr = 0
monthly_payment = 0
cancelled = False
balance = capture_balance()
if balance == 'X':
  cancelled = True
  print("The user cancelled. Application exit")
else:
  apr = capture_apr()
  if apr == 'X':
    cancelled = True
    print("The user cancelled. Application exit")
  else:
    monthly_payment = capture_monthly_payment()
    if monthly_payment == 'X':
      cancelled = True
      print("The user cancelled. Application exit")
     
if not cancelled:
  result = calculateMonths(balance, apr, monthly_payment)
  print("It will take %d months" % (result))

