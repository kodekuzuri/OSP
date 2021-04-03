import mongoengine as me
class Category(me.Document):
    # currently using the generated object id of mongodb atlas as unique categoryid
    uniqueid = me.StringField()
    name = me.StringField(required=True, min_length=1, unique=True)

    @staticmethod
    def AddCategory(name):
        try:
            if Category.objects(name=name).count():
                raise Exception("Category already exists.")
            cat = Category(name=name)
            cat.save()
            cat.uniqueid=str(cat.id)
            cat.save()
            return (True, "Category successfully added.")
        except Exception as e:
            return (False, str(e))
    
    @staticmethod
    def RemoveCategory(uniqueid):
        try:
            if not Category.objects(uniqueid=uniqueid).count():
                raise Exception("Category with given id doesn't exist hence not removed.")
            cat = Category.objects(uniqueid=uniqueid).first()
            cat.delete()
            return (True, "Category successfully removed.")
        except Exception as e:
            return (False, str(e))



