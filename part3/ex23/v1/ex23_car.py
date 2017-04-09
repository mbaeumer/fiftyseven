#!/usr/bin/python

def capture_input(question):
  user_input = ""
  while user_input != 'y' and user_input != 'n':
    user_input = input(question)
    user_input = user_input.lower()
  return user_input

def print_suggestion(suggestion):
  print(suggestion)

print("Exercise 23: Car troubleshooting")
print("")

step1 = capture_input("Is the car silent when you turn the key?")
if step1 == 'y':
  step2 = capture_input("Are the battery terminals corroded?")
  if step2 == 'y':
    print_suggestion("Clean terminals and try again")
  else:
    print_suggestion("Replace cables and try again")
else:
  step3 = capture_input("Does the car make a clickhing noise?")
  if step3 == 'y':
    print_suggesstion("Replace the battery")
  else:
    step4 = capture_input("Does the car crank up but fails to start?")
    if step4 == 'y':
      print_suggestion("Check spark plug connections")
    else:
      step5 = capture_input("Does the engine start and then die?")
      if step5 == 'y':
        step6 = capture_input("Does your car have fuel injection?")
        if step6 == 'n':
          print_suggestion("Check to ensure the choke and opening and closing")
        else:
          print_suggestion("Get it in for service")
      else:
        print_suggestion("Sorry I am running out of ideas")
    
