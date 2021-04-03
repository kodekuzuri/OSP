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
    def GetBuyRequests(self):
        """Get all buy requests of the buyer"""
        from osp.classes.buyrequest import BuyRequest
        return BuyRequest.objects(buyer=self)
    
    def GetType(self):
        return 1

    def GenerateBuyRequest(self, itemid, offer):
        """Generate a new buy request from the buyer"""
        from osp.classes.buyrequest import BuyRequest
        from osp.classes.item import Item
        try:
            # if item is heavy then it must be in the same city as the buyer
            if item.isheavy and (item.city != self.city):
                raise Exception("Cannot buy heavy item outside your city.")
            item = Item.objects(uniqueid=itemid).first()
            if item:
                buyreq = BuyRequest()
                buyreq.CreateBuyRequest(item=item, buyer=self, seller=item.seller, offer=offer)
                return (True, "Buy request placed successfully.")
            else:
                raise Exception("Item doesn't exist in database.")    
        except Exception as e:
            return (False, str(e))
    
    def ChangeOfferPrice(self, buyreqid, newprice):
        """Change offer price of existing buy request"""
        from osp.classes.buyrequest import BuyRequest
        try:
            buyreq = BuyRequest.objects(uniqueid=buyreqid).first()
            if buyreq:
                buyreq.ChangeOfferPrice(newprice)
                return (True, "Offer price changed successfully.")
            else:
                raise Exception("Buy request doesn't exist in database.")
        except Exception as e:
            return (False, str(e))


# SELLER CLASS

class Seller(Customer):
    def GetBuyRequests(self):
        from osp.classes.buyrequest import BuyRequest
        return BuyRequest.objects(seller=self)

    def GetItems(self):
        from osp.classes.item import Item
        return Item.objects(seller=self)
    
    def GetType(self):
        return 2
