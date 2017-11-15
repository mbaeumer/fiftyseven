from city import City

def get_string_input(question):
  result = ''
  while len(result) < 4:
    result = input(question)
  return result

def select_city(matching_cities):
  selected = False
  selected_city = None
  while not selected:
    try:
      print("Select a city:")
      index = 0
      for city in matching_cities:
        index = index + 1
        print("%d - %s, %s (%s)" % (index, city.name, city.country, city.id))
      user_input = int(input("Your choice: "))
      if user_input >= 1 and user_input <= len(matching_cities):
        selected = True
        selected_city = matching_cities[user_input - 1]
    except ValueError:
      print("ERROR: Wrong choice!")
  return selected_city
