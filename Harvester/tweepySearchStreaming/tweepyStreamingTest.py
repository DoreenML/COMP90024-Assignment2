import json
from time import sleep

import couchdb
from tweepy import Stream

import tweepy

def retrieve_couchdb(servers, serverName):
    try:
        database = servers[serverName] if serverName in servers else servers.create(serverName)
    except Exception as e:
        database = servers.create("new_" + serverName)
    return database


# set instance 1 as cloud master
print("got servers")
servers = couchdb.Server('http://admin:adminPass@172.26.133.126:5984/')
print("create database")
database = retrieve_couchdb(servers, 'tweet_doc_stream_stable_mark5')
print("retrieve data")


class MyStreamListener(Stream):
    city = None

    def defineCity(self, cityName):
        self.city = cityName

    def on_status(self, status):
        print(status.text)
        print(self.city)
        twitter_json = status._json
        twitter_json['city'] = self.city
        twitter_json['_id'] = str(twitter_json['id'])
        if str(twitter_json['id']) not in database:
            try:
                database.save(twitter_json)
            except:
                pass

    def on_error(self, status_code):
        print(status_code)
        # if status_code == 420:  # end of monthly limit rate (500k)
        #     return False


bbox = {
    "great_syd": [149.971885992, -34.33117400499998, 151.63054702400007, -32.99606922499993],
    "great_mel": [144.33363404800002, -38.50298801599996, 145.8784120140001, -37.17509899299995],
    "great_brisbane": [152.07339276400012, -28.363962911999977, 153.54670756200005, -26.452339004999942],
    "great_ald": [138.435645001, -35.350296029999974, 139.04403010400003, -34.50022530299998]
}

streamList = []

with open('tweetAPI.json', 'r') as f:
    tweetAPIList = json.load(f)
    for tweetAPI in tweetAPIList:
        streamList.append(
            MyStreamListener(tweetAPI['consumer_key'],
                             tweetAPI['consumer_secret'],
                             tweetAPI['access_token_key'],
                             tweetAPI['access_token_secret']))
print("load json done")
dList = []
count = 0
for city, box in bbox.items():
    stream = streamList[count]
    stream.defineCity(city)
    try:
        thread = stream.filter(locations=list(bbox.values())[count], threaded=True)
        dList.append(thread)
        print("run parallel stream on city ", count)
        count += 1
    except tweepy.TweepError as e:
        print("try again")
        sleep(10)
        thread = stream.filter(locations=list(bbox.values())[count], threaded=True)

count = 0
while True:
    # check if is alive
    if not dList[count].is_alive():
        print("try reboot")
        dList[count] = stream.filter(locations=list(bbox.values())[count], threaded=True)
    sleep(2)
    count += 1
    if count == len(dList):
        count = 0
