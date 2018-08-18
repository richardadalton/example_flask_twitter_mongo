![flask logo](https://github.com/richardadalton/example-flask-twitter-mongo/blob/master/resources/flask-logo.png?raw=true)
![twitter logo](https://github.com/richardadalton/example-flask-twitter-mongo/blob/master/resources/twitter-logo.jpg?raw=true)
![mongo logo](https://github.com/richardadalton/example-flask-twitter-mongo/blob/master/resources/mongo-logo.jpg?raw=true)

# Flask/Twitter/Mongo Example

## Background
This project allows the user to search twitter for existing tweets, or capture new tweets as they happen. 
The results are stored in Mongo, subsequent queries for the same keyword pull from mongo. 

The site is build using the python flask framework.

## Installation

### git clone this repo.

### sudo pip3 install -r requirements.txt

### Create a mongo database, e.g. on mlab.com

### Create environment variables for twitter credentials and mongo uri.

* CONSUMER_KEY
* CONSUMER_SECRET
* OAUTH_TOKEN
* OAUTH_TOKEN_SECRET
* MONGO_URI

