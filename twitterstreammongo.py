__author__ = 'ronanpiercehiggins'


import json
import pymongo
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

CONSUMER_KEY = 'uQIDLDayiNYrUoFiQaS8JkuOU'
CONSUMER_SECRET = 'kwYqW2fIceEovFyklPtuviMckincqtRwxqsJxiN7nhHq0mly35'
OAUTH_TOKEN = '2879848607-W9p7IneZ3uo37B8RYmESZhdTpDEZLAk1thEjaoV'
OAUTH_TOKEN_SECRET = 'rVpexhPWZU7gR7VbkSIMiew3qFhXZfdOCUzEYSDMIdJrD'

keyword_list = ['france']

class MyStreamListener(StreamListener):
    def __init__(self, api=None):

        self.num_tweets = 0
        self.tweet_coll = None

    def mongo_connect(self):
        try:
            client = pymongo.MongoClient()
            print "Mongo is connected!"
            self.db = client.tech_tweetsDB
            #self.db.tweets.drop()
            self.tweet_coll = self.db.tweets

        except pymongo.errors.ConnectionFailure, e:
            print "Could not connect to MongoDB: %s" % e

    def on_data(self, data):
        try:
            status = json.loads(data)
            #print json.dumps(status, indent=4)

            tweet = {}
            tweet["text"] = status["text"].encode('utf-8')
            tweet["screen_name"] = status["user"]['screen_name']
            tweet['followers_count'] = status['user']['followers_count']
            tweet['friends_count'] = status['user']['friends_count']
            tweet['favorite_count'] = status['favorite_count']
            tweet['retweet_count'] = status['retweet_count']

            #print status.get('entities').get("media")
            if status.get('entities').get("media"):
                #print status.get('entities').get("media")
                media = status['entities']['media']
                tweet['media'] = media[0]["display_url"]
            else:
                tweet['media'] = None #good database practise to set anythong empty with None

            tweet['lang'] = status['user']['lang']
            tweet['location'] = status['user']['location']



            print self.num_tweets
            if self.num_tweets < 3:
                self.tweet_coll.insert(tweet)
                #print "droptest"
                self.num_tweets += 1


                return True
            else:
                return False

            return True

        except BaseException as e:
            print("Failed on_data: %s" % str(e))

        return True

    def on_error(self, status):
        print(status)
        return True


    def delete_database(self):

        self.db.tweets.drop()
        results = self.db.tweets.find()
        print results.count()







auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

stream = MyStreamListener()

stream.mongo_connect()


twitter_stream = Stream(auth, stream)

twitter_stream.filter(track=keyword_list)

#stream.delete_database()


