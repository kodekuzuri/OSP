import sys
sys.path.append(".")

from osp import Seller, Item
from osp import Category

c1=Category.objects(name="electronics").first()
s1=Seller.objects().first()

print("round1")
i1=Item()
i1.createItem(name="laptop",category="electronics",seller=s1.name,price=1000,company="acer",city="delhi",photo="./tests/classes/jester_pc.jpeg",info="nice laptop",age=2,weight=5)
i1.uploadToDB()
print("round2")
# print(Item.objects().first())