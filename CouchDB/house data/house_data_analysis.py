import json
import os
import couchdb

couch_url = "http://admin:adminPass@172.26.133.126:5984/"
couch = couchdb.Server(couch_url)

# define the local location of files
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

JSON_FILE = 'house_data.json'
DATABASE_NAME = 'house_data'

def read_json(file_name):
    # load file
    file = open(os.path.join(__location__, file_name), 'r', encoding='utf-8-sig')
    data = json.load(file)
    return data

house_data = read_json(JSON_FILE)
print(len(house_data))

db = couch[DATABASE_NAME]
Total_entry = 249251
Continue_from = 245356
for idx in range(Continue_from, Total_entry):
    db.save(house_data[idx])
    print("current index:", idx)
    print("Percent remaining:", (1 - idx/Total_entry)*100)

    