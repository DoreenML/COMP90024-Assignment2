import csv
import json
import os
import couchdb
from BackEnd.util import find_area, read_json, createView
from threading import Thread

# set passwd and username and url of couch
adminName = "admin"
adminPasswd = "adminPass"
url = "172.26.130.135:5984/"
# define couch
couch_url = "http://" + adminName + ":" + adminPasswd + "@" + url
couch = couchdb.Server(couch_url)
# define thread length
threadLength = 512


# define camera location for retrieve
camera_location_list = []
camera_ID_list = []

def read_csv(csvFilePath, sensor_dict_list=[]):
    # Open a csv reader called DictReader
    with open(os.path.join("./", csvFilePath), encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        # Convert each row into a dictionary
        for row in csvReader:
            sensor_dict_list.append(dict(row))
    return sensor_dict_list


def read_csv_camera_filter(csvFilePath, sensor_dict_list=[]):
    # Open a csv reader called DictReader
    with open(os.path.join("./", csvFilePath), encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        # Convert each row into a dictionary
        for row in csvReader:
            data = dict(row)
            if data['Year'] in ['2022', '2021']:
                sensorData = dict(row)
                saveSensorData = {}
                try:
                    saveSensorData['ID'] = sensorData['ID']
                    saveSensorData['Hourly_Counts'] = int(sensorData['Hourly_Counts'])
                    saveSensorData['Sensor_ID'] = int(sensorData['Sensor_ID'])
                    saveSensorData['Time'] = int(sensorData['Time'])
                    saveSensorData['Mdate'] = int(sensorData['Mdate'])
                    saveSensorData['Month'] = sensorData['Month']
                    saveSensorData['Year'] = int(sensorData['Year'])
                    saveSensorData['Day'] = sensorData['Day']
                    sensor_dict_list.append(saveSensorData)
                    if sensorData['ID'] not in camera_ID_list:
                        saveSensorLocationData = {}
                        # wait done
                except:
                    pass
    return sensor_dict_list

def read_json_australian_post_code(file_name):
    # load file
    file = open(file_name, 'r', encoding='utf-8-sig')
    data = json.load(file)

    dataReturn = []
    idList = []
    for postcodeData in data:
        if (3000 <= int(postcodeData['postcode']) <= 3999) or (
                8000 <= int(postcodeData['postcode']) <= 8999):
            coordinate = [postcodeData['Long_precise'], postcodeData['Lat_precise']]
            suburbID = find_area(coordinate)
            if suburbID != -1:
                if postcodeData["postcode"] not in idList:
                    saveDict = {}
                    saveDict['_id'] = postcodeData["postcode"]
                    saveDict['suburbID'] = suburbID
                    dataReturn.append(saveDict)
                    idList.append(postcodeData["postcode"])
    return dataReturn


# define path to data
JSON_FILE_CRIME = './dataUpload/crime_data.csv'
JSON_FILE_HOUSE = './dataUpload/house_data.csv'
JSON_FILE_AGE = './dataUpload/age_data.json'
JSON_FILE_CAMERA_LOCATION = './dataUpload/Pedestrian_Counting_System_-_Sensor_Locations.json'
JSON_FILE_CAMERA_DATA = './dataUpload/Pedestrian_Counting_System_-_Monthly__counts_per_hour_.csv'
JSON_FILE_BUSINESS = './dataUpload/business_data.json'
JSON_FILE_AUSTRALIAN_CODE = "./dataUpload/australian_postcodes.json"

JSON_FILE_NLP_BASE = "./dataUpload/NLP_Analysis/"

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


def threadSaveMethod(save_list, db):
    threads = [Thread(target=couch_save_data, args=(save_list, db, i, threadLength)) for i in
               range(threadLength)]
    print(db.name + " length is " + str(len(save_list)))
    for threadRun in threads:
        threadRun.start()


# # save crime data
# crime_save_list = read_csv(JSON_FILE_CRIME)
# db = retrieve_couchdb(couch, "crime_data")
# threadSaveMethod(crime_save_list, db)
#
# save house data
# house_save_list = read_csv(JSON_FILE_HOUSE)
# db = retrieve_couchdb(couch, "house_data")
# threadSaveMethod(house_save_list, db)

# # save age group
# age_save_list = read_json(JSON_FILE_AGE)
# db = retrieve_couchdb(couch, "age_data")
# threadSaveMethod(age_save_list, db)
#
# save camera sensor data
# camera_save_list = read_csv_camera_filter(JSON_FILE_CAMERA_DATA)
# db = retrieve_couchdb(couch, "camera_data")
# threadSaveMethod(camera_save_list, db)
#
# save camera sensor location data
# camera_location_list = read_json(JSON_FILE_CAMERA_LOCATION)
# db = retrieve_couchdb(couch, "camera_location_data")
# threadSaveMethod(camera_location_list, db)
#
# save business_data
# business_save_list = read_json(JSON_FILE_BUSINESS)
# db = retrieve_couchdb(couch, "business_data")
# threadSaveMethod(business_save_list, db)


# save australian postcode data
# australian_save_list = read_json_australian_post_code(JSON_FILE_AUSTRALIAN_CODE)
# print(len(australian_save_list))
# db = retrieve_couchdb(couch, "postcode_to_suburb")
# threadSaveMethod(australian_save_list, db)

# read all_city metal data
Mental_save_list = read_json(JSON_FILE_NLP_BASE + "Mental.json")
db = retrieve_couchdb(couch, "mental_data")
threadSaveMethod(Mental_save_list, db)

# read sentiment relevant tweet data
# Melbourne_save_list = read_json(JSON_FILE_NLP_BASE + "Melbourne_mental_suburb.json")
# db = retrieve_couchdb(couch, "melbourne_mental_data")
#
# # create view
# mapFunction = {}
# mapFunction = '''function (doc) {
#   if (doc.rt*5 + doc.like >= 50){
#     emit([1, doc.sentiment_polarity, doc.sentiment_subjectivity], parseInt(Math.log(doc.rt*5 + doc.like)));
#   } else{
#     emit([0, doc.sentiment_polarity, doc.sentiment_subjectivity], 1);
#   }
# }'''
#
# createView(db, "backend", "view_by_mental", mapFunction)
# threadSaveMethod(Melbourne_save_list, db)

# #
# shutil.rmtree('./dataUpload')
