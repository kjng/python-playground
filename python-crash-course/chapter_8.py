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
