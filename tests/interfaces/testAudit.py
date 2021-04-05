import sys
sys.path.append(".")

from osp import Buyer, Item, Seller, Category, BuyRequest

Category.AddCategory("test_cat_1")
Category.AddCategory("test_cat_2")

for req in BuyRequest.objects():
    req.delete()

print("Testing audit.")
print("creating dummy input for testing")
try:
    buyer_test1=Buyer(city="test one",password="abcd",email="testemail@email.com",name="test_buyer1",number="9717911976")
    buyer_test1.save()
    buyer_test1.uniqueid=str(buyer_test1.id)
    buyer_test1.save()

    buyer_test2=Buyer(city="test one",password="abcd",email="testemail@email.com",name="test_buyer2",number="9717911976")
    buyer_test2.save()
    buyer_test2.uniqueid=str(buyer_test2.id)
    buyer_test2.save()

    seller_test=Seller(city="test",password="abcd1",email="testemail1@email.com",name="test_seller",number="9717911976")
    seller_test.save()
    seller_test.uniqueid=str(seller_test.id)
    seller_test.save()

    import base64
    with open("./tests/classes/jester_pc.jpeg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    i1=Item()
    i1.createItem(name="test_buyrequest_item_heavy",category="test_cat_1",seller=seller_test.name,price=1000,company="test",city="test",photo=encoded_string,info="nice heavy laptop",age=2,weight=5)
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
# Category.RemoveCategory(Category.objects(name="test_cat_1").first().uniqueid)
print(i1.category)
print(i3.category)

print("#### print existing buyreqs")
for req in BuyRequest.objects():
    print(req.item.name, req.buyer.name)

print("#### checking buy requests after item deletion")
i1.delete()
for req in BuyRequest.objects():
    print(req.item.name, req.buyer.name)


print("deleting dummies")
try:
    buyer_test1.delete()
    buyer_test2.delete()
    seller_test.delete()
    i2.delete()
    i3.delete()
    Category.RemoveCategory(Category.objects(name="test_cat_2").first().uniqueid)
    print("success")
except:
    print("failed")