import mongoengine as me
class Category(me.Document):
    # currently using the generated object id of mongodb atlas as unique categoryid
    uniqueid = me.StringField()
    name = me.StringField(required=True, min_length=1,unique=True)

