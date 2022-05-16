import tweepy
import json
import couchdb
import tweepySearchRecentUtil
from Harvester.couchdbURL import returnURL

clients = []

# Create tweepy crawler, from api json file
with open('tweetAPI.json', 'r') as f:
    tweetAPIList = json.load(f)
    for tweetAPI in tweetAPIList:
        clients.append(tweepySearchRecentUtil.getClient(tweetAPI))
print(len(clients))

# set instance 1 as cloud master
print("got servers")
servers = couchdb.Server(returnURL())
print("create database")
database = tweepySearchRecentUtil.retrieve_couchdb(servers, 'tweet_doc_search_recent_stable_mark4')
print("retrieve data")

# search all tag one time
tweepySearchRecentUtil.crawlTweets(clients, database)
