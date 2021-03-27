from mongoengine import *
from osp.classes.item import Item
from osp.classes.user import Buyer

BUY_REQUEST_STATUS = ((0, 'Rejected'), (1, 'Pending'), (2, 'Approved'))

class BuyRequest(Document):
    item = ReferenceField(Item, required=True, reverse_delete_rule=CASCADE)
    buyer = ReferenceField(Buyer, required=True, reverse_delete_rule=CASCADE)
    offer = FloatField(required=True, min_value=0)
    status = IntField(default=1, choices=BUY_REQUEST_STATUS)
    paymentstatus = BooleanField(default=False)
