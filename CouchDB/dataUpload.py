import csv
import json
import os
import couchdb
import patoolib
import shutil

from threading import Thread

# set passwd and username and url of couch
adminName = "admin"
adminPasswd = "a13552676625"
url = "127.0.0.1:5984/"
# define couch
couch_url = "http://" + adminName + ":" + adminPasswd + "@" + url
couch = couchdb.Server(couch_url)
# define thread length
threadLength = 32


def read_csv(csvFilePath, sensor_dict_list=[]):
    # Open a csv reader called DictReader
    with open(os.path.join("./", csvFilePath), encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        # Convert each row into a dictionary
        for row in csvReader:
            sensor_dict_list.append(dict(row))
    return sensor_dict_list


def read_json(file_name):
    # load file
    file = open(file_name, 'r', encoding='utf-8-sig')
    data = json.load(file)
    return data


# define path to data
JSON_FILE_CRIME = './dataUpload/crime_data.json'
JSON_FILE_HOUSE = './dataUpload/house_data.json'
JSON_FILE_AGE = './dataUpload/age_data.json'
JSON_FILE_CAMERA_LOCATION = './dataUpload/Pedestrian_Counting_System_-_Sensor_Locations.json'
JSON_FILE_CAMERA_DATA = './dataUpload/Pedestrian_Counting_System_-_Monthly__counts_per_hour_.csv'
JSON_FILE_BUSINESS = './dataUpload/business_data.json'


# define save method
def couch_save_data(saveList, db, rank, length):
    for i, saveItem in enumerate(saveList):
        if i % length == rank:
            db.save(saveItem)


def retrieve_couchdb(servers, serverName):
    try:
        database = servers[serverName] if serverName in servers else servers.create(serverName)
    except Exception as e:
        database = servers.create("new_" + serverName)
    return database


def store_crime_data():
    crime_save_list = []
    table_list = ['Table 01', 'Table 02', 'Table 03', 'Table 04', 'Table 05', 'Table 06']
    crime_data = read_json(JSON_FILE_CRIME)
    for table_idx in range(6):
        lst = crime_data[table_list[table_idx]]
        for item in lst:
            crime_save_list.append(item)
    return crime_save_list


def threadSameMethod(save_list, db):
    threads = [Thread(target=couch_save_data, args=(save_list, db, i, threadLength)) for i in
               range(threadLength)]
    print(db.name + " length is " + str(len(save_list)))
    for threadRun in threads:
        threadRun.start()


# extract data
os.mkdir("dataUpload")
patoolib.extract_archive("./dataUpload.rar", outdir="./dataUpload")
# # save crime data
crime_save_list = store_crime_data()
db = retrieve_couchdb(couch, "crime_data")
threadSameMethod(crime_save_list, db)
#
# save house data
house_save_list = read_json(JSON_FILE_HOUSE)
db = retrieve_couchdb(couch, "house_data")
threadSameMethod(house_save_list, db)

# save age group
age_save_list = read_json(JSON_FILE_AGE)
db = retrieve_couchdb(couch, "age_data")
threadSameMethod(age_save_list, db)

# save camera sensor location data
camera_location_list = read_json(JSON_FILE_CAMERA_LOCATION)
db = retrieve_couchdb(couch, "camera_location_data")
threadSameMethod(camera_location_list, db)

# save camera sensor data
camera_save_list = read_csv(JSON_FILE_CAMERA_DATA)
db = retrieve_couchdb(couch, "camera_data")
threadSameMethod(camera_save_list, db)

# save business_data
business_save_list = read_json(JSON_FILE_BUSINESS)
db = retrieve_couchdb(couch, "business_data")
threadSameMethod(business_save_list, db)
#
shutil.rmtree('./dataUpload')
