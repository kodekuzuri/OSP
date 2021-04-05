import sys
sys.path.append(".")

from osp import Manager, Address, Buyer, Seller
import datetime

# dummy address for testing
addr = Address(houseNumber="A/306, Safal Parivesh", street="Aarohi Homes Lane", locality="South Bopal", city="Ahmedabad", state="Gujarat", pincode="380058").save()

print("#### Testing invalid fields in Manager (should raise exceptions) ####\n")
try:
    test_manager = Manager(gender="", dateOfBirth=datetime.datetime.strptime("2001-1-32", "%Y-%m-%d"), name="Test Manager", number="1234567890", email="random@random.com", password="testpassword", address=addr)
    test_manager.save()
    print("FAILED: Incorrect user saved successfully.")
except Exception as e:
    print(str(e))
    print("PASSED: Exceptions raised successfully.\n")

print("#### Testing correct fields in Manager (should save manager successfully) ####\n")
try:
    test_manager = Manager(gender="Male", dateOfBirth=datetime.datetime.strptime("2001-1-31", "%Y-%m-%d"), name="Test Manager", number="1234567890", email="random@random.com", password="testpassword", address=addr)
    test_manager.save()
    test_manager.uniqueid = str(test_manager.id)
    test_manager.save()
    print("PASSED: Correct manager saved successfully.\n")
except Exception as e:
    print(str(e))
    print("FAILED: Exceptions raised successfully.\n")


# dummy buyer for testing
test_buyer=Buyer(city="Noida test",password="abcd",email="testemail@email.com",name="test_buyer",number="9717911976")
test_buyer.save()
test_buyer.uniqueid=str(test_buyer.id)
test_buyer.save()

# dummy seller for testing
test_seller=Seller(city="Noida test",password="abcd",email="testemail@email.com",name="test_seller",number="9717911976")
test_seller.save()
test_seller.uniqueid=str(test_seller.id)
test_seller.save()

print("\n#### Testing manage buyer. (Existing Buyer)\n")
status, msg = test_manager.ManageBuyer(test_buyer.uniqueid)
if status:
    print("Passed.")
else:
    print("Failed.")
print(msg)

print("\n#### Testing manage seller. (Exisitng Seller)\n")
status, msg = test_manager.ManageSeller(test_seller.uniqueid)
if status:
    print("Passed.")
else:
    print("Failed.")
print(msg)


print("\n#### Testing manage buyer. (Non-Existing Buyer)\n")
status, msg = test_manager.ManageBuyer("nonexisting")
if not status:
    print("Passed.")
else:
    print("Failed.")
print(msg)

print("\n#### Testing manage seller. (Non-Exisitng Seller)\n")
status, msg = test_manager.ManageSeller("nonexisting")
if not status:
    print("Passed.")
else:
    print("Failed.")
print(msg)


print("\nDeletion of Items and BuyRequests on removal of buyer and seller checked in testBuyRequests")

# cleanup after testing
test_manager.delete()
addr.delete()