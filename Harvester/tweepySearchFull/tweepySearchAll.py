# tweet_list =api_s[-1].search(geocode="-37.999250,144.997395,57km", count=100)

import tweepy
import json
import couchdb
import ast

# Initial api par list
# Initial suburb par list
from Harvester.couchdbURL import returnURL

APIFullList = []
locationDict = None


def getClient(tweetAPI):
    authentication = tweepy.OAuthHandler(tweetAPI['consumer_key'], tweetAPI['consumer_secret'])
    return tweepy.API(authentication, wait_on_rate_limit=True)


def retrieve_couchdb(servers, serverName):
    try:
        database = servers[serverName] if serverName in servers else servers.create(serverName)
    except Exception as e:
        database = servers.create("new_" + serverName)
    return database


# get API par
with open('tweetAPI.json', 'r') as f:
    tweetAPIList = json.load(f)
    for tweetAPI in tweetAPIList:
        APIFullList.append(tweetAPI)

with open('center and radius.txt', 'r') as f:
    locationStr = f.read()
    locationDict = ast.literal_eval(locationStr)

# get geo par

# use instance 1 as cloud master
databaseName = "tweet_doc_melbourne_coordinator_mark7"

print("got servers")
servers = couchdb.Server(returnURL())

print("create database, store ", databaseName)
database = retrieve_couchdb(servers, databaseName)


fromDate = 201701010000
toData5 = 202205060000

# toDate = 202205060000

parHashtag = "has:hashtags "
parLang = "lang:en"
api = getClient(APIFullList[5])
label = APIFullList[5]['label']

i = 172
print(i)
# define parameter of tweepy_full_archive
l, a, r = locationDict[i]
location = "point_radius: [" + str(l) + " " + str(a) + " " + str(r*90) + "km] "
print(location)
tweetsGet = tweepy.Cursor(api.search_full_archive,
                          query=location + parLang,
                          label=label,
                          fromDate=fromDate,
                          toDate=toData5).items(100)
# save data:
count = 0
for tweetGet in tweetsGet:
    tweetJson = tweetGet._json
    tweetJson["suburbID"] = i
    database.save(tweetJson)
    count += 1
print("count: ", count, " index: ", i)
