import sys
sys.path.append(".")
from osp import Seller, Item

s1=Seller.objects().first()
print("testing class Item")
try:
    if(Item.objects(name="test_item").count()):
        [x.delete() for x in Item.objects(name="test_item")]
    print("old test items succesfully removed from the databse")
except:
    print("old test items couldnt be deleted, please contact the admin :(")

try:
    i1=Item()
    ### convert photo to base64 string 
    import base64
    with open("./tests/classes/jester_pc.jpeg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    i1.createItem(name="test_item",category="electronics",seller=s1.name,price=1000,company="test",city="test",photo=encoded_string,info="nice laptop",age=2,weight=5)
    print("construction with correct parameters was a success")
    i1.uploadToDB()
    print("Upload to database with correct parameters was a success")
except Exception as e:
    print("Upload to database with correct parameters failed",e)

try:
    i2=Item()
    i2.createItem(name="",category="",seller=s1.name,price=-1,company="test",city="test",photo="",info="nice laptop",age=2,weight=5)
    print("FAILED -> constructed with illegal params")
    i2.uploadToDB()
    print("FAILED -> uploaded with illegal params")
except:
    print("Upload to database with incorrect parameters was rejected")

try:
    Item.objects(name="test_item").first().delete()
    print("item successfully deleted")
except:
    print("item couldnt be deleted")
