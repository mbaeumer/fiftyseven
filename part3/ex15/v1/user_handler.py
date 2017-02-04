#!/usr/bin/python

def create_user_dictionary():
  users = {}
  users['user1']="pwd1"
  users['user2']="pwd2"
  users['user3']="pwd3"
  users['user4']="PWD4"
  return users

def lookup_user(user, password, user_dictionary):
  result = "Login failed"
  if (user in user_dictionary):
    if (user_dictionary[user] == password):
      result = "Login succeeded"
  return result
