# ADDRESS DATA MEMBER

class Address:
    def __init__(self, house_no, street, locality, city, state, pincode):
        self.house_no = house_no
        self.street = street
        self.locality = locality
        self.city = city
        self.state = state
        self.pincode = pincode


# END OF ADDRESS DATA MEMBER DECLARATION


# CATEGORY CLASS

class Category:

    categories_list = []

    def __init__(self,  value):
        self.value = value
        id = "random generation pls"
        self.id = id

    def getType(self):
        return self.value

    def getID(self):
        return self.id
      
 # END OF ITEM CLASSES DECLARATION 

# ITEM CLASS

class Item:

    # pls check once if this has to be static
    item_list = []

    def __init__(self, name, category, seller, price, company, city, photo, info, is_heavy, age=None):
        self.name = name
        self.category = category
        self.seller = seller
        self.price = price
        self.company = company
        self.city = city
        self.photo = photo
        self.info = info
        self.is_heavy = is_heavy
        if age is None:
            self.age = 0
        else:
            self.age = age

    def getInfo(self):
        # return dict
        pass

    def search(self, s):
        # search in item_list
        pass


# END OF ITEM CLASS DECLARATION


# USER CLASS DATA MEMBER

class User:
    def __init__(self, name, telephone_number, email, password=None):

        self.name = name
        self.telephone_number = telephone_number
        self.email = email

        user_id = "nahi aata random string generation"
        self.user_id = user_id

        if password is not None:
            # and self.verifyPassword(password) is True ? ye condition add karna hai ?
            self.password = password
        else:
            password = "Random generated password"
            self.password = password

    def verifyPassword(self, s):
        pass

    def getInfo(self):
        # return dict
        pass


# END OF USER CLASS DECLARATION


# MANAGER CLASS

class Manager(User):

    def __init__(self, name, telephone_number, email, address, gender, date_of_birth, password=None):
        # self.super.__init__(name, telephone_number, email, password)
        super().__init__(name, telephone_number, email, password)
        self.address = address
        self.gender = gender
        self.date_of_birth = date_of_birth

    def audit(self):
        pass

    def manageBuyer(self, buyer):
        pass

    def manageSeller(self, seller):
        pass

    def remove(self):
        pass

    def removeItem(self, item):
        pass

    def negotiation(self, buyer, seller):
        pass

    def getInfo(self):
        # return dict
        pass

# END OF MANAGER CLASS DECLARATION


# CUSTOMER CLASS

class Customer(User):
    def __init__(self, name, telephone_number, email, city, password=None):
        super().__init__(name, telephone_number, email, password)
        self.city = city

# END OF CUSTOMER CLASS


# REQUEST CLASS

class Request:
    def __init__(self, item, buyer, seller, offered_price, status, payment_status):
        self.item = item
        self.buyer = buyer
        self.seller = seller
        self.offered_price = offered_price


# END OF REQUEST CLASS


# BUYER CLASS

class Buyer(Customer):
    def __init__(self, name, telephone_number, email, city, password=None):
        super().__init__(name, telephone_number, email, city, password)
        self.requests = []

    def generateBuyRequest(self, item, price):
        pass

    def getInfo(self):
        # return dict
        pass

# END OF BUYER CLASS



# SELLER CLASS

class Seller(Customer):
    def __init__(self, name, telephone_number, email, city, password=None):
        super().__init__(name, telephone_number, email, city, password)
        self.items = []
        self.requests = []

    def uploadItem(self, item):
        pass

    def removeItem(self, item):
        pass

    def modifyRequestStatus(self, buy_request):
        pass

    def approvePaymentStatus(self, buy_request):
        pass

    def getInfo(self):
        # return dict
        pass

# END OF SELLER CLASS DECLARATION




