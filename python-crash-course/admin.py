from classes import User
from privileges import Privileges

class Admin(User):
  def __init__(self, first_name, last_name, age, location, privileges):
    super().__init__(first_name, last_name, age, location)
    self.privileges = Privileges(privileges)
admin = Admin('Kevin', 'Jang', 23, 'Edison', ['can add post', 'can delete post', 'can update post'])
admin.privileges.show_privileges()
