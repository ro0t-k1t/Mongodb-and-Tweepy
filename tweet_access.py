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

count = 10
query = 'Fallout'

results = [x for x in tweepy.Cursor(api.search, q=query).items(count)]

#for result in results:
 #   print json.dumps(result._json, indent=2)

for status in results:
    if status.place == None:
        print status.text.encode('utf-8')
        print status.user.id
        print status.user.screen_name
        #print status.user.profile_image_url_https
        print status.user.followers_count
        print status.place


"""status_texts = [ status._json['text'] for status in results]

screen_names = [ status._json["user"]['screen_name']
                 for status in results
                        for mention in
status._json['entities']['user_mentions']]

hashtags = [ hashtag['text']
                            for status in results
                                    for hashtag in
status._json['entities']['hashtags'] ]

words = [ word
                for text in status_texts
                        for word in text.split()]

print json.dumps(status_texts[0:5], indent=1)
print json.dumps(screen_names[0:5], indent=1)
print json.dumps(hashtags[0:5], indent=1)
print json.dumps(words[0:5], indent=1)"""
