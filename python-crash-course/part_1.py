# Part 1 Exercises from Python Crash Course

# Simple Message
message = 'Hello World!'
print(message)

# Simple Messages
another_message = 'Foo!'
print(another_message)
another_message = 'Bar.'
print(another_message)

# Personal Message
name = 'Kevin Jang'
print('Hello ' + name + ', would you like to learn some Python today?')

# Name Cases
print(name.lower())
print(name.upper())
print(name.title())

# Famous Quote
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

# Famous Quote 2
famous_person = 'Albert Einstein'
message = famous_person + ' once said, "A person who never made a mistake never tried anything new."'
print(message)

# Stripping Names
whitespace_name = ' \t Kevin Jang  \n'
print(whitespace_name)
print(whitespace_name.lstrip())
print(whitespace_name.rstrip())
print(whitespace_name.strip())

# Number Eight
print(5 + 3)
print(11 - 3)
print(2 * 4)
print (16 / 2)

# Favorite Number
fav_number = 7
message = 'My favorite number is ' + str(fav_number) + '! What\'s yours?'
print(message)

# Names
names = ['Peter', 'Yue', 'Brian']
print(names[0])
print(names[1])
print(names[2])

# Greetings
message = 'Good evening, '
print(message + names[0])
print(message + names[1])
print(message + names[2])

# Your Own List
cars = ['Tesla Model S', 'Honda S2000', 'BMW M2', 'Porsche 911', 'Porsche Boxster']
message = 'I would like to own a '
print(message + cars[0] + ' car.')
print(message + cars[1] + ' car.')
print(message + cars[2] + ' car.')
print(message + cars[3] + ' car.')
print(message + cars[4] + ' car.')

# Guest List
guest_list = ['Taylor Swift', 'Yo Yo Ma', 'Bruce Brubaker']
message = 'Would you like to have dinner with me, '
print(message + guest_list[0] + '?')
print(message + guest_list[1] + '?')
print(message + guest_list[2] + '?')

# Changing Guest List
print('Oh no! ' + guest_list[1] + ' can\'t make it...')
guest_list[1] = 'Barack Obama'
message = 'Great! See you at dinner, '
print(message + guest_list[0] + '.')
print(message + guest_list[1] + '.')
print(message + guest_list[2] + '.')

# More Guests
print('Hey everyone! I found a bigger dinner table!')
guest_list.insert(0, 'Peter Cai')
guest_list.insert(2, 'Yue Qian')
guest_list.append('Brian Hong')
print(message + guest_list[0] + '.')
print(message + guest_list[1] + '.')
print(message + guest_list[2] + '.')
print(message + guest_list[3] + '.')
print(message + guest_list[4] + '.')
print(message + guest_list[5] + '.')

# Shrinking Guest List
print('Oh no! I can only invite two people for dinner...')
print('Sorry, ' + guest_list.pop(0) + '. I can\'t have you over for dinner.')
print('Sorry, ' + guest_list.pop() + '. I can\'t have you over for dinner.')
print('Sorry, ' + guest_list.pop() + '. I can\'t have you over for dinner.')
print('Sorry, ' + guest_list.pop() + '. I can\'t have you over for dinner.')
print('Hey, ' + guest_list[0] + ', you\'re still invited!')
print('Hey, ' + guest_list[1] + ', you\'re still invited!')
del guest_list[1]
del guest_list[0]
print(guest_list)
