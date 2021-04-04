import mongoengine as me
from osp.classes.item import Item, SoldItem
from osp.classes.user import Buyer,Seller

BUY_REQUEST_STATUS = ((0, 'Rejected'), (1, 'Pending'), (2, 'Approved'))

#       approveRequest: change to appove and email payment details
#   rejectRequest: change status to rejeted
#     approvePaymentStatus: shift item to SoldItem, delete item
#   changeofferprice:


class BuyRequest(me.Document):
    uniqueid = me.StringField()
    item = me.ReferenceField(
        Item, required=True, reverse_delete_rule=me.CASCADE)
    buyer = me.ReferenceField(Buyer, required=True,
                              reverse_delete_rule=me.CASCADE)
    seller = me.ReferenceField(Seller, required=True,
                              reverse_delete_rule=me.CASCADE)                              
    offer = me.FloatField(required=True, min_value=0)
    status = me.IntField(default=1, choices=BUY_REQUEST_STATUS)
    paymentstatus = me.BooleanField(default=False)

    def CreateBuyRequest(self, **kwargs):
        """kwargs gets reffield  make sure while calling the function"""
        try:
            self.item = kwargs['item']
            self.buyer = kwargs['buyer']
            self.seller = self.item.seller
            self.offer = float(kwargs['offer'])
            self.save()
            self.uniqueid = str(self.id)
            self.save()
        except:
            raise

    def ChangeOfferPrice(self, new_price):
        try:
            if(self.status==1):
                self.offer = new_price
                self.save()
            else: 
                raise Exception("Can't change offer price of buy request which has already been approved or rejected.")
        except:
            raise

    def ApproveRequest(self):
        try:
            if(self.status==1):
                self.status = 2
                self.save()
            elif self.status == 2: 
                raise Exception("Request already approved.")
            else:
                raise Exception("Request already rejected, can't approve it.")
        except:
            raise

    def ApprovePayment(self):
        try:
            if(self.status==2):
                self.paymentstatus=1
                self.save()
                scopy= SoldItem()
                data_dict={
                    "name":self.item.name,
                    "category":self.item.category.name,
                    "buyer":self.buyer.uniqueid,
                    "seller":self.seller.uniqueid,
                    "price":self.offer,
                    "photo":self.item.photo
                }
                scopy.CreateAndUploadSoldItem(**data_dict)
                self.item.delete()
            else: 
                raise Exception("Can't approve payment for a request which is pending or rejected.")
        except:
            raise
    
    def RejectRequest(self):
        try:
            if(self.status==1):
                self.status=0
                self.save()
            elif self.status == 0: 
                raise Exception("Request already rejected.")
            else:
                raise Exception("Request already approved, can't reject it.")
        except:
            raise