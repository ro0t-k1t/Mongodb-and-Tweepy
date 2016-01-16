__author__ = 'ronanpiercehiggins'

import json
import tweepy
from tweepy import OAuthHandler
import pandas as panda
import matplotlib.pyplot as plt
import re
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
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

tweets_data_path = 'tweet_mining.json'




def read_json(file_path):

    results = []
    tweets_file = open(tweets_data_path, "r")
    for tweet_line in tweets_file:
        try:
            status = json.loads(tweet_line)
            results.append(status)

        except:
            continue

    return results


#print len(results)

def is_token_in_tweet_text(token, tweet_text):
    token = token.lower()

    tweet_text = tweet_text.lower()
    match = re.search(token, tweet_text)
    if match:
        return True
    return False



results = read_json(tweets_data_path)



statuses = panda.DataFrame()
statuses['text'] = map(lambda x: x['text'], results) #map automarically iterates through the list results

statuses['lang'] = map(lambda x: x['lang'], results)

statuses['country'] = map(lambda status: status['place']['country'] if status['place'] != None else None, results)

myBool = True

while myBool:

    var1 = raw_input("Enter first keyword: ")
    var2 = raw_input("Enter second keyword: ")
    var3 = raw_input("Enter third keyword: ")

    statuses[var1] = statuses['text'].apply(lambda status: is_token_in_tweet_text(var1, status))
    statuses[var2] = statuses['text'].apply(lambda status: is_token_in_tweet_text(var2, status))
    #statuses['c#'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('c#', status))
    statuses[var3] = statuses['text'].apply(lambda status: is_token_in_tweet_text(var3, status))


    print statuses[var1]


    """print statuses[var1].value_counts()[False]
    print statuses[var2].value_counts()[False]
    #print statuses['c#'].value_counts()[True]
    print statuses[var3].value_counts()[False]"""

    if statuses[var3].value_counts()[False] < 10 and statuses[var2].value_counts()[False] < 10 and statuses[var1].value_counts()[False] < 10:
            myBool = False



"""tweets_by_lang = statuses['lang'].value_counts()




fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Tweet Languages', fontsize=15)
ax.set_ylabel('Number of tweets', fontsize=15)
ax.xaxis.label.set_color('#666666')
ax.yaxis.label.set_color('#666666')
ax.tick_params(axis='x', colors='#666666')
ax.tick_params(axis='y', colors='#666666')

ax.set_title('Top 10 languages', fontsize=15, color='#666666')

tweets_by_lang[:10].plot(ax=ax, kind='bar', color='#FF7A00')

for spine in ax.spines.values():
    spine.set_edgecolor('#666666')


plt.show()"""

"""print statuses[var1].value_counts()[True]
print statuses[var2].value_counts()[True]
#print statuses['c#'].value_counts()[True]
print statuses[var3].value_counts()[True]"""


slices = [statuses[var1].value_counts()[True], statuses[var2].value_counts()[True], statuses[var3].value_counts()[True]]

#slices = [1,2,3]
activities = [var1, var2, var3]
cols = ['c','m','r']

plt.pie(slices,
        labels = activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0),
        autopct='%1.1f%%')

plt.title('Interesting Graph\nCheck it out')
plt.show()



