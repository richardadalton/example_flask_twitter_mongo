import tweepy
from auth import get_api

api = get_api()

def search(query, count):
    return [status for status in tweepy.Cursor(api.search, q=query).items(count)]
    
tweets = search("#Friday", 15)

for tweet in tweets:
    print(tweet.text)
