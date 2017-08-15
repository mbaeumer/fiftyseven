#!/usr/bin/python

def get_string_value(question):
  value = ''
  while len(value) == 0:
    value = input(question)

  return value

def get_yes_no_answer(question):
  answers = ['y', 'n']
  answer = ''
  while answer not in answers:
    answer = input(question)

  return answer == 'y'
