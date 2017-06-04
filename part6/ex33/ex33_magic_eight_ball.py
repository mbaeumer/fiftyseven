#!/usr/bin/python
from magic_core import get_users_question
from magic_core import init_answers
from magic_core import select_answer

def main():
  print_title()
  answers = init_answers()
  question = get_users_question()
  while len(question) > 0:
    answer = select_answer(answers)
    print(answer)
    question = get_users_question()
  print("You decided to exit! Good bye")

def print_title():
  print("Exercise 33: Magic eight ball")
  print()

if __name__ == '__main__':
  main()
