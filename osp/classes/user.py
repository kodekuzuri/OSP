from mongoengine import *
from osp.classes.address import Address

# USER CLASS

class User(Document):
    # currently using the generated object id of mongodb atlas as unique userid
    uniqueid = StringField()
    password = StringField(required=True, min_length=1)
    email = EmailField(required=True)
    name = StringField(required=True, min_length=1)
    number = StringField(required=True, regex='^[0-9]{10}$')

    is_authenticated = BooleanField(default=False)
    is_active = BooleanField(default=True)
    is_anonymous = BooleanField(default=False)

    meta = {'allow_inheritance': True}

    def get_id(self):
        """Return the uniqueid to satisfy Flask-Login's requirements."""
        return self.uniqueid

    # def is_authenticated(self):
    #     """Return True if the user is authenticated."""
    #     return self.authenticated


# MANAGER CLASS

class Manager(User):
    address = ReferenceField(Address, required=True, reverse_delete_rule=NULLIFY)
    gender = StringField(required=True, min_length=1)
    dateOfBirth = DateField(required=True)

    def GetType(self):
        return 0


# CUTOMER CLASS

class Customer(User):
    city = StringField(required=True, min_length=1)

    meta = {'allow_inheritance': True}


# BUYER CLASS

class Buyer(Customer):
    # buy_requests reference field (PULL type)
    
    def GetType(self):
        return 1


# SELLER CLASS

class Seller(Customer):
    # buy_requests reference field (PULL type)
    # items reference field (PULL type)
    
    def GetType(self):
        return 2
