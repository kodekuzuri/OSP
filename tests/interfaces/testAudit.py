import sys
sys.path.append(".")

from osp import Buyer, Item, Seller

print("Testing audit.")
print("creating dummy input for testing")
try:
    buyer_test1=Buyer(city="test one",password="abcd",email="testemail@email.com",name="test_buyer",number="9717911976")
    buyer_test1.save()
    buyer_test1.uniqueid=str(buyer_test.id)
    buyer_test1.save()

    buyer_test2=Buyer(city="test one",password="abcd",email="testemail@email.com",name="test_buyer",number="9717911976")
    buyer_test2.save()
    buyer_test2.uniqueid=str(buyer_test.id)
    buyer_test2.save()

    seller_test=Seller(city="test",password="abcd1",email="testemail1@email.com",name="test_seller",number="9717911976")
    seller_test.save()
    seller_test.uniqueid=str(seller_test.id)
    seller_test.save()

    import base64
    with open("./tests/classes/jester_pc.jpeg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    i1=Item()
    i1.createItem(name="test_buyrequest_item_heavy",category="test_cat_1",seller=seller_test.name,price=1000,company="test",city="test",photo=encoded_string,info="nice heavy laptop",age=2,weight=501)
    i1.uploadToDB()
    
    i2=Item()
    i2.createItem(name="test_buyrequest_item",category="test_cat_2",seller=seller_test.name,price=1000,company="test",city="test",photo=encoded_string,info="nice light laptop",age=2,weight=5)
    i2.uploadToDB()

    i3=Item()
    i3.createItem(name="test_buyrequest_item",category="test_cat_1",seller=seller_test.name,price=1000,company="test",city="test",photo=encoded_string,info="nice light laptop",age=2,weight=5)
    i3.uploadToDB()

    buyer_test1.GenerateBuyRequest(i1.uniqueid, 1000)
    buyer_test2.GenerateBuyRequest(i1.uniqueid, 1000)
    buyer_test1.GenerateBuyRequest(i3.uniqueid, 1000)

    print("dummy creation successfull")
except Exception as e:
    print("dummy content creation failed",e)


print("#### checking category deletions effect on items")
Category.RemoveCategory(Category.objects(name="test_cat_1").uniqueid)
print(i1.category)
print(i3.category)


print("deleting dummies")
try:
    buyer_test.delete()
    seller_test.delete()
    i1.delete()
    i2.delete()
    print("success")
except:
    print("failed")