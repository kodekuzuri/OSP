import sys
sys.path.append(".")

import datetime
from osp import ManagerSignUp, CustomerSignUp

# testing for manager

data1 = {
    'name': 'Nisarg Upadhyaya',
    'email': 'nisarg1631@gmail.com',
    'number': '1234567890',
    'address': {
        'houseNumber': 'OSP',
        'street': 'OSP',
        'locality': 'OSP',
        'city': 'OSP',
        'state': 'OSP',
        'pincode': '123456'
    },
    'gender': 'Male',
    'dob': datetime.date(2001,3,16)
}

status, msg = ManagerSignUp(data1)

print(status)
print(msg)

# repeate with same email

data2 = {
    'name': 'Nisarg Upadhyaya',
    'email': 'nisarg1631@gmail.com',
    'number': '1234567890',
    'address': {
        'houseNumber': 'OSP',
        'street': 'OSP',
        'locality': 'OSP',
        'city': 'OSP',
        'state': 'OSP',
        'pincode': '123456'
    },
    'gender': 'Male',
    'dob': datetime.date(2001,3,16)
}

status, msg = ManagerSignUp(data2)

print(status)
print(msg)

# testing for buyer

data3 = {
    'name': 'Nisarg Upadhyaya',
    'email': 'nisarg1631@gmail.com',
    'number': '1234567890',
    'city': 'Ahmedabad'
}

status, msg = CustomerSignUp(data3, isBuyer=True)

print(status)
print(msg)

# repeate with same email

data4 = {
    'name': 'Nisarg Upadhyaya',
    'email': 'nisarg1631@gmail.com',
    'number': '1234567890',
    'city': 'Ahmedabad'
}

status, msg = CustomerSignUp(data4, isBuyer=True)

print(status)
print(msg)

# testing for seller

data5 = {
    'name': 'Nisarg Upadhyaya',
    'email': 'nisarg1631@gmail.com',
    'number': '1234567890',
    'city': 'Ahmedabad'
}

status, msg = CustomerSignUp(data5, isBuyer=False)

print(status)
print(msg)

# repeate with same email

data6 = {
    'name': 'Nisarg Upadhyaya',
    'email': 'nisarg1631@gmail.com',
    'number': '1234567890',
    'city': 'Ahmedabad'
}

status, msg = CustomerSignUp(data6, isBuyer=False)

print(status)
print(msg)
