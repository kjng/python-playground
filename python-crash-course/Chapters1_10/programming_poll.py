with open('poll_results.txt', 'a') as file_object:
  print("(type 'quit' at any time to exit)")
  while True:
    name = input("What is your name? ")
    if name == 'quit':
      break

    response = input("Why do you like programming? ")
    if response == 'quit':
      break

    file_object.write('Response from ' + name.title() + ': ' + response + '\n')
