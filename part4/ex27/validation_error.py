#!/usr/bin/python
from enum import Enum

class ValidationError(Enum):
  FIRSTNAME_EMPTY = 1
  FIRSTNAME_NOT_VALID = 2
  LASTNAME_EMPTY = 3
  LASTNAME_NOT_VALID = 4
  ZIP_EMPTY = 5
  ZIP_NOT_VALID = 6
  ID_EMPTY = 7
  ID_NOT_VALID = 8
  NONE = 9
