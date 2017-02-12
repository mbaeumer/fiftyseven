#!/usr/bin/python

def init_driving_age_info():
  driving_age_info = {}
  driving_age_info['Sweden'] = 18
  driving_age_info['Brazil'] = 16
  driving_age_info['USA'] = 16 
  driving_age_info['Jamaica'] = 15
  driving_age_info['Germany'] = 18
  return driving_age_info

def print_driving_age_for_country(age, driving_age_info):
  for k,v in driving_age_info.items():
    result = "you are allowed to drive" if age >= v else "you are not allowed to drive"
    print("In %s %s" % (k, result))
