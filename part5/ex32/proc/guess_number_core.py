#!/usr/bin/python
import random
from level import Difficulty
from comparison_result import ComparisonResult
 
def generate_my_number(difficulty_level):
  max = 10
  if difficulty_level == Difficulty.MEDIUM:
    max = 50
  elif difficulty_level == Difficulty.HARD:
    max = 100
  number = random.randint(0,max)  
  return number

# get the user's input as string
def get_user_guess(attempts):
  message = "What is your next guess: "
  if attempts == 1:
    message = "Make the first guess: "
  guess = input(message)
  return guess

def get_difficulty_level():
  choice = 0
  while choice < 1 or choice > 3:
    print("Select difficulty")
    print("Easy \t - 1")
    print("Medium \t - 2")
    print("Hard \t - 3")
    try:
      choice = int(input("Your choice: "))
    except ValueError:
      print("ERROR: Please enter a valid choice!")
      choice = 0
  difficulty_level = Difficulty(choice)
  print(difficulty_level)
  return difficulty_level

def get_play_again():
  user_input = ''
  while user_input != 'y' and user_input != 'n':
    user_input = input("Play again? ")
  return user_input == 'y'

def isValidGuess(guess_as_string):
  try:
    guess = int(guess_as_string)
    return True
  except ValueError:
    return False

def validateGuess(guess, my_number):
  if my_number > guess:
    return ComparisonResult.HIGHER
  elif my_number < guess:
    return ComparisonResult.LOWER
  return ComparisonResult.EQUAL

def get_validation_message(comparison_result):
  message = "You got it"
  if comparison_result == ComparisonResult.HIGHER:
    message = "The number is higher"    
  elif comparison_result == ComparisonResult.LOWER:  
    message = "The number is lower"
  return message

 
