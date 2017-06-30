#!/usr/bin/python
from inputsource import InputSource
from number_filter import filter_even_numbers
from filereader import read_file

def main():
  print_title()
  source = capture_input_source()
  if source == InputSource.PROMPT:
    row = capture_input_from_prompt()    
    filtered_values = filter_even_numbers(row)
  else:
    filename = capture_filename()
    filtered_values = read_file(filename)
  print("The result: ")
  print(filtered_values)
        
def print_title():
  print("Exercise 37: Filtering even numbers")
  print("")

def capture_input_source():
  choice = ''
  while choice != '1' and choice != '2':
    print("Choose the input source:")
    print("1 - Prompt")
    print("2 - File")
    choice = input("Your choice: ")
  return InputSource(int(choice))

def capture_filename():
  filename = ''
  while len(filename) == 0:
    filename = input("Enter a filename: ")
  return filename

def capture_input_from_prompt():
  return input("Enter some numbers: ")

if __name__ == '__main__':
  main()
