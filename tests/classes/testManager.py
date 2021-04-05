import sys
sys.path.append(".")

from osp import Manager, Address
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




# cleanup after testing
test_manager.delete()
addr.delete()