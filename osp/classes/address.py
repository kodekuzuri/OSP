from mongoengine import *

# ADDRESS CLASS

class Address(Document):
    houseNumber = StringField(required=True, min_length=1, regex="^[a-zA-Z0-9-\/, ]*$")
    street = StringField(required=True, regex="^[a-zA-Z0-9-\/, ]*$")
    locality = StringField(required=True, min_length=1, regex="^[a-zA-Z0-9-\/, ]*$")
    city = StringField(required=True, min_length=1, regex="^[a-zA-Z ]*$")
    state = StringField(required=True, min_length=1, regex="^[a-zA-Z ]*$")
    pincode = StringField(required=True, min_length=1, regex="^[1-9]{1}[0-9]{2}\s{0,1}[0-9]{3}$")
