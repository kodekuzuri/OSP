import mongoengine as me
from osp.classes.item import Item
from osp.classes.user import Buyer, Seller

BUY_REQUEST_STATUS = ((0, 'Rejected'), (1, 'Pending'), (2, 'Approved'))

class BuyRequest(Document):
    item = me.ReferenceField(Item, required=True, reverse_delete_rule=me.CASCADE)
    buyer = me.ReferenceField(Buyer, required=True, reverse_delete_rule=me.CASCADE)
    seller = me.ReferenceField(Seller, required=True, reverse_delete_rule=me.CASCADE)
    offer = me.FloatField(required=True, min_value=0)
    status = me.IntField(default=1, choices=BUY_REQUEST_STATUS)
    paymentstatus = me.BooleanField(default=False)
