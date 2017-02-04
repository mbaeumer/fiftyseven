#!/usr/bin/python
import getpass
from user_handler import create_user_dictionary
from user_handler import lookup_user

print("Exercise 15: Password")
print()
username = input("Enter your username: ")
pwd = getpass.getpass("Enter your password: ")
user_dictionary = create_user_dictionary()
result = lookup_user(username, pwd, user_dictionary)
print(result)


