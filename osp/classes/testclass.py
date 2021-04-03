from mongoengine import *


class TestClass(Document):
    def _check_id(val):
        if TestClass.objects(id_=val).count():
            raise ValidationError('ID exists')

    name = StringField(required=True, min_length=1)
    email = EmailField(required=True)
    id_ = StringField(required=True, validation=_check_id)

class TestClass2(Document):
    tc1 = ListField(ReferenceField(TestClass, reverse_delete_rule=PULL))

BUY_REQUEST_STATUS = ((0, 'Rejected'), (1, 'Pending'), (2, 'Approved'))
class TestClass3(Document):
    name = StringField(required=True, min_length=1)
    status = IntField(default=1, choices=BUY_REQUEST_STATUS)

    @staticmethod
    def listall():
        for item in TestClass3.objects():
            print(item.name)
