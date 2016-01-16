__author__ = 'ronanpiercehiggins'


import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter
import sys
import time
from tweepy import Stream
from tweepy.streaming import StreamListener


CONSUMER_KEY = 'uQIDLDayiNYrUoFiQaS8JkuOU'
CONSUMER_SECRET = 'kwYqW2fIceEovFyklPtuviMckincqtRwxqsJxiN7nhHq0mly35'
OAUTH_TOKEN = '2879848607-W9p7IneZ3uo37B8RYmESZhdTpDEZLAk1thEjaoV'
OAUTH_TOKEN_SECRET = 'rVpexhPWZU7gR7VbkSIMiew3qFhXZfdOCUzEYSDMIdJrD'

keyword_list =['python, ruby']

class MyStreamListener(StreamListener):
    def __init__(self):
        self.num_tweets=0

    def on_data(self, data):
        self.num_tweets += 1
        if self.num_tweets < 11:
            try:
                with open('tweet_mining.json', 'a') as tweet_file:
                    tweet_file.write(data)
                    return True
            except BaseException as e:
                print("Failed on_data: %s" % str(e))
            return True
        else:
            return False

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)