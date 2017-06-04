#!/usr/bin/python
from guess_number_core import generate_my_number
from guess_number_core import isValidGuess
from guess_number_core import validateGuess
from guess_number_core import get_user_guess
from guess_number_core import get_validation_message
from guess_number_core import get_difficulty_level
from guess_number_core import get_play_again
from level import Difficulty
from comparison_result import ComparisonResult

def main():
  print_title()
  difficulty_level = get_difficulty_level()
  play_again = True
  while play_again:
    play(difficulty_level)
    play_again = get_play_again()

def play(difficulty_level):
  my_number = generate_my_number(difficulty_level)
  attempts = 0
  status = ComparisonResult.HIGHER
  while status != ComparisonResult.EQUAL:
    current_user_guess = ''
    while not isValidGuess(current_user_guess):
      attempts = attempts + 1
      current_user_guess = get_user_guess(attempts)

    current_user_guess = int(current_user_guess)
    status = validateGuess(current_user_guess, my_number)
    message = get_validation_message(status)
    print("Attempts: %d - %s " % (attempts, message))
  print("FINISHED")
  
def print_title():
  print("Exercise 32: Guess the number (procedural version)")
  print("")

if __name__ == '__main__':
  main()
