![mongo logo](https://github.com/richardadalton/example_flask_twitter_mongo/blob/master/resources/mongo-logo.jpg?raw=true)

# Flask/Twitter/Mongo Example

## Background
This project allows the user to search twitter for existing tweets, or capture new tweets as they happen. 
The results are stored in Mongo, subsequent queries for the same keyword pull from mongo. 

The site is build using the python flask framework.

## Installation
1. git clone this repo.

2. sudo pip3 install -r requirements.txt

3. Create a mongo database, e.g. on mlab.com

4. Create environment variables for twitter credentials and mongo uri.

* CONSUMER_KEY
* CONSUMER_SECRET
* OAUTH_TOKEN
* OAUTH_TOKEN_SECRET
* MONGO_URI

