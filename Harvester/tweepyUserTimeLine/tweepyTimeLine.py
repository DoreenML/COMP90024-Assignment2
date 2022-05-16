import json
from datetime import datetime
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import time
import couchdb
import tweepy

from mpi4py import MPI

from Harvester.couchdbURL import returnURL

JSON_FILE = 'phidu_admissions_preventable_diagnosis_vaccine_pha_2016_17-6982188917692169592.json'
def retrieve_couchdb(servers, serverName):
    try:
        database = servers[serverName] if serverName in servers else servers.create(serverName)
    except Exception as e:
        database = servers.create("new_" + serverName)
    return database

def form_area_dict():
    area_dict = {}
    data = read_json(JSON_FILE)
    for idx in range(276):
        area_dict[idx] = data["features"][idx]["geometry"]["coordinates"][0][0]
    return area_dict

def read_json(file_name):
    # load file
    file = open("./" + file_name, 'r', encoding='utf-8-sig')
    data = json.load(file)
    return data

def form_area_dict():
    area_dict = {}
    data = read_json(JSON_FILE)
    for idx in range(276):
        area_dict[idx] = data["features"][idx]["geometry"]["coordinates"][0][0]
    return area_dict

area_dict = form_area_dict()
def find_area(cor_list):
    point = Point(cor_list)
    for idx in range(276):
        polygon = Polygon(area_dict[idx])
        if (polygon.contains(point)):
            return idx + 1
    return -1

def readAuthorHave(fileName):
    authorList = []
    last = None
    with open(fileName, 'r', encoding='utf-8') as f:
        for line in f:
            # lineClean = str(line.replace('\n', ''))
            # dictTweet = ast.literal_eval(lineClean)
            pos = line.find("'user_id': ") + 12
            count = 0
            for i in range(200):
                if line[pos + i] == "'":
                    break
                count += 1
            user_id = line[pos: pos+count]
            if last != user_id:
                authorList.append(user_id)
                last = user_id
    return authorList

# for i in range(8):
#     userHavenDict[i] = readAuthorHave('tweet_melbourne' + str(i) + '.json')
#     print("done: ", i)
f = open('authorListHaven.json', 'r')
authorHave = json.load(f)

apiList = []
apiDict = \
    [{"consumer_key": "XFEcxTOgeBOqrm93oi8HaGOV0",
      "consumer_secret": "nuWBsAq35YwFQD3M0XhGaHQmazb0l97aTxYdPUb99fFWhdn9xv",
      "access_token_key": "1513721883568787456-PfsFmjlJabzIZzZ0I48oEEOrT2toDb",
      "access_token_secret": "1qfH3VCR9egkvQXtUvKs1qnu2a3ubRuvvvTS93nCJCmNI",
      "bearer_token": "AAAAAAAAAAAAAAAAAAAAACr1bwEAAAAA%2BLXtPE4xYA%2FkLERzJdvu%2BQ5SghY%3DtRw00y62xzJj6ktJGmsNcCvvbJBvdRp0Ln3v8cqHPAv8SGLGtL"},
     {"consumer_key": "PBWjRTxSaanQoI33STur380CS",
      "consumer_secret": "POPUnpMbOTs0m721mnfTQRUMZ14rXqcUaPcMIQjjhch6wAqz6l",
      "access_token_key": "1514215434110734336-RoXlXdIxUqCOpilAMXiIBxVAqwiBpT",
      "access_token_secret": "kDNYIteibDvq1u2oeXwBkL4jeBf9E8Kqxxb8YUtVDlfMk",
      "bearer_token": "AAAAAAAAAAAAAAAAAAAAAFbrbwEAAAAAC1wy50bsb8qQYA9nK37G1xh9LVE%3DJ6G6CclRKUSp7CFH1nLiRS7Ola3Xg9nxZiH4MlHDAIhEOIrKFm"},
     {"consumer_key": "B5d80GNgf0htlN6BQM6GyYATf",
      "consumer_secret": "qgpxFGhb6oRcT7DxJtXSGT7FCQrlpiapIirm0j4wjesRNbsoA6",
      "access_token_key": "1081497692281417729-7ImilqK4akdwyGVTsniKNMoPGI7PuC",
      "access_token_secret": "Iws2mN2cirOCLB6oNCQ7xc6rwjUUSvqLudI1uVN1Omtlv",
      "bearer_token": "AAAAAAAAAAAAAAAAAAAAANP1bwEAAAAAT5eE2A91XgW71d7szYKYaLMqvHo%3DZ2S2Y9p2fOKxBOn9IfhzfHXIdIYufgSXBhH6xpQAI7NYcAvMZF"},
     {"label": "tweetGetAllMark1", "consumer_key": "wiJQ6KzS8Kv2A186DcEX7eWZb",
      "consumer_secret": "xIwnQfIEdVR3Nn3woYEgBVHxj4ZIRLs4nBn1vcJUoYL7AGfOsO",
      "access_token_key": "1455506331612315654-yWwOg9menAVBY6CKeSO91jNtVh4HTe",
      "access_token_secret": "FOpRd5h2wROZgKE47KrteR2ktqQ4mfaImecHjaYNfHJzF",
      "bearer_token": "AAAAAAAAAAAAAAAAAAAAAGVUcAEAAAAAAs7KWklx3Yv%2B6oMp8XP1N9putbY%3DIUnEuPAU6bqLjT7U0xXfznhxio5BS9EQjv5X2JUx328a110Euu"},
     {"consumer_key": "ag2JLYS9hxeqZE5KOtexoCdPH",
      "consumer_secret": "6cJ3CyGKusGQeyOIOXDPyKg0l8Q8fVaaV0dpQIkrwrhSPdKH9C",
      "access_token_key": "1455506331612315654-udqG1YU3fEEqhEYkC4BwSHxQFQQ6mH",
      "access_token_secret": "c2DW47O8gKjPecRBnqpwSfyZalQsm3cXBafyLFh90Fhcy",
      "bearer_token": "AAAAAAAAAAAAAAAAAAAAAIgUcAEAAAAAuoiP07RH1N3KB8rleIQafMA3wLQ%3Dza5H34XVFUEv1mzVIELoqwCjLVsUgIax5wz2cZY6mA29XIExau"},
     {"label": "tweetGetAllMark5", "consumer_key": "WVcn9qytTT4v4TyuhzbYwHTBg",
      "consumer_secret": "cN4NrQNhbRmqjqm0HmWNVrcbQl3A8BWoRNr22ZSHrOTAbuYn1n",
      "access_token_key": "1455506331612315654-CMRrTI65EsutES1M9uiEmYs2vQyWdG",
      "access_token_secret": "C2Xta9GDRxkAA0IrqZhehur8ydwrKdEWVqAXcebFIM2ca",
      "bearer_token": "AAAAAAAAAAAAAAAAAAAAALUUcAEAAAAAbQos%2FK9KHpYAC%2FJ6WZpVuAO58pE%3Dya4hQuW1vqbg6ryKSQAvqRjktS9xZv2xl4QhCTwVL4J3p9vXqf"},
     {"consumer_key": "CUAGDKipxKb5wKKr2WPPEOp0m",
      "consumer_secret": "Cls2eFnOsY5HuqUCdXONgK04cLW1e5pq7cffIK5lg7tI3w6HF7",
      "access_token_key": "1519804086337499136-Pqd3A4PgoQqwYVd6EiagDvsJRV0Uv0",
      "access_token_secret": "JYm51jkLcn14I3RGOBRm3O71aQFSQixQM22fKZBddg67s",
      "bearer_token": "AAAAAAAAAAAAAAAAAAAAALEOcAEAAAAAkIWSxwXYGbcU8fSaqzsxN3BNqK4%3DcvJKEe1CX9fPKLb3qwEXKR2UTq6uL1ggg8MGeQVyi6PUzR6ecw"},
     {"consumer_key": "WVcn9qytTT4v4TyuhzbYwHTBg",
      "consumer_secret": "cN4NrQNhbRmqjqm0HmWNVrcbQl3A8BWoRNr22ZSHrOTAbuYn1n",
      "access_token_key": "1455506331612315654-CMRrTI65EsutES1M9uiEmYs2vQyWdG",
      "access_token_secret": "C2Xta9GDRxkAA0IrqZhehur8ydwrKdEWVqAXcebFIM2ca",
      "bearer_token": "AAAAAAAAAAAAAAAAAAAAALUUcAEAAAAAbQos%2FK9KHpYAC%2FJ6WZpVuAO58pE%3Dya4hQuW1vqbg6ryKSQAvqRjktS9xZv2xl4QhCTwVL4J3p9vXqf"},
     {"consumer_key": "e5nnzCo6OSJyGzDz6tbQqdT7o",
      "consumer_secret": "Sxdx1jwJUSx0TVgdMrH4c59OKCPSttbl2hWrkWI1VfNI9XqJGX",
      "access_token_key": "1520628831605772288-bNRQ3xUnx2XW7zNOBHNLbkNfkOCZ1O",
      "access_token_secret": "qxITm5KT2gr4F3Uc1HsDjyeyOzdgd6iYqC6sHMRUZ4u5q",
      "bearer_token": "AAAAAAAAAAAAAAAAAAAAABRZcAEAAAAAx%2B08sRUg9YPBdr%2F5aZ6sa8btJ5s%3DsScZ6x6ej3D3UESmz0sdQTM6sEFixDDFi4Z6a7E158uVn8obe1"},
     {"consumer_key": "wiJQ6KzS8Kv2A186DcEX7eWZb",
      "consumer_secret": "xIwnQfIEdVR3Nn3woYEgBVHxj4ZIRLs4nBn1vcJUoYL7AGfOsO",
      "access_token_key": "1455506331612315654-yWwOg9menAVBY6CKeSO91jNtVh4HTe",
      "access_token_secret": "FOpRd5h2wROZgKE47KrteR2ktqQ4mfaImecHjaYNfHJzF",
      "bearer_token": "AAAAAAAAAAAAAAAAAAAAAGVUcAEAAAAAAs7KWklx3Yv%2B6oMp8XP1N9putbY%3DIUnEuPAU6bqLjT7U0xXfznhxio5BS9EQjv5X2JUx328a110Euu"},
     {"consumer_key": "CUAGDKipxKb5wKKr2WPPEOp0m",
      "consumer_secret": "Cls2eFnOsY5HuqUCdXONgK04cLW1e5pq7cffIK5lg7tI3w6HF7",
      "access_token_key": "1519804086337499136-Pqd3A4PgoQqwYVd6EiagDvsJRV0Uv0",
      "access_token_secret": "JYm51jkLcn14I3RGOBRm3O71aQFSQixQM22fKZBddg67s",
      "bearer_token": "AAAAAAAAAAAAAAAAAAAAALEOcAEAAAAAkIWSxwXYGbcU8fSaqzsxN3BNqK4%3DcvJKEe1CX9fPKLb3qwEXKR2UTq6uL1ggg8MGeQVyi6PUzR6ecw"}

     ]

apiDictBackEnd = [{"consumer_key": "CUAGDKipxKb5wKKr2WPPEOp0m",
                   "consumer_secret": "Cls2eFnOsY5HuqUCdXONgK04cLW1e5pq7cffIK5lg7tI3w6HF7",
                   "access_token_key": "1519804086337499136-Pqd3A4PgoQqwYVd6EiagDvsJRV0Uv0",
                   "access_token_secret": "JYm51jkLcn14I3RGOBRm3O71aQFSQixQM22fKZBddg67s",
                   "bearer_token": "AAAAAAAAAAAAAAAAAAAAALEOcAEAAAAAkIWSxwXYGbcU8fSaqzsxN3BNqK4%3DcvJKEe1CX9fPKLb3qwEXKR2UTq6uL1ggg8MGeQVyi6PUzR6ecw"}]

print("got servers")
servers = couchdb.Server(returnURL())
print("create database")
database = retrieve_couchdb(servers, 'tweet_users_time_line_mark9')
tweetUserList = json.loads(open("./authorListAdd.json").read())
print("load tweet users: ", len(tweetUserList))

print("retrieve data")

startTime = datetime.now().second
# renew the start position
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# set tweet key and secret
apiAccess = apiDict[rank]
consumer_key = apiAccess['consumer_key']
consumer_key_secret = apiAccess['consumer_secret']
access_token = apiAccess['access_token_key']
access_token_secret = apiAccess['access_token_secret']
bearer_token = apiAccess['bearer_token']
authentication = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

limits = api.rate_limit_status()
print(limits['resources']['statuses']['/statuses/user_timeline']['remaining'],
      limits['resources']['statuses']['/statuses/lookup']['reset'])

for i, tweetUser in enumerate(tweetUserList):
    # jump to own
    if i % size != rank or str(tweetUser["_id"]) in authorHave[str(rank)]:
        continue
    try:
        for pages in tweepy.Cursor(api.user_timeline, user_id=tweetUser["_id"], count=2500).pages():
                for tweetResponse in pages:
                    tweetItem = tweetResponse._json
                    saveTweetItem = {}
                    saveTweetItem["_id"] = tweetItem["id_str"]
                    saveTweetItem["user_id"] = tweetItem["user"]["id_str"]
                    saveTweetItem["user_place"] = tweetUser["place"]
                    saveTweetItem["created_at"] = tweetItem["created_at"]
                    saveTweetItem["text"] = tweetItem["text"]
                    # save user history
                    saveTweetItem["coordinates_history"] = tweetItem["coordinates"]
                    saveTweetItem["place_history"] = tweetItem["place"]
                    # save to local json
                    saveTweetItem["retweet_count"] = tweetItem["retweet_count"]
                    saveTweetItem["favorite_count"] = tweetItem["favorite_count"]
                    saveTweetItem["retweet_count"] = tweetItem["retweet_count"]
                    saveTweetItem["retweet_count"] = tweetItem["retweet_count"]
                    # read hash tag
                    saveTweetItem['hashtags'] = []
                    # read coordinates
                    saveTweetItem['coordinates'] = tweetItem["coordinates"]
                    for hashtag in tweetItem['entities']['hashtags']:
                        saveTweetItem['hashtags'].append(hashtag['text'])
                    try:
                        database.save(saveTweetItem)
                    except:
                        pass
    except:
        # jump user when error occur
        print("error occur, break out in user, " + str(i))
        pass
    timesRemain = limits['resources']['statuses']['/statuses/user_timeline']['remaining']
    if timesRemain <= 50:
        limits = api.rate_limit_status()
        resetTimeLine = limits['resources']['statuses']['/statuses/user_timeline']['reset']
        resetTime = time.localtime(resetTimeLine)
        currentTime = time.localtime()
        sleepTime = time.mktime(resetTime) - time.mktime(currentTime)
        print("rank sleep for: ", sleepTime, "seconds")
        time.sleep(sleepTime)
    print("read" + str(i) + "user")
