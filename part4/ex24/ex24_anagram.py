#!/usr/bin/python
from anagram import isAnagram

print("Exercise 24: Anagram checker")
print("")

first = input("Enter the first string: ")
second = input("Enter the second string: ")

result = isAnagram(first, second)
if result:
  print("The words '%s' and '%s' are anagrams" % (first, second))
else:
  print("The words '%s' and '%s' are not anagrams" % (first, second))

