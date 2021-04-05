import sys
sys.path.append(".")

from osp import Buyer, Item, Seller

print("Testing BuyRequest and associated functions from class Buyer and Seller")
print("creating dummy input for testing")
try:
    buyer_test=Buyer(city="test one",password="abcd",email="testemail@email.com",name="test_buyer",number="9717911976")
    buyer_test.save()
    buyer_test.uniqueid=str(buyer_test.id)
    buyer_test.save()

    seller_test=Seller(city="test",password="abcd1",email="testemail1@email.com",name="test_seller",number="9717911976")
    seller_test.save()
    seller_test.uniqueid=str(seller_test.id)
    seller_test.save()

    import base64
    with open("./tests/classes/jester_pc.jpeg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    i1=Item()
    i1.createItem(name="test_buyrequest_item_heavy",category="electronics",seller=seller_test.name,price=1000,company="test",city="test",photo=encoded_string,info="nice heavy laptop",age=2,weight=501)
    i1.uploadToDB()
    
    i2=Item()
    i2.createItem(name="test_buyrequest_item",category="electronics",seller=seller_test.name,price=1000,company="test",city="test",photo=encoded_string,info="nice light laptop",age=2,weight=5)
    i2.uploadToDB()

    print("dummy creation successfull")
except Exception as e:
    print("dummy content creation failed",e)


# generate new buy request (heavy)
print("generate new buy request (heavy)")
status, msg = buyer_test.GenerateBuyRequest(i1.uniqueid, 1000)
print(status, msg)


# generate new buy request
print("generate new buy request")
status, msg = buyer_test.GenerateBuyRequest(i2.uniqueid, 1000)
print(status, msg)


# negotiation
print("negotiation")
status, msg = buyer_test.Negotiate(buyer_test.GetBuyRequests().first().uniqueid)
print(status, msg)


# change offer price
print("change offer price")
status, msg = buyer_test.ChangeOfferPrice(buyer_test.GetBuyRequests().first().uniqueid, 2000)
print(status, msg)


# reject request
print("reject request")
print(seller_test.RejectRequest(buyer_test.GetBuyRequests().first().uniqueid))

print("change offer price on rejected request")
status, msg = buyer_test.ChangeOfferPrice(buyer_test.GetBuyRequests().first().uniqueid, 2000)
print(status, msg)

print("approve rejected request")
print(seller_test.ApproveRequest(buyer_test.GetBuyRequests().first().uniqueid))

print("delete this buy request for further testsing")
try:
    buyer_test.GetBuyRequests().first().delete()
    print("success")
except:
    print("failed deletion")
# create new buy request to move further
print("generate new buy request for further testing")
status, msg = buyer_test.GenerateBuyRequest(i2.uniqueid, 1000)
print(status, msg)

# approve request
print("approve request")
print(seller_test.ApproveRequest(buyer_test.GetBuyRequests().first().uniqueid))


# approve payment

seller = buyer_test.GetBuyRequests().first().seller
print(seller.ApprovePayment(buyer_test.GetBuyRequests().first().uniqueid))

print("deleting dummies")
try:
    buyer_test.delete()
    seller_test.delete()
    i1.delete()
    i2.delete()
    print("success")
except:
    print("failed")