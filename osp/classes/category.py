from mongoengine import *

class Category(Document):
    # currently using the generated object id of mongodb atlas as unique categoryid
    uniqueid = StringField()
    name = StringField(required=True, min_length=1)
