#!/usr/bin/python
import re
from passwordstrength import PasswordStrength

def validatePassword(password):
  if password.isdigit():
    return PasswordStrength.VERY_WEAK
  elif password.isalpha():
    return PasswordStrength.WEAK
  elif re.match(r'^[\w\d_-]+$', password):
    return PasswordStrength.STRONG
  elif re.findall(r'[~!@#$%^&\*()_+=-`]', password):
    return PasswordStrength.VERY_STRONG

