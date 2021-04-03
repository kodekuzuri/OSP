from mongoengine import me
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
            self.seler=kwargs['seller']
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
                raise Exception("Buy Request status wrong")
        except:
            raise

    def ApproveRequest(self):
        try:
            self.status = 2
            self.save()
            scopy= SoldItem()
            data_dict={
                "name":self.item.name,
                "category":self.item.category.name,
                "buyer":self.buyer.name,
                "seller":self.seller.name,
                "price":self.offer,
                "photo":self.item.photo
            }
            scopy.CreateAndUploadSoldItem(**data_dict)
            self.item.delete()
        except:
            raise

    def ApprovePayment(self):
        try:
            self.paymentstatus=1
            self.save()

        except:
            raise
    
    def RejectRequest(self):
        try:
            self.status=0
            self.save()
        except:
            raise