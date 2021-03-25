from mongoengine import *

connect(host='mongodb+srv://ospapp:tyaLmQbvP6rJU4uY@smmh.yappb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

# inherit all classes from Document, can directly save the data to mongodb
class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

    def foo1(self, other):
        other.first_name = "Name is now set"
        print(self.email + " says hi to " + other.email)
        print("Hello")

# accessing saved objects from mongodb
nissu = User.objects(email="nisarg1631@gmail.com").first()
other = User.objects(email="yo@yo.com").first()


# can still use them as traditional python objects
nissu.foo1(other)
print(other.email, other.first_name)
other.save()

# creating new user

# a = User()
# a.email = "nisarg1631@gmail.com"

# b = User()
# b.email = "yo@yo.com"


# using them as traditional python objects
# b.foo1(a)
# a.foo1(b)

# a.save()
# b.save()
