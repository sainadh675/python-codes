import pymongo  
from pymongo import MongoClient
cluster=MongoClient("mongodb+srv://sainadh:5225@cluster0.ccwdr5m.mongodb.net/")
db=cluster.test
collection=db.book

schema = {
    'bsonType': 'object',
    'required': ['name', 'age'],
    'properties': {
        'name': {
            'bsonType': 'string',
            'description': 'must be a string and is required'
        },
        'age': {
            'bsonType': 'int',
            'minimum': 0,
            'maximum': 150,
            'description': 'must be an integer between 0 and 150'
        }
    }
}
# db.create_collection('book',validator={'$jsonSchema':schema})
# db.book.insert_one({'name':'sai','age':22})

collection.insert_one({'name':'muthukuri','age':155})