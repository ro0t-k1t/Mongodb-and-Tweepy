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
db = conn['tech_tweetsDB']
coll = db.tweets
coll.drop()
"""docs = [{"name": "Henry", "surname": "Moore", "twitter": "@henrymoore"}, {"name": "Stephen", "surname": "Fry", "twitter": "@stephenfry"}]
coll.insert_many(docs)
results = coll.find({"name": "Henry"})
for doc in results:
    print doc

print results.count()
print coll.count()"""