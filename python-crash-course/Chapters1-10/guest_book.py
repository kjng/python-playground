with open('guest_book.txt', 'a') as file_object:
  print("(type 'quit' at any time to exit)")
  while True:
    guest = input("Enter your name: ")
    if guest == "quit":
      break
    file_object.write(guest.title() + "\n")
