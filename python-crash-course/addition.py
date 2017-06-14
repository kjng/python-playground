"""Program to add numbers. Handles inputs that are text instead of numbers."""
successful = False

while successful != True:
  num_one = input("Enter a number: ")
  num_two = input("Enter another number: ")
  try:
    num_one = int(num_one)
    num_two = int(num_two)
  except ValueError:
    print("Both of your numbers really need to be numbers!")
  else:
    print(str(num_one) + " + " + str(num_two) + " = " + str(num_one + num_two))
    successful = True
