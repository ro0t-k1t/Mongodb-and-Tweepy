__author__ = 'ronanpiercehiggins'

import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter
import sys
import time


CONSUMER_KEY = 'uQIDLDayiNYrUoFiQaS8JkuOU'
CONSUMER_SECRET = 'kwYqW2fIceEovFyklPtuviMckincqtRwxqsJxiN7nhHq0mly35'
OAUTH_TOKEN = '2879848607-W9p7IneZ3uo37B8RYmESZhdTpDEZLAk1thEjaoV'
OAUTH_TOKEN_SECRET = 'rVpexhPWZU7gR7VbkSIMiew3qFhXZfdOCUzEYSDMIdJrD'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

#user = api.get_user('@madonna')

"""print(user.screen_name)
print(user.followers_count)

for friend in user.friends():
    print
    print(friend.screen_name)
    print(friend.followers_count)"""


"""count = 1

for x in range(10):
    api.update_status(status=count)
    count += 1
    time.sleep(1)"""


for t in tweepy.Cursor(api.user_timeline).items():
        api.destroy_status(t.id)











