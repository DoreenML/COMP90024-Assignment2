import json
import os
import couchdb

couch_url = "http://admin:adminPass@172.26.133.126:5984/"
couch = couchdb.Server(couch_url)

# define the local location of files
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

JSON_FILE = 'Pedestrian_Counting_System_-_Sensor_Locations.json'
DATABASE_NAME = 'sensor_location_data'

def read_json(file_name):
    # load file
    file = open(os.path.join(__location__, file_name), 'r', encoding='utf-8-sig')
    data = json.load(file)
    return data

Lsensor_data = read_json(JSON_FILE)
Total_entry = len(Lsensor_data)
Continue_from = 0 

db = couch[DATABASE_NAME]
for idx in range(Continue_from, Total_entry):
    # print(Lsensor_data[idx])
    db.save(Lsensor_data[idx])
    print("current index:", idx)
    print("Percent remaining:", (1 - idx/Total_entry)*100)
