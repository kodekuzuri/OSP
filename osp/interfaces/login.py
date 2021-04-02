from osp.classes import Manager, Buyer, Seller


def Login(userId, password, type=0):
    """
    Login functionality to check if the credenials entered by the user are valid

    Returns user if the login is a valid one, else returns none

    type = 0 (default) corresponds to manager login\n
    type = 1 corresponds to buyer login\n
    type = 2 (or anything else other than 0 and 1) corresponds to seller login
    """

    if type == 0:
        return  Manager.objects(uniqueid=userId, password=password).first()
    
    elif type == 1:
        return Buyer.objects(uniqueid=userId, password=password).first()
    
    else:
        return Seller.objects(uniqueid=userId, password=password).first()
