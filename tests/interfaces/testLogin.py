import sys
sys.path.append(".")

import datetime
from osp import Login, Buyer, Manager, Seller, Address

# testing for manager
a = Manager()
a.uniqueid = "admin"
a.password = "admin"
a.name = "sysadmin"
a.email = "admin@osp.com"
a.number = "1234567890"
a.address = Address(houseNumber="1/OSP", street="OSP", locality="OSP", city="OSP", state="OSP", pincode="123 456").save()
a.gender = "Male"
a.dateOfBirth = datetime.date(2021,1,1)
a.save()

print(Login("admin", "admin", 0)) # correct credentials
print(Login("admin1", "admin", 0)) # incorrect userId
print(Login("admin", "admin1", 0)) # incorrect password
print(Login("admin1", "admin1", 0)) # both incorrect
print(Login("admin", "admin", 1)) # incorrect user type

a.address.delete()
a.delete()

# testing for buyer
b = Buyer()
b.uniqueid = "buyer"
b.password = "buyer"
b.name = "sysadmin"
b.email = "admin@osp.com"
b.number = "1234567890"
b.city = "OSP"
b.save()

print(Login("buyer", "buyer", 1)) # correct credentials
print(Login("buyer1", "buyer", 1)) # incorrect userId
print(Login("buyer", "buyer1", 1)) # incorrect password
print(Login("buyer1", "buyer1", 1)) # both incorrect
print(Login("buyer", "buyer", 2)) # incorrect user type

b.delete()

# testing for seller
c = Seller()
c.uniqueid = "seller"
c.password = "seller"
c.name = "sysadmin"
c.email = "admin@osp.com"
c.number = "1234567890"
c.city = "OSP"
c.save()

print(Login("seller", "seller", 2)) # correct credentials
print(Login("seller1", "seller", 2)) # incorrect userId
print(Login("seller", "seller1", 2)) # incorrect password
print(Login("seller1", "seller1", 2)) # both incorrect
print(Login("seller", "seller", 0)) # incorrect user type

c.delete()

print(Login("605e5c73340b2c7e854e33d8", "Byfs1BO8", 0))
