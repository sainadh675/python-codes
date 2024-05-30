import pymongo
import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime as dt

cluster=MongoClient('mongodb+srv://sainadh:5225@cluster0.ccwdr5m.mongodb.net/')
db=cluster.test
collection=db.employee
