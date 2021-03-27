from mongoengine import *
from osp.classes.user import Seller
from osp.classes.category import Category

class Item(Document):
    # currently using the generated object id of mongodb atlas as unique itemid
    uniqueid = StringField()
    name = StringField(required=True, min_length=1)
    category = ReferenceField(Category, reverse_delete_rule=NULLIFY)
    seller = ReferenceField(Seller, required=True, reverse_delete_rule=CASCADE)
    price = FloatField(required=True, min_value=0)
    company = StringField(required=True)
    city = StringField(required=True, min_length=1)
    photo = ImageField(required=True)
    info = StringField(required=True, min_length=1)
    age = IntField(min_value=0)
    isheavy = BooleanField(required=True)
