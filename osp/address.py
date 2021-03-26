from mongoengine import *

# ADDRESS CLASS

class Address(Document):
    houseNumber = StringField(required=True, min_length=1)
    street = StringField()
    locality = StringField(required=True, min_length=1)
    city = StringField(required=True, min_length=1)
    state = StringField(required=True, min_length=1)
    pincode = StringField(required=True, regex="^[1-9]{1}[0-9]{2}\\s{0, 1}[0-9]{3}$")
