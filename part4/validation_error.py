#!/usr/bin/python
from enum import Enum

class ValidationError(Enum):
  FIRSTNAME_EMPTY,
  FIRSTNAME_TOO_SHORT,
  LASTNAME_EMPTY,
  LASTNAME_TOO_SHORT,
  ZIP_EMPTY,
  ZIP_NOT_VALID,
  ID_EMPTY,
  ID_NOT_VALID,

  NONE 
