import unittest
from employee import Employee

class EmployeeTests(unittest.TestCase):
  def setUp(self):
    self.test_employee = Employee('Kevin', 'Jang', 0)

  def test_give_default_raise(self):
    self.test_employee.give_raise()
    self.assertEqual(self.test_employee.salary, 5000)

  def test_give_custom_raise(self):
    self.test_employee.give_raise(1234)
    self.assertEqual(self.test_employee.salary, 1234)

unittest.main()
