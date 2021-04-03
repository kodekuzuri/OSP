import sys
sys.path.append(".")

from osp import Buyer, Item, Seller

# buyer = Buyer.objects().first()
# item = Item.objects(name="The World Is Flat").first()

# generate new buy request (heavy)

# status, msg = buyer.GenerateBuyRequest(item.uniqueid, 1000)
# print(status, msg)


# generate new buy request

# status, msg = buyer.GenerateBuyRequest(item.uniqueid, 1000)
# print(status, msg)


# negotiation

# status, msg = buyer.Negotiate(buyer.GetBuyRequests().first().uniqueid)
# print(status, msg)


# change offer price

# status, msg = buyer.ChangeOfferPrice(buyer.GetBuyRequests().first().uniqueid, 2000)
# print(status, msg)


# reject request

# seller = buyer.GetBuyRequests().first().seller
# print(seller.RejectRequest(buyer.GetBuyRequests().first().uniqueid))


# approve request

# seller = buyer.GetBuyRequests().first().seller
# print(seller.ApproveRequest(buyer.GetBuyRequests().first().uniqueid))


# approve payment

# seller = buyer.GetBuyRequests().first().seller
# print(seller.ApprovePayment(buyer.GetBuyRequests().first().uniqueid))
