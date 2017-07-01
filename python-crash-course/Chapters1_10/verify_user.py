import json

"""Driver program"""
def enter_username():
  username = get_username()

  if username:
    confirmation = input("Is " + username + " your username (yes/no)? ")
    if confirmation.lower() == 'yes':
      print("Welcome back, " + username + "!")
    else:
      save_username()
  else:
    save_username()

"""Retrieves username from file or returns None"""
def get_username():
  try:
    with open('username.txt') as f_obj:
      username = json.load(f_obj)
  except FileNotFoundError:
    return None
  else:
    return username

"""Gets username from user and saves in file"""
def save_username():
  username = input("Enter your username: ")
  with open('username.txt', 'w') as f_obj:
    json.dump(username, f_obj)
    print("Username saved: " + username + ".")

enter_username()
