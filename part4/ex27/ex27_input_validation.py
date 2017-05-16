#!/usr/bin/python
from validation_error import ValidationError
from input_validator import isZipValid
from input_validator import isStringValid
from input_validator import isIdValid

def print_result(validation_firstname, validation_lastname, validation_zip, validation_id):
  if validation_firstname == ValidationError.FIRSTNAME_EMPTY:
    print("The firstname must not be empty")
  if validation_firstname == ValidationError.FIRSTNAME_NOT_VALID:
    print("The firstname is not valid")

  if validation_lastname == ValidationError.LASTNAME_EMPTY:
    print("The lastname must not be empty")
  elif validation_lastname == ValidationError.LASTNAME_NOT_VALID:
    print("The lastname is not valid")

  if validation_zip == ValidationError.ZIP_EMPTY:
    print("The zip code must not be empty")
  elif validation_zip == ValidationError.ZIP_NOT_VALID:
    print("The zip code is not valid")

  if validation_id == ValidationError.ID_EMPTY:
    print("The ID must not be empty")
  elif validation_id == ValidationError.ID_NOT_VALID:
    print("The ID is not valid")
  
  if validation_firstname == ValidationError.NONE and validation_lastname == ValidationError.NONE and validation.zip == ValidationError.NONE and validation_id == ValidationError.NONE:
    print("There was no error")

print("Exercise 27: Input validation")
print("")

firstname = input("Enter firstname: ")
lastname = input("Enter lastname: ")
zip = input("Enter zip code: ")
id = input("Enter id: ")

validation_firstname = isStringValid(firstname, True)
validation_lastname = isStringValid(lastname, False)
validation_zip = isZipValid(zip)
validation_id = isIdValid(id)
print_result(validation_firstname, validation_lastname, validation_zip, validation_id)



