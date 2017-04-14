#/usr/bin/python

def isAnagram(first, second):
  if len(first) == 0 or len(second) == 0:
    return False
  if len(first) != len(second):
    return False

  i = 0
  while i < len(first):
    char = first[i]
    j = 0
    char_in_second = 0
    while j < len(second):
      if second[j] == char:
        char_in_second = char_in_second + 1
      j = j + 1
    if char_in_second  != 1:
      return False
    i = i + 1
  return True


