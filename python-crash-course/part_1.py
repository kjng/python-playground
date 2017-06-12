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
print('Albert Einstein once said, "A person who never made a mistake never \
    tried anything new."')

# Famous Quote 2
famous_person = 'Albert Einstein'
message = famous_person + ' once said, "A person who never made a mistake never\
 tried anything new."'
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
cars = ['Tesla Model S', 'Honda S2000', 'BMW M2', 'Porsche 911',
    'Porsche Boxster']
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

# Seeing the World
locations = ['Japan', 'South Korea', 'Australia', 'Iceland', 'England']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

# Dinner Guests
print('I\'m inviting ' + str(len(guest_list)) + ' guests to dinner!')

# Every Function
languages = ['english', 'chinese', 'japanese', 'korean', 'spanish', 'german']
print(languages)
print(sorted(languages))
print(sorted(languages, reverse=True))
languages.reverse()
print(languages)
languages.reverse()
print(languages)
languages.sort(reverse=True)
print(languages)
languages.sort()
print(languages)

# Pizzas
pizzas = ['Mushroom', 'Hawaiian', 'Pepperoni']
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
print("I really love pizza!")

# Animals
animals = ['dog', 'cat', 'turtle']
for animal in animals:
    print("A " + animal + " would make a great pet.")
print("Any of these animals would make a great pet!")

# Counting to Twenty
for value in range(1, 21):
    print(value)

# One Million
million_nums = list(range(1, 1000001))
# for num in million_nums:
#   print(num)

# Summing a Million
print(min(million_nums))
print(max(million_nums))
print(sum(million_nums))

# Odd Numbers
odd_nums = list(range(1, 20, 2))
for num in odd_nums:
    print(num)

# Threes
threes = list(range(3, 31, 3))
for num in threes:
    print(num)

# Cubes
cubes = []
for val in range(1, 11):
    print(val**3)
    cubes.append(val**3)

# Cube Comprehension
cubes = [value**3 for value in range(1, 11)]
for val in cubes:
    print(val)

# Slices
print("The first tree items in the list are: " + str(cubes[:3]))
print("Three items from the middle of the list are: " + str(cubes[3:6]))
print("The last three items in the list are: " + str(cubes[-3:]))

# My Pizzas, Your Pizzas
friend_pizzas = pizzas[:]
pizzas.append('Sausage')
friend_pizzas.append('Three Cheese')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# More Loops
foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
friends_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']
for food in foods:
    print(food)
for food in friends_foods:
    print(food)

# Buffet
simple_foods = ('mac and cheese', 'pizza', 'prime rib', 'cocktail shrimp',
    'chicken nuggets')
for food in simple_foods:
    print(food)
simple_foods = ('mac and cheese', 'pizza', 'sushi', 'cocktail shrimp', 'salmon')
for food in simple_foods:
    print(food)
