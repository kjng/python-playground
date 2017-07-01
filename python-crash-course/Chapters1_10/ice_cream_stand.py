from classes import Restaurant

class IceCreamStand(Restaurant):
  def __init__(self, stand_name, flavors):
    super().__init__(stand_name, 'ice cream')
    self.flavors = flavors
  def get_flavors(self):
    print(self.restaurant_name + ' serves flavors: ' + ", ".join(self.flavors))
ice_cream_stand = IceCreamStand("Kevin's", ['vanilla', 'strawberry', 'chocolate'])
ice_cream_stand.get_flavors()
