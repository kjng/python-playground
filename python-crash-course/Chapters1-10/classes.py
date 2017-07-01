class Restaurant():
  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0
  def describe_restaurant(self):
    print('The restaurant is called ' + self.restaurant_name.title() + ' and serves ' + self.cuisine_type.title() + ' food.')
  def open_restaurant(self):
    print(self.restaurant_name.title() + ' is open!')
  def set_number_served(self, number):
    self.number_served = number
  def increment_number_served(self, increment):
    self.number_served += increment

restaurant = Restaurant('taco bell', 'fake mexican')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.number_served)
restaurant.set_number_served(17)
print(restaurant.number_served)
restaurant.increment_number_served(4)
print(restaurant.number_served)
Restaurant('burger king', 'american').describe_restaurant()
Restaurant('tasty moment', 'taiwanese').describe_restaurant()

class User():
  def __init__(self, first_name, last_name, age, location):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.location = location
    self.login_attempts = 0
  def describe_user(self):
    print(self.first_name)
    print(self.last_name)
    print(self.age)
    print(self.location)
  def greet_user(self):
    print('Hello, ' + self.first_name.title() + ' ' + self.last_name.title() + '!')
  def increment_login_attempts(self):
    self.login_attempts += 1
  def reset_login_attempts(self):
    self.login_attempts = 0

kevin = User('kevin', 'jang', 23, 'edison')
bob = User('bob', 'dodo', 42, 'nyc')
tobias = User('tobias', 'fate', 13, 'twitch')
kevin.describe_user()
kevin.greet_user()
bob.describe_user()
bob.greet_user()
tobias.describe_user()
tobias.greet_user()
kevin.increment_login_attempts()
kevin.increment_login_attempts()
kevin.increment_login_attempts()
print(kevin.login_attempts)
kevin.reset_login_attempts()
print(kevin.login_attempts)
