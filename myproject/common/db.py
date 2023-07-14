# import pymongo
# from pymongo import MongoClient

# # client = MongoClient('mongodb+srv://bujairvk111:sLJZe1GqwJafvCkZ@cluster0.lsvowi0.mongodb.net/?retryWrites=true&w=majority')
# client = MongoClient('mongodb+srv://bujairvk111:sLJZe1GqwJafvCkZ@cluster0.lsvowi0.mongodb.net/test')
# db = client['finance']

# import pymongo
# from pymongo import MongoClient
# from django.conf import settings

# client = pymongo.MongoClient('mongodb+srv://bujairvk111:sLJZe1GqwJafvCkZ@cluster0.lsvowi0.mongodb.net/?retryWrites=true&w=majority')
# db = client['finance']

# collection = db['sample']
# collection.insert_one({'name': 'bujair', 'age': 20})


import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient('mongodb+srv://bujair:12345@database.jvyfog0.mongodb.net/?retryWrites=true&w=majority')
db = client['finance']

# Select a collection
collection = db['budget']



