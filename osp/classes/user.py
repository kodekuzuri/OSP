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
            item = Item.objects(uniqueid=itemid).first()
            # if item is heavy then it must be in the same city as the buyer
            if item.isheavy and (str(item.city).casefold() != str(self.city).casefold()):
                raise Exception("Cannot buy heavy item outside your city.")
            if item:
                buyreq = BuyRequest()
                buyreq.CreateBuyRequest(item=item, buyer=self, offer=offer)
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
        
    def Negotiate(self, buyreqid):
        """Sends mail to relevant parties asking for negotiation"""
        from osp.classes.buyrequest import BuyRequest
        from osp.interfaces.signup import SendMail
        try:
            buyreq = BuyRequest.objects(uniqueid=buyreqid).first()
            if buyreq:
                buyer_mail = self.email
                seller_mail = buyreq.seller.email
                manager_mail = Manager.objects().first().email
                text = f'''Hello,
                
                Negotiation requested for buy request {buyreqid} of item {buyreq.item.name} by {self.name}.

                Regards,
                Team OSP
                '''
                subject = 'Negotiation request'
                SendMail(text, subject, buyer_mail)
                SendMail(text, subject, seller_mail)
                SendMail(text, subject, manager_mail)
                return (True, "Negotiation request placed successfully.")
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
    
    def ApproveRequest(self, buyreqid):
        """Approve existing buy request"""
        from osp.classes.buyrequest import BuyRequest
        from osp.interfaces.signup import SendMail
        try:
            buyreq = BuyRequest.objects(uniqueid=buyreqid).first()
            if buyreq:
                buyer_mail = buyreq.buyer.email
                seller_mail = buyreq.seller.email
                manager_mail = Manager.objects().first().email
                buyreq.ApproveRequest()
                text = f'''Hello,
                
                Buy request {buyreqid} of item {buyreq.item.name} by {buyreq.buyer.name} has been approved by {buyreq.seller.name}.
                Here is the payment link <insert_payment_link>.

                Regards,
                Team OSP
                '''
                subject = 'Buy request approved'
                SendMail(text, subject, buyer_mail)
                SendMail(text, subject, seller_mail)
                SendMail(text, subject, manager_mail)
                return (True, "Approved request. Payment details sent to the buyer.")
            else:
                raise Exception("Buy request doesn't exist in database.")
        except Exception as e:
            return (False, str(e))
    
    def RejectRequest(self, buyreqid):
        """Reject existing buy request"""
        from osp.classes.buyrequest import BuyRequest
        try:
            buyreq = BuyRequest.objects(uniqueid=buyreqid).first()
            if buyreq:
                buyreq.RejectRequest()
                return (True, "Rejected request.")
            else:
                raise Exception("Buy request doesn't exist in database.")
        except Exception as e:
            return (False, str(e))
    
    def ApprovePayment(self, buyreqid):
        """Approve payment of existing buy request"""
        from osp.classes.buyrequest import BuyRequest
        from osp.interfaces.signup import SendMail
        try:
            buyreq = BuyRequest.objects(uniqueid=buyreqid).first()
            if buyreq:
                buyer_mail = buyreq.buyer.email
                seller_mail = buyreq.seller.email
                manager_mail = Manager.objects().first().email
                buyreq.ApprovePayment()
                text = f'''Hello,
                
                Payment for buy request {buyreqid} of item {buyreq.item.name} by {buyreq.buyer.name} has been approved by {buyreq.seller.name}.
                Item has been removed from the database.

                Regards,
                Team OSP
                '''
                subject = 'Payment approved'
                SendMail(text, subject, buyer_mail)
                SendMail(text, subject, seller_mail)
                SendMail(text, subject, manager_mail)
                return (True, "Payment approved.")
            else:
                raise Exception("Buy request doesn't exist in database.")
        except Exception as e:
            return (False, str(e))
