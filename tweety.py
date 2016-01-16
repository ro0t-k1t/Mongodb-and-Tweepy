__author__ = 'ronanpiercehiggins'

import json
import tweepy

from tweepy import OAuthHandler

CONSUMER_KEY = 'uQIDLDayiNYrUoFiQaS8JkuOU'
CONSUMER_SECRET = 'kwYqW2fIceEovFyklPtuviMckincqtRwxqsJxiN7nhHq0mly35'
OAUTH_TOKEN = '2879848607-W9p7IneZ3uo37B8RYmESZhdTpDEZLAk1thEjaoV'
OAUTH_TOKEN_SECRET = 'rVpexhPWZU7gR7VbkSIMiew3qFhXZfdOCUzEYSDMIdJrD'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 23424803

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

#dub_trends_set = set([trend['name'] for trend in dub_trends[0]['trends']])
lon_trends_set = set([trend['name'] for trend in lon_trends[0]['trends']])

def myFunc():
    for trend in dub_trends[0]['trends']:
        return set(trend['name'])

dub_trends_set = myFunc()



common_trends = set.union(dub_trends_set,lon_trends_set)


print common_trends

#print json.dumps(lon_trends, indent=1)
