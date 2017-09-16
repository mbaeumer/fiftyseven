#!/usr/bin/python
from file_reader import read_file
from datetime import datetime
from frequencyresult import FrequencyResult
from operator import itemgetter

def main():
  print_title()
  filename = "macbeth.txt"
  content = read_file(filename)
  frequencyresult = process_data(content)
  print_result(frequencyresult)

def process_data(content):
  starttime = datetime.now()
  words = {}
  rows = content.split("\n")
  for row in rows:
    splitted = row.split(" ")
    for word in splitted:
      if len(word) > 0:
        if word in words:
          frequency = words[word]
          frequency = frequency + 1
          words[word] = frequency
        else:
          words[word] = 1 
  endtime = datetime.now()
  frequencyresult = FrequencyResult(words, starttime, endtime)
  return frequencyresult

def print_result(frequencyresult):
  for k, v in sorted(frequencyresult.words.items(), key=itemgetter(1), reverse = True):
    print(k, v)
  print(frequencyresult.get_time_elapsed())
  print(len(frequencyresult.words))

def print_title():
  print("Exercise 46: Word frequency finder - version 1 \n")
  
if __name__ == '__main__':
  main()

