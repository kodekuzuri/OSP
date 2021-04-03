import mongoengine as me
# from osp.classes import category
from osp.classes.user import Seller
from osp.classes.category import Category
import tempfile
import base64

# this can change depending if you send the JSON by url or not

# from PIL import Image


class Item(me.Document):
    # currently using the generated object id of mongodb atlas as unique itemid
    uniqueid = me.StringField()
    name = me.StringField(required=True, min_length=1)
    category = me.ReferenceField(Category, reverse_delete_rule=me.NULLIFY)
    seller = me.ReferenceField(
        Seller, required=True, reverse_delete_rule=me.CASCADE)
    price = me.FloatField(required=True, min_value=0)
    company = me.StringField(required=True)
    city = me.StringField(required=True, min_length=1)
    photo = me.ImageField(required=True)
    info = me.StringField(required=True, min_length=1)
    age = me.IntField(min_value=0)
    weight = me.FloatField(required=True, min_value=0)
    isheavy = me.BooleanField(required=True)


    def createItem(self,**kwargs):    
        _name = kwargs['name']
        _category = kwargs['category']
        _seller = kwargs['seller']
        _price = int(kwargs['price'])
        _company = kwargs['company']
        _city = kwargs['city']
        _photo = kwargs['photo']
        _info = kwargs['info']
        _age = int(kwargs['age'])
        _weight = int(kwargs['weight'])

        self.name = _name

        #category passed is a string
        if not Category.objects(name=_category).count():
            raise Exception("No such category")
        else:
            self.category = Category.objects(name=_category).first()
        
        # seller passed to constructor is string
        if not Seller.objects(name=_seller).count():
            raise Exception("No such seller")
        else:
            self.seller = Seller.objects(name=_seller).first()
        
        self.price = _price
        self.company = _company
        self.city = _city

        ## this will change  s#_photo is a path
        # with open(_photo,"rb") as fd:
        #     self.photo.put(fd,content_type='image/jpeg') 
        print("temp work started")
        file_like = base64.b64decode(_photo)
        bytes_image = bytearray(file_like)

        with tempfile.TemporaryFile() as f:
            f.write(bytes_image)
            f.flush()
            f.seek(0)
            self.photo.put(f)
        self.info = _info
        self.age = _age
        self.weight = _weight
        self.isheavy = True if _weight > 500 else False  # store 500 as a var
        # self.uploadToDB()
        print("temp work finished")


    def uploadToDB(self):
        try:
            self.save()
            self.uniqueid = str(self.id)
            self.save()
        except:
            raise
