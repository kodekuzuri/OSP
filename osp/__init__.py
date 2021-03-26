from mongoengine import *

# connect to database
connect(host='mongodb+srv://ospapp:tyaLmQbvP6rJU4uY@smmh.yappb.mongodb.net/ospDatabase?retryWrites=true&w=majority') # make this environment variable finally

# make all relevant classes available directly
from osp.classes import *

# make all relevant interfaces available directly
from osp.interfaces import *
