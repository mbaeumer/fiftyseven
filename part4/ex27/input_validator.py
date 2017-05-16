#!/usr/bin/python
import re
from validation_error import ValidationError

def isZipValid(zip):
  if len(zip) == 0:
    return ValidationError.ZIP_EMPTY
  elif not re.match(r'^[0-9]{5}$', zip):
    return ValidationError.ZIP_NOT_VALID
  else:
    return ValidationError.NONE

def isStringValid(string, isFirst):
  if len(string) == 0:
    if isFirst:
      return ValidationError.FIRSTNAME_EMPTY
    else:
      return ValidationError.LASTNAME_EMPTY
  elif not re.match(r'^[a-zA-Z]{2,}$', string):
    if isFirst:
      return ValidationError.FIRSTNAME_NOT_VALID
    else:
      return ValidationError.LASTNAME_NOT_VALID
  else:
    return ValidationError.NONE

def isIdValid(id):
  if len(id) == 0:
    return ValidationError.ID_EMPTY
  elif not re.match(r'^[A-Z]{2}-[0-9]{4}', id):
    return ValidationError.ID_NOT_VALID
  else:
    return ValidationError.NONE
