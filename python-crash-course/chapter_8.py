def display_message():
  print('I am learning about defining functions in Python!')
display_message()

def favorite_book(title):
  print('One of my favorite books is ' + title.title() + '.')
favorite_book('the hobbit')

def make_shirt(size='large', message='I love Python'):
  print('You ordered a t-shirt size of ' + size + ' with a message of ' + message + '!')
make_shirt('small', 'Hello World')
make_shirt(message='Hello World', size='small')
make_shirt()
make_shirt('medium')
make_shirt(message='Hey there')

def city_country(city, country):
  return city.title() + ', ' + country.title()
print(city_country('santiago', 'chile'))
print(city_country('new jersey', 'united states'))
print(city_country('london', 'england'))

magicians = ['houdini', 'idk', 'bob']
def show_magicians(magicians):
  for magician in magicians:
    print(magician.title())
show_magicians(magicians)

def make_great(magicians):
  for i in range(len(magicians)):
    magicians[i] = 'Great ' + magicians[i]
  return magicians
great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)

def order_sandwich(*ingredients):
  order = "Making a sandwich with the following toppings: " + ", ".join(ingredients)
  return order
print(order_sandwich('ham'))
print(order_sandwich('ham', 'turkey', 'bacon', 'lettuce'))
print(order_sandwich('peanut butter', 'jelly'))

def build_profile(first, last, **user_info):
  """Build a dictionary containing everything we know about a user."""
  profile = {}
  profile['first_name'] = first
  profile['last_name'] = last
  for key, value in user_info.items():
    profile[key] = value
  return profile
print(build_profile('Kevin', 'Jang', age=23, hometown='Edison', hobby='piano'))

def make_car(manufacturer, model, **optional_features):
  car = {
    'manufacturer': manufacturer,
    'model': model
  }
  for key, value in optional_features.items():
    car[key] = value
  return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)


