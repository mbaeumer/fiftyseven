#!/usr/bin/python
import re

def isZipValid(zip):
  return len(zip)>0 and re.match(r'^[0-9]{5}$', zip) 
