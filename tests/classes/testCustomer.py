import sys
sys.path.append(".")

from osp import Customer
print("testing class customer")
print("testing constructor with correct parameters")
try:
    c1=Customer(city="Noida test",password="abcd",email="testemail@email.com",name="test_customer",number="9717911976")
    c1.save()
    c1.uniqueid=str(c1.id)
    c1.save()
    print("Passed")
except Exception as e:
    print("Failed",e)

print("testing constructor with incorrect parameters")
try:
    c1=Customer(city="$",password="abcd",email="testemail@email.com",name="test_customer",number="9717911976")
    c1.save()
    c1.uniqueid=str(c1.id)
    c1.save()
    print("Failed")
    Customer.objects(city="$").first().delete()
except:
    print("passed")


print("testing deletion of customer")
try:
    Customer.objects(city="Noida test").first().delete()
    print("Passed")
except Exception as e:
    print("failed",e)