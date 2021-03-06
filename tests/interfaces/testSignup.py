import sys
sys.path.append(".")

import datetime
from osp import ManagerSignUp, CustomerSignUp

# testing for manager

data1 = {
    'name': 'OSP Manager',
    'email': 'osp.noreply@gmail.com',
    'number': '1234567890',
    'houseNumber': 'OSP',
    'street': 'OSP',
    'locality': 'OSP',
    'city': 'OSP',
    'state': 'OSP',
    'pincode': '123456',
    'gender': 'Male',
    'dob': '2001-01-01'
}

status, msg = ManagerSignUp(data1)

print(status)
print(msg)

# repeate with same email

data2 = {
    'name': 'OSP Manager',
    'email': 'osp.noreply@gmail.com',
    'number': '1234567890',
    'houseNumber': 'OSP',
    'street': 'OSP',
    'locality': 'OSP',
    'city': 'OSP',
    'state': 'OSP',
    'pincode': '123456',
    'gender': 'Male',
    'dob': '2001-01-01'
}

status, msg = ManagerSignUp(data2)

print(status)
print(msg)

# testing for buyer

data3 = {
    'name': 'OSP Buyer',
    'email': 'osp.noreply@gmail.com',
    'number': '1234567890',
    'city': 'OSP'
}

status, msg = CustomerSignUp(data3, isBuyer=True)

print(status)
print(msg)

# repeate with same email

data4 = {
    'name': 'OSP Buyer',
    'email': 'osp.noreply@gmail.com',
    'number': '1234567890',
    'city': 'OSP'
}

status, msg = CustomerSignUp(data4, isBuyer=True)

print(status)
print(msg)

# testing for seller

data5 = {
    'name': 'OSP Seller',
    'email': 'osp.noreply@gmail.com',
    'number': '1234567890',
    'city': 'OSP'
}

status, msg = CustomerSignUp(data5, isBuyer=False)

print(status)
print(msg)

# repeate with same email

data6 = {
    'name': 'OSP Seller',
    'email': 'osp.noreply@gmail.com',
    'number': '1234567890',
    'city': 'OSP'
}

status, msg = CustomerSignUp(data6, isBuyer=False)

print(status)
print(msg)
