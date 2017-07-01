with open('guest.txt', 'w') as file_object:
  guest = input("What is your name? ")
  file_object.write(guest.title() + "\n")
