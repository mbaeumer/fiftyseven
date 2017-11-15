#!/usr/bin/python
from requestutil import get_raw_data
from jsonreader import read_json_file
from userinputhandler import get_string_input
from userinputhandler import select_city
from city_util import get_city_list
from weatherinfo import WeatherInfo
from responseconverter import parse_response

def main():
  print_title()
  key = "9bc5ebe3b7c229cf108539437bcac023"
  base_url = "http://api.openweathermap.org/data/2.5/weather?id="
  cities = load_cities()

  searchTerm = get_string_input("Enter a city ID or name (at least 4 characters or numbers): ")
  matching_cities = get_city_list(cities, searchTerm)
  if len(matching_cities) > 0:
    selected_city = select_city(matching_cities)
    url = base_url + selected_city.id + "&appid=" + key
    print(url)
    raw_data = get_raw_data(url)
    print(raw_data)
    weather_info = parse_response(raw_data)
    print_weather_info(weather_info)
  else:
    print("Sorry, no data for %s available!")

def print_title():
  print("Exercise 48: Weather service - Version 1\n")

def load_cities():
  print("Loading cities...")
  return read_json_file("city.list.json")

def print_weather_info(weather_info):
  print("Result:")
  print("City: %s" % (weather_info.name))
  print("Temp (Kelvin): %f" % weather_info.temp_kelvin)
  print("Temp (Celsius): %f" % weather_info.temp_celsius)
  print("Sunrise: %s" % weather_info.sunrise)
  print("Sunset: %s" % weather_info.sunset)

if __name__ == '__main__':
  main()
