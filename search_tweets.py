import tweepy
from auth import get_api

api = get_api()

def search(query, count):
    api = get_api()
    tweets = tweepy.Cursor(api.search, q=query).items(count)
    
    tweets_list = []
    for tweet in tweets:
        tweets_list.append(tweet._json)
    return tweets_list    
