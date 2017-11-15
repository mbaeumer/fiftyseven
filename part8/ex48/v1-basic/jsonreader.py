#!/usr/bin/python
import json
from city import City

def read_json_file(filename):
  with open(filename) as data_file:    
    data = json.load(data_file)

  cities = []
  for d in data:
    if d['country']  == 'SE':
      coords = d["coord"]
      city = City(str(d['id']), d['name'], d['country'], coords['lon'], coords['lat'])
      cities.append(city)
  return cities
