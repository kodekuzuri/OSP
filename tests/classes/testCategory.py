import sys
sys.path.append(".")

from osp import Category

# print initial list
print([category.name for category in Category.objects()])

# testing new additions (correct)
status, msg = Category.AddCategory("TestCat1")
print(status, msg)

status, msg = Category.AddCategory("TestCat2")
print(status, msg)

# print list after addition
print([category.name for category in Category.objects()])

# testing new additions (empty name)
status, msg = Category.AddCategory("")
print(status, msg)

# testing new additions (same name)
status, msg = Category.AddCategory("TestCat1")
print(status, msg)

# testing removal (existing)
cat = Category.objects(name="TestCat2").first()
status, msg = Category.RemoveCategory(cat.uniqueid)
print(status, msg)

# print list after removal
print([category.name for category in Category.objects()])

# testing removal (non-existing)
status, msg = Category.RemoveCategory("random")
print(status, msg)
