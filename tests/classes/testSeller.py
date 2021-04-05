import sys
sys.path.append(".")

from osp import Seller
print("testing class Seller")
print("testing constructor with correct parameters")
try:
    c1=Seller(city="Noida test",password="abcd",email="testemail@email.com",name="test_seller",number="9717911976")
    c1.save()
    c1.uniqueid=str(c1.id)
    c1.save()
    print("Passed")
except Exception as e:
    print("Failed",e)

print("testing constructor with incorrect parameters")
try:
    c1=Seller(city="$",password="abcd",email="testemail@email.com",name="",number="9717911976")
    c1.save()
    c1.uniqueid=str(c1.id)
    c1.save()
    print("Failed")
    Seller.objects(city="$").first().delete()
except:
    print("passed")


print("testing deletion of seller")
try:
    Seller.objects(city="Noida test").first().delete()
    print("Passed")
except Exception as e:
    print("failed",e)


print("Other seller functions tested with buyrequests")