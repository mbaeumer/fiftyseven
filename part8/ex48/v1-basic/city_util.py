from city import City

def get_city_list(all_cities, searchTerm):
  matching_cities = []
  for city in all_cities:
    if searchTerm in city.id or searchTerm.title() in city.name:
      matching_cities.append(city)
  return matching_cities