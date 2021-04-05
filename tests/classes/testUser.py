import sys
sys.path.append(".")

from osp import User

print("#### Testing invalid fields in User (should raise exceptions) ####\n")
try:
    test_user = User(name="", number="0123456789", email="random@random", password="testpassword")
    test_user.save()
    print("FAILED: Incorrect user saved successfully.")
except Exception as e:
    for key, value in e.__dict__["errors"].items():
        print(f"{key}: {value}")
    print("PASSED: Exceptions raised successfully.\n")

print("#### Testing correct fields in user (should save user successfully) ####\n")
try:
    test_user = User(name="Nisarg Upadhyaya", number="1234567890", email="random@random.com", password="testpassword")
    test_user.save()
    test_user.uniqueid = str(test_user.id)
    test_user.save()
    print("PASSED: Correct user saved successfully. Assigned unique ID to user.\n")
    print(f"#### Querying database for users with assigned ID")
    count = User.objects(uniqueid=test_user.uniqueid).count()
    test_user.delete()
    if count == 1:
        print("PASSED: Query returned 1 user only.")
    else:
        raise Exception("More than 1 user with same ID present.")
except Exception as e:
    for key, value in e.__dict__["errors"].items():
        print(f"{key}: {value}")
    print("FAILED: Correct user raised exceptions.\n")
