from osp import *
import datetime
import secrets, string, random
import os

obj = TestClass3.objects().first()
obj.delete()
print(TestClass3.objects().count())

# obj = Seller.objects(name="OSP Seller").first()
# print(obj.GetItems())

# print(type(os.environ["OSP_DATABASE"]))
# print(type(os.environ["OSP_MAIL"]))
# print(type(os.environ["OSP_PASSWORD"]))
# print(type(os.environ["OSP_APPKEY"]))

# a = datetime.datetime.strptime("2001-03-16", "%Y-%m-%d")
# print(a)

# a = TestClass3()
# a.name = 'Nisarg'
# a.save()

# b = TestClass3()
# b.name = 'Animesh'
# b.save()

# TestClass3.listall()

# user = TestClass3.objects(id='605f029e136846e6154d34c2').first()

# if user:
#     print(user.name)
# else:
#     print("doesnt exist")



# def GeneratePassword():
#     """
#     Utility function to generate random passwords
#     """
#     passlen = random.randint(6,10)
#     passchars = string.ascii_letters+string.digits+'@_!$'
#     return ''.join(secrets.choice(passchars) for _ in range(passlen))

# for _ in range(40):
#     print(GeneratePassword())

# a = TestClass3()
# a.name = "nisarg"
# a.email = "yo@yo.com"
# a.save()
# c = str(a.id)
# print(type(a.name))
# print(Login("admin", "admin",0))

# a = Manager()
# a.userId = "admin"
# a.password = "admin"
# a.name = "sysadmin"
# a.email = "admin@osp.com"
# a.number = "1234567890"
# a.address = Address(houseNumber="1/OSP", locality="OSP", city="OSP", state="OSP", pincode="123 456").save()
# a.gender = "N/A"
# a.dateOfBirth = datetime.date(2021,1,1)
# a.save()
# a.delete()

# a = TestClass3("Nisarg","nisarg1631@gmail.com")
# a.save()

# user = TestClass3.objects().first()
# print(user.name)
# for user in TestClass3.objects():
#     print(user.name)

# a = TestClass3()
# a.name = "Nisarg Upadhyaya"
# a.email = "hello@hello.com"
# a.id_ = "12346"
# a.phone = "9009009090"

# b = TestClass3()
# b.name = "LOLOLOL"
# b.email = "hello@hello.com"
# b.id_ = "12347"
# b.phone = "9009009090"

# print(a.name, b.name)
# try:
#     a.save()
# except Exception as e:
#     for key,val in e.__dict__['errors'].items():
#         print(key,val)

# d = TestClass3()
# d.name = "Hello"
# d.email = "yo@yo.com"
# d.id_ = "3214"
# d.phone = "83428934"
# d.save()

# for user in TestClass.objects():
#     print(user.name)

# b = TestClass()
# b.id_ = "1235"
# b.email = "hello@something.com"
# b.name = "Parth Ajmera"
# b.save()

# a = TestClass.objects(name="Parth Ajmera").first()
# a.delete()

# c = TestClass2(tc1=TestClass.objects())
# c.save()

# d = TestClass2(tc1=TestClass.objects(name="Nisarg Upadhyaya"))
# d.save()

# c = TestClass2.objects().first()

# for user in c.tc1:
#     print(user.name)

# print(c.tc1[1].name)

# a = TestClass.objects(name="Nisarg Upadhyaya")
# for user in a:
#     print(user.id)

# b = TestClass()
# b.id_ = "1234"
# b.email = "hello@something.com"
# b.name = "nothing"
# b.save()
# print(b._object_key)

# from mongoengine import *

# connect(host='mongodb+srv://ospapp:tyaLmQbvP6rJU4uY@smmh.yappb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

# # inherit all classes from Document, can directly save the data to mongodb
# class User(Document):
#     email = StringField(required=True)
#     first_name = StringField(max_length=50)
#     last_name = StringField(max_length=50)

#     def foo1(self, other):
#         other.first_name = "Name is now set"
#         print(self.email + " says hi to " + other.email)
#         print("Hello")

# # accessing saved objects from mongodb
# nissu = User.objects(email="nisarg1631@gmail.com").first()
# other = User.objects(email="yo@yo.com").first()


# # can still use them as traditional python objects
# nissu.foo1(other)
# print(other.email, other.first_name)
# other.save()

# # creating new user

# # a = User()
# # a.email = "nisarg1631@gmail.com"

# # b = User()
# # b.email = "yo@yo.com"


# # using them as traditional python objects
# # b.foo1(a)
# # a.foo1(b)

# # a.save()
# # b.save()
