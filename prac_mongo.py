from pymongo import MongoClient
from pymongo import MongoClient
import certifi

mongo_srv = 'mongodb+srv://user:1234@cluster1.b5dbq8u.mongodb.net/?retryWrites=true&w=majority'
# client = MongoClient(mongo_srv)

ca = certifi.where();

client = MongoClient(mongo_srv, tlsCAFile=ca)
db = client.rgorithm


# CRUD
# Create
doc = {
 'name':'bob',
 'age':27
}
doc2 = {
 'name':'joe',
 'age':11
}
doc3 = {
 'name':'sam',
 'age':43
}
doc4 = {
 'name':'dave',
 'age':56
}

# Read
user = list(db.users.find({'name': 'sam'}))
print(user)
#
user = list(db.users.find_one({'name': 'sam'}, {'_id': False}))
print(user)
# print(all_users[0])

# for user in all_users:
#     print(user)

# create
# db.users.insert_one(doc)


# Update
db.users.update_one({'name': 'sam'}, {'$set': {'age': 34}})

# Delete
db.users.delete_one({'name': 'dave'})

