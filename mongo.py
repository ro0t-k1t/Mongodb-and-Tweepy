__author__ = 'ronanpiercehiggins'


import pymongo

def mongo_connect():
    try:
        conn = pymongo.MongoClient()
        print "Mongo is connected"
        return conn
    except pymongo.errors.ConnectionFailure, e:
        print "Could not connect to MongoDb: %s" % e

conn = mongo_connect()
db = conn['twitter_stream']
coll = db.my_collection
docs = [{"name": "Henry", "surname": "Moore", "twitter": "@henrymoore"}, {"name": "Stephen", "surname": "Fry", "twitter": "@stephenfry"}]
coll.insert_many(docs)
results = coll.find()
print results

print db.collection_names()
print conn.database_names()