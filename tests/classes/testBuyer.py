import sys
sys.path.append(".")

from osp import Buyer
print("testing class Buyer")
print("testing constructor with correct parameters")
try:
    c1=Buyer(city="Noida test",password="abcd",email="testemail@email.com",name="test_buyer",number="9717911976")
    c1.save()
    c1.uniqueid=str(c1.id)
    c1.save()
    print("Passed")
except Exception as e:
    print("Failed",e)

print("testing constructor with incorrect parameters")
try:
    c1=Buyer(city="$",password="abcd",email="testemail@email.com",name="",number="9717911976")
    c1.save()
    c1.uniqueid=str(c1.id)
    c1.save()
    print("Failed")
    Buyer.objects(city="$").first().delete()
except:
    print("passed")


print("testing deletion of buyer")
try:
    Buyer.objects(city="Noida test").first().delete()
    print("Passed")
except Exception as e:
    print("failed",e)


print("Other buyer functions tested with buyrequests")