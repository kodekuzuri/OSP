from mongoengine import *
from .address import Address

# USER CLASS

class User(Document):
    userId = StringField(required=True, min_length=1, unique=True)
    password = StringField(required=True, min_length=1)
    name = StringField(required=True, min_length=1)
    email = EmailField(required=True) # move to inherited classes and ensure uniqueness?
    number = StringField(required=True, regex='^[0-9]{10}$')

    meta = {'allow_inheritance': True}


# MANAGER CLASS

class Manager(User):
    address = ReferenceField(Address, required=True, reverse_delete_rule=NULLIFY)
    gender = StringField(required=True, min_length=1)
    dateOfBirth = DateField(required=True)


# CUTOMER CLASS

class Customer(User):
    city = StringField(required=True, min_length=1)

    meta = {'allow_inheritance': True}


# BUYER CLASS

class Buyer(Customer):
    # buy_requests reference field (PULL type)
    pass


# SELLER CLASS

class Seller(Customer):
    # buy_requests reference field (PULL type)
    # items reference field (PULL type)
    pass
