import unittest
from city_functions import format_city_country

class CityCountryTestCase(unittest.TestCase):

  def test_city_country(self):
    city_country = format_city_country('santiago', 'chile')
    self.assertEqual(city_country, 'Santiago, Chile')

unittest.main()
