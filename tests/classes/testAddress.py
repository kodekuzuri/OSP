import sys
sys.path.append(".")

from osp import Address

print("#### Testing empty fields in address (should raise exceptions) ####\n")
try:
    Address(houseNumber="", street="", locality="", city="", state="", pincode="").save()
    print("FAILED: Incorrect address saved successfully.")
except Exception as e:
    for key, value in e.__dict__["errors"].items():
        print(f"{key}: {value}")
    print("PASSED: Exceptions raised successfully.\n")


print("#### Testing invalid fields in address (should raise exceptions) ####\n")
try:
    Address(houseNumber="@-402", street="?Lane", locality="mira_bhayandar", city="new0delhi", state="dehradun123", pincode="876gh3").save()
    print("FAILED: Incorrect address saved successfully.")
except Exception as e:
    for key, value in e.__dict__["errors"].items():
        print(f"{key}: {value}")
    print("PASSED: Exceptions raised successfully.\n")

print("#### Testing correct fields in address (should save address successfully) ####\n")
try:
    Address(houseNumber="A/306, Safal Parivesh", street="Aarohi Homes Lane", locality="South Bopal", city="Ahmedabad", state="Gujarat", pincode="380058").save()
    print("PASSED: Correct address saved successfully.")
except Exception as e:
    for key, value in e.__dict__["errors"].items():
        print(f"{key}: {value}")
    print("FAILED: Correct address raised exceptions.\n")
