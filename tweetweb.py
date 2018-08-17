import os
from flask import Flask, render_template, request
from search_tweets import search_tweets, stream_tweets
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route("/")
def get_index():
    return render_template('index.html')
    
@app.route("/results")
def get_results():
    query = request.args.get('search')
    count = int(request.args.get('how_many'))
    tweet_type = request.args.get('tweet_type')

    if query in mongo.db.collection_names():
        tweets = mongo.db[query].find()
    else:
        if tweet_type == 'stream':
            tweets = stream_tweets(query, count)
        else:
            tweets = search_tweets(query, count)
            mongo.db[query].insert_many(tweets)

    return render_template('results.html', tweets=tweets)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)