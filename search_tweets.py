import tweepy
from auth import get_api

api = get_api()

def search(query, count):
    api = get_api()
    tweets = tweepy.Cursor(api.search, q=query).items(count)
    return [ tweet._json for tweet in tweets]    