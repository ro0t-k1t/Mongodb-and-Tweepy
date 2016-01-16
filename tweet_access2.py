__author__ = 'ronanpiercehiggins'

import json
import tweepy

from tweepy import OAuthHandler

from collections import Counter

from prettytable import PrettyTable

CONSUMER_KEY = 'uQIDLDayiNYrUoFiQaS8JkuOU'
CONSUMER_SECRET = 'kwYqW2fIceEovFyklPtuviMckincqtRwxqsJxiN7nhHq0mly35'
OAUTH_TOKEN = '2879848607-W9p7IneZ3uo37B8RYmESZhdTpDEZLAk1thEjaoV'
OAUTH_TOKEN_SECRET = 'rVpexhPWZU7gR7VbkSIMiew3qFhXZfdOCUzEYSDMIdJrD'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 10
query = 'Taylor Swift'

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [status._json['text'] for status in results]

screen_names = [status._json['user']['screen_name']
                for status in results
                for mention in status._json['entities']['user_mentions']]
hashtags = [hashtag['text']
            for status in results
            for hashtag in status._json['entities']['hashtags']]
words = [w for t in status_texts
         for w in t.split()]

"""for entry in [screen_names, hashtags, words]: #screen names, hasttags is a list! A list gets put into entry
    counter = Counter(entry)
    print counter.most_common()[:10]
    print"""



for label, data in (('Text', status_texts),('Screen Name', screen_names),('Word', words)):
    table = PrettyTable(field_names=[label, 'Counter'])
    counter = Counter(data)
    [ table.add_row(entry) for entry in counter.most_common()[:3]]
    table.align[label], table.align['count'] = 'l', 'm'
    print table



#List comps = you are essetnially looking to find whatever expression you say first
#inside the loop.


def get_lexical_diversity(items):
    return 1.0*len(set(items))/len(items)

def get_average_words(tweets):
    total_words = sum([ len(tweet.split()) for tweet in tweets])
    return 1.0*total_words/len(tweets)

print "Average words: %s" % get_average_words(status_texts)
print "Words Diversity: %s" % get_lexical_diversity(words)
print "Screen Name Diversity: %s" % get_lexical_diversity(screen_names)
print "HashTag Diversity: %s" % get_lexical_diversity(hashtags)