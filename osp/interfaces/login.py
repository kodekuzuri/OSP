from osp.classes import Manager, Buyer, Seller


def Login(userId, password, type=0):
    """
    Login functionality to check if the credenials entered by the user are valid

    Returns true if the login is a valid one, else returns false

    type = 0 (default) corresponds to manager login\n
    type = 1 corresponds to buyer login\n
    type = 2 (or anything else other than 0 and 1) corresponds to seller login
    """

    if type == 0:
        return True if Manager.objects(userId=userId, password=password).count() else False
    
    elif type == 1:
        return True if Buyer.objects(userId=userId, password=password).count() else False
    
    else:
        return True if Seller.objects(userId=userId, password=password).count() else False
