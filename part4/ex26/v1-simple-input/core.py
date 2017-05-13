#!/usr/bin/python
from math import log
from math import ceil

def calculateMonths(balance, apr, downpayment):
  i = (apr/100)/365
  result = -1/30 * log(1 + balance/downpayment*(1-(1+i)**30))/log(1+i)
  result = ceil(result)
  print(result)
  return result

