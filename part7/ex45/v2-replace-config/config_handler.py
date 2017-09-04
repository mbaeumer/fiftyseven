#!/usr/bin/pyhon
from replacement_matcher import Replacement

def get_replace_config():
  config = []
  config.append(Replacement("are", "is", 0))
  config.append(Replacement("don't", "do not", 0))
  config.append(Replacement("Lorem Ipsum", "Ipsum Lorem", 0))
  return config
