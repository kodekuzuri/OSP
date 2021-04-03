import mongoengine as me
from osp.classes.address import Address

# USER CLASS


class User(me.Document):
    # currently using the generated object id of mongodb atlas as unique userid
    uniqueid = me.StringField()
    password = me.StringField(required=True, min_length=1)
    email = me.EmailField(required=True)
    name = me.StringField(required=True, min_length=1)
    number = me.StringField(required=True, regex='^[1-9]{1}[0-9]{9}$')

    is_authenticated = me.BooleanField(default=False)
    is_active = me.BooleanField(default=True)
    is_anonymous = me.BooleanField(default=False)

    meta = {'allow_inheritance': True}

    def get_id(self):
        """Return the uniqueid to satisfy Flask-Login's requirements."""
        return self.uniqueid


# MANAGER CLASS

class Manager(User):
    address = me.ReferenceField(Address, required=True,
                                reverse_delete_rule=me.NULLIFY)
    gender = me.StringField(required=True, min_length=1)
    dateOfBirth = me.DateField(required=True)

    def GetType(self):
        return 0


# CUTOMER CLASS

class Customer(User):
    city = me.StringField(required=True, min_length=1)

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

    def GetItems(self):
        from osp.classes.item import Item
        return Item.objects(seller=self)
    
    def GetType(self):
        return 2
