#!/usr/bin/python
import os
from file_reader import read_file
from file_writer import write_file

def main():
  input_file = "test.txt"
  try:
    output_file = get_output_file_name()
    content = read_file(input_file)
    print(content)
    content = replace(content)
    print(content)
    write_file(output_file, content)
    print("Finished writing content to %s" % (output_file))
  except FileNotFoundError:
    print("ERROR: The file does not exist")

def print_title():
  print("Exercise 45: Word finder")
  print("")

def replace(content):
  content = content.replace("utilize", "use")
  return content

def get_output_file_name():
  output_file = ''
  correct = False
  while not correct:
    correct = True
    output_file = input("Enter the name of the output file: ")
    if len(output_file) == 0:
      print("ERROR: Please enter a filename!")
      correct = False
    if os.path.exists(output_file):
      print("ERROR: The file %s already exists" % (output_file))
      correct = False
    if not output_file.endswith(".txt"):
      print("ERROR: The filename %s is not correct!" % (output_file))
      correct = False
  return output_file
  
if __name__ == '__main__':
  main()
