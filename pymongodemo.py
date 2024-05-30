import pymongo
import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime as dt

cluster=MongoClient('mongodb+srv://sainadh:5225@cluster0.ccwdr5m.mongodb.net/')
db=cluster.test
collection=db.employee
author_collection=db.author

printer=pprint.PrettyPrinter()
#inserting into document

post={"name":"sainadh","email":"sainadh@gmail.com","age":25}
#collection.insert_one(post)

#reading data from collection

results=collection.find_one({"name":"sai"})

#print(results)

#collection.delete_one({"last_name":"Muthukuri"})
def create_documents():
    first_names=["sainadh","mounika","venkatesh"]
    last_names=["Muthukuri","pulivarthi","N"]
    ages=[24,24,25]
    docs=[]
    
    for first_name,last_name,age in zip(first_names,last_names,ages):
        doc={"first_name":first_name,"last_name":last_name,"age":age}
        docs.append(doc)
    #collection.insert_many(docs)
create_documents()

#updating records in the collections

def update_byname(name):
    updatedata={
        "$set":{"phno":8374},
        "$inc":{"age":1}

    }
    collection.update_one({"name":"sainadh"},updatedata)
#update_byname("sainadh")

#Replacing the data in the collection

def replace_byid(person_id):
    from bson.objectid import ObjectId
    _id=ObjectId(person_id)
    repl={
        "name":"sai"
    }
    collection.replace_one({"_id":_id},repl)
#replace_byid("6639f79a0502d32ddb0ef702")

#deleting the data from the collection


#collection.delete_one({"name":"sai"})

#giving id manually

add={
    "_id":101,
    "name":"sai",
    "email":"sai@gmail.com"
}
#collection.insert_one(add)


#counting total number of documets present in the db

def count_all():
    count=collection.count_documents(filter={})
    print("number of documents:",count)
#count_all()

def person_by_id(person_id):
    from bson.objectid import ObjectId
    _id=ObjectId(person_id)
    person=collection.find_one({"_id":_id})
    print(person)
#person_by_id("6639d6dfcfd64e7ba8ae4e1b")
 
def get_age_range(min_age,max_age):
    qery={"$and":[
        {"age":{"$gte":min_age}},
        {"age":{"$lte":max_age}}
    ]
    }
    people=collection.find(qery).sort("age")
    for person in people:
        print(person)
#get_age_range(15,30)


#creating collection----

#db.create_collection("author")


#adding bulk data----

def bulk_data():
    authors=[
        {
            "firstn_name":"sai",
            "last_name":"muthukuri",
            "date_of_birth":dt(2000,6,16)
        },
        {
            "firstn_name":"Brahmini",
            "last_name":"Muthukuri",
            "date_of_birth":dt(1999,7,11)
        },
        {
            "firstn_name":"Lakshmi",
            "last_name":"Venkata",
            "date_of_birth":dt(1999,6,24)
        }
    ]
    author_collection.insert_many(authors)
#bulk_data()

# retrreving all the data in the data in the collection with specific name

authors_containing_muthukuri=author_collection.find({"firstn_name":{"$regex":"a{1}"}})
#printer.pprint(list(authors_containing_muthukuri))

address={
    "_id":'6639d6dfcfd64e7ba8ae4e1a',
    'Apartment name':'sai sree residency',
    'street':'viduth nagar',
    'Area':'jammu narayana puram',
    'city':'vizianagram',
    'pincode':535002
}

#adding relations to already exisiting documents

def add_adress_relation(person_id,address):
    from bson.objectid import ObjectId
    _id=ObjectId(person_id)
    collection.update_one({'_id':_id},{'$addToSet':{'addresses':address}})
add_adress_relation('6639d6dfcfd64e7ba8ae4e1a',address)

