# Import the libraries
import numpy as np
import tweepy
import json
import pandas as pd
from tweepy import OAuthHandler
from textblob import TextBlob

# credentials
consumer_key = "NKplhMO19jOi5KwnR3QlUJnUx"
consumer_secret = "MEQx2FmsOjbaxxm0CeE9u9OHNqQ0xIqFul30tIfkFHRCF7oy6j"
access_token = "156224585-C6LFHPJjxlVNu5QXfTnTwW2Z7Ka7ZoqDSi8ly5JV"
access_token_secret = "mQXX1pVixM3GfRYI3YVXH7f9669SUnTtaJMcyHIR2MWmE"
# calling API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# Provide the query you want to pull the data. For example,
# pulling data for the mobile phone ABC
query ="new zealand"
# Fetching tweets
Tweets = api.search(query, count = 100,lang='en', exclude='retweets',tweet_mode='extended')

text = []
p = []
s = []
for tweet in Tweets:
    analysis = TextBlob(tweet.full_text)
    text.append(tweet.full_text)
    p.append(analysis.sentiment[0])
    s.append(analysis.sentiment[1])
result = pd.DataFrame({'Tweet Text' : text, 'polarity' : p , 'subjectvity' : s})   
print(result)
