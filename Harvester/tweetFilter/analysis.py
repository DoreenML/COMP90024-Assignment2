import json
import couchdb
import datetime
from tqdm import tqdm


def retrieve_couchdb(servers, serverName):
    try:
        database = servers[serverName] if serverName in servers else servers.create(serverName)
    except Exception as e:
        database = servers.create("new_" + serverName)
    return database


couch_url = "http://admin:adminPass@172.26.133.126:5984/"
couch = couchdb.Server(couch_url)

dbName = 'tweet_doc_mark1'
db = couch[dbName]

print("get db view")
dbView = db.view('view/view_id')

# for item in tqdm(dbView):
#     idList.append(item['id'])
#
# for deleteID in tqdm(deleteIDList):
#     del db[item.id]


# delete function
countList = []
saveList = []
index = 0
for item in dbView:
    if item['tweet_id'] not in countList:
        countList.append(item['tweet_id'])
        item["_id"] = str(item['tweet_id'])
        saveList.append(item)
    index += 1
    if index % 10000 == 0:
        print(index, "/", 791641)

newDbName = 'tweet_doc_search_recent_mark1'

dbNew = retrieve_couchdb(couch, newDbName)
print("remain: ", len(countList))
for saveItem in tqdm(saveList):
    saveItem["_id"] = str(saveItem["tweet_id"])
    if str(saveItem["tweet_id"]) not in dbNew:
        dbNew.save(saveItem)

# search function
# couch_url = "http://admin:adminPass@172.26.133.126:5984/"
# couch = couchdb.Server(couch_url)
#
# dbName = 'tweet_covid_australia_mark6'
# db = couch[dbName]
# dbView = db.view('view/view_id')
# print("start view")
# docList = []
# count = 0
# index = 0
# for item in dbView:
#     # datetime.datetime.strptime('Mon Feb 15 2010', '%a %b %d %Y').strftime('%d/%m/%Y')
#     dateFormat = datetime.datetime.strptime(item.value[1][4:10], '%b %d')
#     docList.append(dateFormat)
#     if index % 10000 == 0:
#         print(index, "/", 110000)
#     index += 1
#
#
# docList.sort()
# aL = [[x, docList.count(x)] for x in set(docList)]
# for date, count in aL:
#     print(date.strftime('%m/%d'), "count: ", count)
