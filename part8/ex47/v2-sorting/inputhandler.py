from sortingorder import SortingOrder

def get_sorting_order():
  selected = False
  sorting_order = ''
  while not selected:
    try:
      print("Select the sorting order:")
      print("1 - Ascending")
      print("2 - Descending")
      user_input = int(input("Your choice: "))
      if user_input == 1 or user_input == 2:
        selected = True
    except ValueError:
      print("ERROR: Wrong sorting order")
  sorting_order = SortingOrder(user_input)
  return sorting_order