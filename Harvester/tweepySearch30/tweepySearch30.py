# tweet_list =api_s[-1].search(geocode="-37.999250,144.997395,57km", count=100)
import time

import tweepy
import json
import couchdb
import ast
from mpi4py import MPI
from datetime import datetime

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
databaseName = "tweet_doc_melbourne_coordinator_30_mark8"

print("got servers")
servers = couchdb.Server(returnURL())

print("create database, store ", databaseName)
database = retrieve_couchdb(servers, databaseName)

DateList = [202204070000, 202204120000, 202204170000, 202204220000, 202204270000, 202205010000, 202205060000]
DateTuple = [(DateList[i - 1], DateList[i]) for i in range(1, len(DateList))]

parHashtag = "has:hashtags "
parLang = "lang:en"

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# 2 3 4
api = getClient(APIFullList[rank])
label = APIFullList[rank]['label']
fromDate, toData = DateTuple[rank]
for i in range(1, 190):
    # define parameter of tweepy_full_archive
    l, a, r = locationDict[i]
    location = "point_radius: [" + str(l) + " " + str(a) + " " + str(r * 90) + "km] "
    startTime = datetime.now().second
    tweetsGet = tweepy.Cursor(api.search_30_day,
                              query=location + parLang,
                              label=label,
                              fromDate=fromDate,
                              toDate=toData).items(100)
    # save data:
    count = 0
    for tweetGet in tweetsGet:
        tweetJson = tweetGet._json
        tweetJson["_id"] = str(tweetJson["id"])
        tweetJson["suburbID"] = i
        if tweetJson["_id"] not in database:
            database.save(tweetJson)
        count += 1
    endTime = datetime.now().second
    workTime = endTime - startTime
    if workTime < 2:
        time.sleep(2.05 - workTime)
    print("count: ", count, " index: ", i)
