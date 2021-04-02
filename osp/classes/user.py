import mongoengine as me
from osp.classes.address import Address

# USER CLASS


class User(me.Document):
    # currently using the generated object id of mongodb atlas as unique userid
    uniqueid = me.StringField()
    password = me.StringField(required=True, min_length=1)
    email = me.EmailField(required=True)
    name = me.StringField(required=True, min_length=1)
    number = me.StringField(required=True, regex='^[0-9]{10}$')

    meta = {'allow_inheritance': True}


# MANAGER CLASS

class Manager(User):
    address = me.ReferenceField(Address, required=True,
                                reverse_delete_rule=me.NULLIFY)
    gender = me.StringField(required=True, min_length=1)
    dateOfBirth = me.DateField(required=True)


# CUTOMER CLASS

class Customer(User):
    city = me.StringField(required=True, min_length=1)

    meta = {'allow_inheritance': True}


# BUYER CLASS

class Buyer(Customer):
    # buy_requests reference field (PULL type)
    pass


# SELLER CLASS

class Seller(Customer):
    # buy_requests reference field (PULL type)
    # items reference field (PULL type)
    # name = me.StringField(required=True, min_length=1)
    pass
