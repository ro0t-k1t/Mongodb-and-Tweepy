__author__ = 'ronanpiercehiggins'

import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter

CONSUMER_KEY = 'qqkcE7INHDimxZ9xhkF3beD9m'
CONSUMER_SECRET = 'wtbrFDEI1vicUTR7QRKAg0j9l6Ft38yHCdgdxEFnqkVPuXkn9B'
OAUTH_TOKEN = '2879848607-wU6dmnGeRswVr5A6qUmse4onk8b2qJsIN2OtAcz'
OAUTH_TOKEN_SECRET = 'DAxU0puUdpdgRbkVRXTn1CPoOwetpShKaNbUAtVZ6ZwAQ'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 10
query = 'Taylor Swift'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets = 10

pop_tweets = [status for status in results if status._json['retweet_count'] > min_retweets]

# create a dictionary of tweet text and associated re tweets
tweets_tup = tuple([(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count']) for tweet in pop_tweets])








pop_tweets_set = set(tweets_tup)


sorted_tweets_tup = sorted(pop_tweets_set, key=itemgetter(1), reverse=True)[:5]

table = PrettyTable(field_names=['Text', 'Retweet Count'])

for key, val in sorted_tweets_tup:
    table.add_row([key, val])
table.max_width['Text'] = 50
table.align['Text'], table.align['Retweet Count'] = '1', 'r'

print table
