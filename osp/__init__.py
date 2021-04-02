import mongoengine as me
import os

# connect to database
me.connect(host=os.environ["OSP_DATABASE"]) # make this environment variable finally

# make all relevant classes available directly
from osp.classes import *

# make all relevant interfaces available directly
from osp.interfaces import *
