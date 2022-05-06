import json
import os
import couchdb

couch_url = "http://admin:adminPass@172.26.133.126:5984/"
couch = couchdb.Server(couch_url)

# define the local location of files
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

JSON_FILE = 'age_data.json'
DATABASE_NAME = 'age_data'

def read_json(file_name):
    # load file
    file = open(os.path.join(__location__, file_name), 'r', encoding='utf-8-sig')
    data = json.load(file)
    return data

business_data = read_json(JSON_FILE)

db = couch[DATABASE_NAME]
for item in business_data:
    db.save(item)
print("Age data upload finished")