#!/usr/bin/python
import random

def get_users_question():
  question = ''
  question = input("What is your question (leave blank to exit)? ")
  return question

def init_answers():
  answers = []
  answers.append('Yes')
  answers.append('No')
  answers.append('Maybe')
  answers.append('Ask again later!')
  return answers


def select_answer(list):
  index = random.randint(0,len(list)-1)
  return list[index]
  
