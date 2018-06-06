import os
from flask import Flask, render_template, request
from search_tweets import search
from pymongo import MongoClient

MONGODB_URI = os.environ.get("MONGODB_URI")
MONGODB_NAME = os.environ.get("MONGODB_NAME")

app = Flask(__name__)

@app.route("/")
def get_index():
    return render_template('index.html')
    
@app.route("/results")
def get_results():
    query = request.args.get('search')
    
    with MongoClient(MONGODB_URI) as conn:
        db = conn[MONGODB_NAME]
        collection = db[query]
        collections_we_have = db.collection_names()

        # Search Twitter    
        if query in collections_we_have:
            #Get it from Mongo
            tweets = collection.find()
        else:
            #Get it from Twitter and save to Mongo
            tweets = search(query, 10)
            collection.insert_many(tweets)
    
    return render_template('results.html', tweets=tweets)


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)
