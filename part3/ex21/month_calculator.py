#!/usr/bin/python

def init_month_table():
  months = {}
  months['1'] = "January"
  months['2'] = "February"
  months['3'] = "March"
  months['4'] = "April"
  months['5'] = "May"
  months['6'] = "June"
  months['7'] = "July"
  months['8'] = "August"
  months['9'] = "September"
  months['10'] = "October"
  months['11'] = "November"
  months['12'] = "December"
  return months

def get_month(months, number):
  return months[number]
