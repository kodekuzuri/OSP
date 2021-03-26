from mongoengine import *

# connect to database
connect(host='mongodb+srv://ospapp:tyaLmQbvP6rJU4uY@smmh.yappb.mongodb.net/ospDatabase?retryWrites=true&w=majority')

# make all relevant classes available directly
# from .testclass import TestClass, TestClass2, TestClass3

from .user import Manager, Buyer, Seller
from .address import Address
