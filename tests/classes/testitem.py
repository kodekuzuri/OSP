import sys
sys.path.append(".")
from PIL import Image
from osp import Seller, Item
from osp import Category

c1=Category.objects(name="electronics").first()
s1=Seller.objects().first()

# print("round1")
i1=Item()
i1.createItem(name="test_item",category="electronics",seller=s1.name,price=1000,company="test",city="test",photo="jester_pc.jpeg",info="nice laptop",age=2,weight=5)
i1.uploadToDB()
# print("round2")

img1=Image.open(Item.objects().first().photo)
img1.show()