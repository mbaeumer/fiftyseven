#!/usr/bin/python
import os
import re
from file_reader import read_file
from file_writer import write_file
from config_handler import get_replace_config
from replacement_result import ReplacementResult

def main():
  input_file = "test.txt"
  try:
    output_file = get_output_file_name()
    content = read_file(input_file)
    print(content)
    replacement_result = replace(content, get_replace_config())
    print(replacement_result.content)
    write_file(output_file, replacement_result.content)
    print("Finished writing content to %s" % (output_file))
    print_replacement_result(replacement_result)
  except FileNotFoundError:
    print("ERROR: The file does not exist")

def print_title():
  print("Exercise 45: Word finder")
  print("version 2 with a replacement config and replacement statistics")
  print("")

def replace(content, replacement_config):
  for r in replacement_config:
    r.occurence = len(re.findall(r.to_replace, content))
    content = content.replace(r.to_replace, r.replaced_by)

  replacement_result = ReplacementResult(replacement_config, content)
  return replacement_result

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

def print_replacement_result(replacement_result):
  for rc in replacement_result.config:
    print("Replaced %s by %s %d times" % (rc.to_replace, rc.replaced_by, rc.occurence))  

if __name__ == '__main__':
  main()
