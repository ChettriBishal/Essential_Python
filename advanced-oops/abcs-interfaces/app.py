from database import Database
from admin import Admin
from user import User

a = Admin('paco', 'perez', 2)
b = Admin('rolf', 'smith', 1)
c = User('snowden','pp123123')

users = [a,b,c]

for user in users:
    user.save()

