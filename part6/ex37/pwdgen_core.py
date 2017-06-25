#!/usr/bin/python
from chartype import CharType
import re
import random 

def generate_letter_list():
  letters = []
  letters.append('a')
  letters.append('b')
  letters.append('c')
  letters.append('d')
  letters.append('e')
  letters.append('f')
  letters.append('g')
  letters.append('h')
  letters.append('i')
  letters.append('j')
  letters.append('k')
  letters.append('l')
  letters.append('m')
  letters.append('n')
  letters.append('o')
  letters.append('p')
  letters.append('q')
  letters.append('r')
  letters.append('s')
  letters.append('t')
  letters.append('u')
  letters.append('v')
  letters.append('w')
  letters.append('x')
  letters.append('x')
  letters.append('y')
  letters.append('z')
  return letters

def generate_special_chars():
  specials = []
  specials.append('$')
  specials.append('#')
  specials.append('+')
  specials.append('_')
  specials.append('-')
  specials.append('!')
  return specials

def generate_password(min_length, min_numbers, min_specials):
  letters = generate_letter_list()
  specials = generate_special_chars()

  password = ''
  while len(password) < min_length:
    chartype = pick_character_type(password, min_length, min_numbers, min_specials)
    if chartype == CharType.LETTER:
      letter = pick_character(letters)
      password = password + letter    
    elif chartype == CharType.SPECIAL:
      special = pick_character(specials)
      password = password + special
    else:
      number = random.randint(0, 9)
      password = password + str(number)

  return password

def pick_character(character_list):
  character = ''
  index = random.randint(0, len(character_list) - 1)
  return character_list[index]

def pick_character_type(password, min_length, min_numbers, min_specials):
  chartype = CharType.LETTER
  max_random = 10
  rand = random.randint(1, max_random)
  probability_numbers = pick_probability_for_numbers(password, min_numbers)
  probability_specials = probability_numbers + pick_probability_for_specials(password, min_specials)
  if rand <= probability_numbers:
    chartype =  CharType.NUMBER
  elif rand > probability_numbers and rand <= probability_specials:
    chartype =  CharType.SPECIAL

  return chartype

def pick_probability_for_numbers(password, min_numbers):
  probability = 1
  if not hasEnoughNumbers(password, min_numbers):
    probability = 5
  return probability

def pick_probability_for_specials(password, min_specials):
  probability = 1
  if not hasEnoughSpecialChars(password, min_specials):
    probability = 5
  return probability

def hasEnoughNumbers(password, min_numbers):
  numbers = re.findall(r'\d', password)
  return len(numbers) >= min_numbers

def hasEnoughSpecialChars(password, min_specials):
  specials = re.findall(r'[-#\+_!$]', password)
  return len(specials) >= min_specials

