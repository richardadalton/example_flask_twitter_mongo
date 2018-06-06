import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from auth import get_api
from auth import get_auth
import json

api = get_api()


class MyStreamListener(StreamListener):

    def __init__(self, limit, tweets):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0 
        self.limit = limit
        self.tweets = tweets

    def on_data(self, data):
        if self.num_tweets < self.limit:
            self.num_tweets += 1
            try:
                self.tweets.append(json.loads(data))
                return True
            except BaseException as e:
                print ("Failed on_data: %s" % str(e))
                
            return True
        else:
            return False

    def on_error(self, status):
        print(status)
        return True


def search_tweets(query, count):
    api = get_api()
    tweets = tweepy.Cursor(api.search, q=query).items(count)
    return [ tweet._json for tweet in tweets]    
    

def stream_tweets(query, count):
    auth = get_auth()
    tweets = []
    twitter_stream = Stream(auth, MyStreamListener(count, tweets))
    twitter_stream.filter(track=[query])
    return tweets