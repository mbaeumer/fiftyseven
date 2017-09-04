#!/usr/bin/python

def read_file(filename):
  content = ''
  try:
    file = open(filename, "r")
    for line in file:
      content = content + line
    file.close()
  except FileNotFoundError as e:
    raise FileNotFoundError
  return content
