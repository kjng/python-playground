import json

def favorite_number():
  favorite_number = get_favorite_number()

  if favorite_number:
    print("Your favorite number is " + favorite_number + "!")
  else:
    favorite_number = input("What is your favorite number? ")
    with open('favorite_number.txt', 'w') as f_obj:
      json.dump(favorite_number, f_obj);
      print("We'll remember your favorite number for when you come back!")

def get_favorite_number():
  try:
    with open('favorite_number.txt') as f_obj:
      favorite_number = json.load(f_obj)
  except FileNotFoundError:
    return None
  else:
    return favorite_number

favorite_number()
