#!/usr/bin/python
from passwordstrength import PasswordStrength
from pwd_val import validatePassword

def print_result(strength):
  if strength == PasswordStrength.VERY_WEAK:
    print("The password is very weak!")
  elif strength == PasswordStrength.WEAK:
    print("The password is weak!")
  elif strength == PasswordStrength.STRONG:
    print("The password is strong!")
  elif strength == PasswordStrength.VERY_STRONG:
    print("The password is very strong!")

print("Exercise 25: Password strength checker")
print("")
password = input("Enter a potential password: ")
strength = validatePassword(password)
print_result(strength)

