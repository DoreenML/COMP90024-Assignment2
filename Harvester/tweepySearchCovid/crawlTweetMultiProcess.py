import csv
from datetime import datetime
import time
import os

import couchdb
import tweepy

# multi process
from mpi4py import MPI



def retrieve_couchdb(servers, serverName):
    try:
        database = servers[serverName] if serverName in servers else servers.create(serverName)
    except Exception as e:
        database = servers.create("new_" + serverName)
    return database


def deleteAttribute(dictGiven):
    dictNew = {}
    dictNew['_id'] = dictGiven['_id']
    dictNew['in_melbourne'] = dictGiven['in_melbourne']
    dictNew['in_reply_to_status_id_str'] = dictGiven['in_reply_to_status_id_str']
    dictNew['in_reply_to_user_id_str'] = dictGiven['in_reply_to_user_id_str']
    dictNew['text'] = dictGiven['text']
    dictNew['created_at'] = dictGiven['created_at']
    dictNew['user_id'] = dictGiven['user']["id"]
    dictNew['user_location'] = dictGiven['user']["location"]
    dictNew['geo'] = dictGiven["geo"]
    dictNew['coordinates'] = dictGiven['coordinates']
    dictNew['place'] = dictGiven['place']
    dictNew['retweet_count'] = dictGiven['retweet_count']
    dictNew['favorite_count'] = dictGiven['favorite_count']
    dictNew['lang'] = dictGiven['lang']
    return dictNew


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
     {"consumer_key": "vBiXbWeFeOPf7BPEuPKXSkB9r",
      "consumer_secret": "8yPcjeHvQlV1PXjd12XQyVZoEI6gT4VWOGr1Qi74wpCT73BE0o",
      "access_token_key": "1512683317820239876-pV82VUFemuKDCiWy6UHJq2vRIpgZa2",
      "access_token_secret": "5D8PYXkSNXIMRVslpyAQSkJpWOFXGnnXiHiljzodbtXFw",
      "bearer_token": "AAAAAAAAAAAAAAAAAAAAAKsMcAEAAAAAjJKmPixhdJBwv0k0gsJrtJddEww%3DibfJ3mdNeF3jsbQZTaKeln0pvH3VeoqkwsPD9MLUSyLcroNAl6"},
     {"consumer_key": "ag2JLYS9hxeqZE5KOtexoCdPH",
      "consumer_secret": "6cJ3CyGKusGQeyOIOXDPyKg0l8Q8fVaaV0dpQIkrwrhSPdKH9C",
      "access_token_key": "1455506331612315654-udqG1YU3fEEqhEYkC4BwSHxQFQQ6mH",
      "access_token_secret": "c2DW47O8gKjPecRBnqpwSfyZalQsm3cXBafyLFh90Fhcy",
      "bearer_token": "AAAAAAAAAAAAAAAAAAAAAIgUcAEAAAAAuoiP07RH1N3KB8rleIQafMA3wLQ%3Dza5H34XVFUEv1mzVIELoqwCjLVsUgIax5wz2cZY6mA29XIExau"},
     {"consumer_key": "97NZMdQiYkDd6obbuMWWa9xdn",
      "consumer_secret": "jrKgbE7JHqo7bVGZUUbqgIoYtRvOsMg2fmJCJYnZsyPakMgGl8",
      "access_token_key": "1519879315579895808-cMiBiMVmtlUISfuRroDsjZpHa8pWXn",
      "access_token_secret": "fWtilQislbFHVWD8doi1YqZIPkmHpW1KXg6HMnnCUOATu",
      "bearer_token": "AAAAAAAAAAAAAAAAAAAAAFIOcAEAAAAAd7pqY5AN04VUGhNUkuPmOCOGwGk%3DXdypxk16XugMPesVJCrkxLAHaEkGBb14Vzc99NIICfxHyn5fp3"},
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

     ]

def crawlTSVProcess(given_tsv, api, rank, apiLength):
    retrieveList = []
    countRequestNum = 0
    for i, row in enumerate(given_tsv):
        if i % apiLength != rank or i == 0:
            continue
        if i == 0 or row[3] != 'en':
            continue
        if len(retrieveList) < 100:
            # jump duplicate
            if str(row[0]) not in database:
                retrieveList.append(row[0])
        else:
            tweetResponses = api.lookup_statuses(retrieveList)
            # set empty
            retrieveList = []
            # save data
            for tweetResponse in tweetResponses:
                saveJson = tweetResponse._json
                if 'Australia' in saveJson['user']['location'] or 'AU' in saveJson['user'][
                    'location'] or 'Melbourne' in \
                        saveJson['user']['location'] or 'Victoria' in saveJson['user']['location']:
                    if 'Melbourne' in saveJson['user']['location']:
                        saveJson['in_melbourne'] = True
                    else:
                        saveJson['in_melbourne'] = False
                    saveJson['_id'] = saveJson['id_str']
                    database.save(deleteAttribute(saveJson))
            countRequestNum += 1
            if countRequestNum % 25 == 0:
                print("rank:", rank, ", i:", i)
                limits = api.rate_limit_status()
                timesRemain = limits['resources']['statuses']['/statuses/lookup']['remaining']
                if timesRemain <= 50:
                    userTimeLine = limits['resources']['statuses']['/statuses/lookup']['reset']
                    userTime = time.localtime(userTimeLine)
                    currentTime = time.localtime()
                    sleepTime = time.mktime(userTime) - time.mktime(currentTime)
                    print("rank sleep for: ", sleepTime, "seconds")
                    time.sleep(sleepTime)


print("got servers")
servers = couchdb.Server('http://admin:adminPass@172.26.133.126:5984/')
print("create database")
database = retrieve_couchdb(servers, 'tweet_covid_australia_mark6')
print("retrieve data")

startTime = datetime.now().second
# renew the start position
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

for filename in os.listdir('covidTweetID/covidData')[::-1][100:]:  # . is cwd
    print(filename)
    tsv_file = open("covidTweetID/covidData/" + filename)
    read_tsv = csv.reader(tsv_file, delimiter="\t")
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
    # run process
    crawlTSVProcess(read_tsv, api, rank, size)
