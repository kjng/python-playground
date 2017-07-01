# age = 0
# while age != 'quit':
#   age = input('Enter your age: ')
#   if age != 'quit':
#     age = int(age)
#     if age < 3:
#       print('Your ticket is free!')
#     elif age >= 3 and age <= 12:
#       print('Your ticket is $10.')
#     elif age > 12:
#       print('Your ticket will be $15.')

active = True
while active:
  age = input('Enter your age: ')
  if age == 'quit':
    active = False
  else:
    age = int(age)
    if age < 3:
      print('Your ticket is free!')
    elif age >= 3 and age <= 12:
      print('Your ticket is $10.')
    elif age > 12:
      print('Your ticket will be $15.')

# while True:
#   age = input('Enter your age: ')
#   if age == 'quit':
#     break
#   age = int(age)
#   if age < 3:
#     print('Your ticket is free!')
#   elif age >= 3 and age <= 12:
#     print('Your ticket is $10.')
#   elif age > 12:
#     print('Your ticket will be $15.')
