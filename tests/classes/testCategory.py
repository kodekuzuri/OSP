import sys
sys.path.append(".")

from osp import Category

# print initial list
print([category.name for category in Category.objects()])

# testing new additions (correct)
print("adding existing category, TestCat1")
status, msg = Category.AddCategory("TestCat1")
print(status, msg)
print()

print("adding new category, TestCat2")
status, msg = Category.AddCategory("TestCat2")
print(status, msg)
print()

# print list after addition
print([category.name for category in Category.objects()])
print()

# testing new additions (empty name)
print("construction with wrong params")
status, msg = Category.AddCategory("")
print(status, msg)
print()

# # testing new additions (same name)
# status, msg = Category.AddCategory("TestCat1")
# print(status, msg)

# testing removal (existing)
print("testing removal (existing)")
cat = Category.objects(name="TestCat2").first()
status, msg = Category.RemoveCategory(cat.uniqueid)
print(status, msg)
print()

# print list after removal
print([category.name for category in Category.objects()])
print()

# testing removal (non-existing)
print("testing removal (non-existing)")
status, msg = Category.RemoveCategory("random")
print(status, msg)
print()
