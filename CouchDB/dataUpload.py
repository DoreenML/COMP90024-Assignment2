import os
import io
import csv
import time
import json
import shutil
import couchdb
import schedule
import requests
import pandas as pd
from threading import Thread
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from datetime import date, timedelta

# set passwd and username and url of couch
adminName = "admin"
adminPasswd = "adminPass"
url = "172.26.134.245:5984/"

# test local host
# adminName = "admin"
# adminPasswd = "a13552676625"
# url = "127.0.0.1:5984/"

# define couch
couch_url = "http://" + adminName + ":" + adminPasswd + "@" + url
couch = couchdb.Server(couch_url)
# define thread length
threadLength = 64

# define camera location for retrieve
camera_location_list = []
camera_ID_list = []

# define real time data
covidRealTimeURL = "https://www.dhhs.vic.gov.au/ncov-covid-cases-by-lga-source-csv"
estateRealTimeURL = "https://data.melbourne.vic.gov.au/api/views/gh7s-qda8/rows.csv?accessType=DOWNLOAD"


# common function
def dateRange(start, end):
    delta = end - start  # as timedelta
    days = [start + timedelta(days=i) for i in range(delta.days + 1)]
    return days


def getTwoMonthDateRange():
    todayDate = date.today()
    twoMonthDaysAgoDate = todayDate - timedelta(days=60)
    days = dateRange(twoMonthDaysAgoDate, todayDate)
    daysString = [dateUnit.strftime("%Y-%m-%d") for dateUnit in days]
    return daysString


def find_area(cor_list):
    area_dict = form_area_dict()
    point = Point(cor_list)
    for idx in range(185):
        polygon = Polygon(area_dict[idx])
        if (polygon.contains(point)):
            return idx + 1
    return -1


def read_json(file_name):
    # load file
    file = open(file_name, 'r', encoding='utf-8-sig')
    data = json.load(file)
    return data


def form_area_dict():
    area_dict = {}
    data = read_json("../BackEnd/areaData.json")
    for idx in range(276):
        area_dict[idx] = data["features"][idx]["geometry"]["coordinates"][0][0]
    return area_dict


# method for couchdb
def createView(dbConn, designDoc, viewName, mapFunction, reduceFunction='_sum'):
    data = {
        "_id": f"_design/{designDoc}",
        "views": {
            viewName: {
                "map": mapFunction,
                "reduce": reduceFunction
            }
        },
        "language": "javascript",
        "options": {"partitioned": False}
    }
    dbConn.save(data)


def createViewForNone(dbConn, designDoc, viewName, mapFunction):
    data = {
        "_id": f"_design/{designDoc}",
        "views": {
            viewName: {
                "map": mapFunction,
            }
        },
        "language": "javascript",
        "options": {"partitioned": False}
    }
    dbConn.save(data)


def createMultiViews(dbConn, designDoc, viewNameList, mapFunctionList, reduceFunctionList):
    views = {}
    for i in range(len(viewNameList)):
        views[viewNameList[i]] = {"map": mapFunctionList[i], "reduce": reduceFunctionList[i]}
    data = {
        "_id": f"_design/{designDoc}",
        "views": views,
        "language": "javascript",
        "options": {"partitioned": False}
    }
    dbConn.save(data)


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
            if data['Year'] in ['2022', '2021', '2020']:
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


### read 2014-2017 mental data in all city
def read_aurin_file(filePath):
    f = open(filePath)
    data = json.loads(f.read())['features']
    aurinSaveList = []
    for saveItem in data:
        getItem = saveItem['properties']
        if getItem["presentation_type"] == "Mental health-related presentations":
            aurinSaveList.append(getItem)
    return aurinSaveList


# define path to data
JSON_FILE_CRIME = './dataUpload/crime_data.csv'
JSON_FILE_HOUSE = './dataUpload/house_data.csv'
JSON_FILE_AGE = './dataUpload/age_data.json'
JSON_FILE_CAMERA_LOCATION = './dataUpload/Pedestrian_Counting_System_-_Sensor_Locations.json'
JSON_FILE_CAMERA_DATA = './dataUpload/Pedestrian_Counting_System_-_Monthly__counts_per_hour_.csv'
JSON_FILE_BUSINESS = './dataUpload/business_data.json'
JSON_FILE_AUSTRALIAN_CODE = "./dataUpload/australian_postcodes.json"
JSON_FILE_NLP_BASE = "./dataUpload/NLP_Analysis/"

JSON_FILE_AURIN_BASE = "dataUpload/aurin/"
JSON_2014_2015 = "mental health emergency 2014-2015.json"
JSON_2015_2016 = "mental health emergency 2015-2016.json"
JSON_2016_2017 = "mental health emergency 2016-2017.json"
JSON_2017_2018 = "mental health emergency 2017-2018.json"


# define couchdb save method
def retrieve_couchdb(servers, serverName):
    try:
        database = servers[serverName] if serverName in servers else servers.create(serverName)
    except Exception as e:
        database = servers.create("new_" + serverName)
    return database


# define multi thread save method
def couch_save_data(saveList, db, rank, length):
    for i, saveItem in enumerate(saveList):
        if i % length == rank:
            try:
                db.save(saveItem)
            except:
                pass
    return


# get covid activate case
def update_covid_activate_case(couchGiven):
    csv = requests.get(covidRealTimeURL).content
    df = pd.read_csv(io.StringIO(csv.decode('utf-8')))
    records = df.to_dict(orient='records')
    print("csv crawl done")
    # get last two week new cases
    daysNeed = getTwoMonthDateRange()
    saveList = []
    # del unnecessary attribute
    for i in range(len(records)):
        if records[i]['diagnosis_date'] in daysNeed:
            del records[i]["acquired"]
            del records[i]["Localgovernmentarea"]
            saveList.append(records[i])

    # del database
    try:
        couchGiven.delete("activate_covid_database")
    except:
        pass

    db = retrieve_couchdb(couchGiven, "activate_covid_database")
    threadSaveMethod(saveList, db)

    # create view
    mapFunction = '''function (doc) {
      if(doc["diagnosis_date"] != ""){
        emit([doc["diagnosis_date"], doc["Postcode"]], 1);
      }
    }'''
    createView(db, "backend", "view_by_date", mapFunction)
    return records


# def update_real_estate(couchGiven):
#     csv = requests.get(estateRealTimeURL).content
#     df = pd.read_csv(io.StringIO(csv.decode('utf-8')))
#     records = df.to_dict(orient='records')
#     saveList = []
#
#     for i in range(len(records)):
#         try:
#             if records[i]['status'] == 'COMPLETED':
#                 saveDict = {}
#                 coordinate = [records[i]['longitude'], records[i]['latitude']]
#                 saveDict['suburbID'] = find_area(coordinate)
#                 saveDict['longitude'] = records[i]['longitude']
#                 saveDict['latitude'] = records[i]['latitude']
#                 saveDict['one_bdrm_dwe'] = records[i]['one_bdrm_dwe']
#                 saveDict['two_bdrm_dwe'] = records[i]['two_bdrm_dwe']
#                 saveDict['three_bdrm_dwe'] = records[i]['three_bdrm_dwe']
#                 saveList.append(saveDict)
#         except:
#             print(records[i])
#     # del database
#     try:
#         couchGiven.delete("real_time_estate_data")
#     except:
#         pass
#
#     db = retrieve_couchdb(couchGiven, "real_time_estate_data")
#     threadSaveMethod(saveList, db)


def threadSaveMethod(save_list, db):
    threads = [Thread(target=couch_save_data, args=(save_list, db, i, threadLength)) for i in
               range(threadLength)]
    print(db.name + " length is " + str(len(save_list)))
    for threadRun in threads:
        threadRun.start()


# update real estate and covid data once per day
def updateDaily(couchGiven):
    # update_real_estate(couchGiven)
    update_covid_activate_case(couchGiven)


def updateOnce(couchGiven):
    ### save crime data
    # crime_save_list = read_csv(JSON_FILE_CRIME)
    # db = retrieve_couchdb(couchGiven, "crime_data")
    # # create view
    # mapFunction = '''function (doc) {
    #   if(parseInt(doc["Year"]) >= 2019){
    #       emit([doc["Year"], doc["Postcode"], doc["Offence Division"], doc["Offence Subdivision"], doc["Offence Subgroup"]], parseInt(doc['Incidents Recorded']));
    #     }
    # }'''
    # createView(db, "backend", "view_by_category_postcode", mapFunction)
    # threadSaveMethod(crime_save_list, db)

    # ### save house data
    # house_save_list = read_csv(JSON_FILE_HOUSE)
    # db = retrieve_couchdb(couchGiven, "house_data")
    # mapFunction = '''function (doc) {
    #   if (parseInt(doc['Census year']) >= 2020){
    #   emit([doc['CLUE small area'], doc['Census year'], doc['Predominant space use']], 1);
    #   }
    # }'''
    # createView(db, "backend", "view_by_building_suburb", mapFunction)
    # threadSaveMethod(house_save_list, db)

    ### save age group
    # age_save_list = read_json(JSON_FILE_AGE)
    # db = retrieve_couchdb(couchGiven, "age_data")
    # threadSaveMethod(age_save_list, db)

    ### save camera sensor data
    # camera_save_list = read_csv_camera_filter(JSON_FILE_CAMERA_DATA)
    # db = retrieve_couchdb(couchGiven, "camera_data")
    # mapFunction = '''function (doc) {
    #   var monthList = ['January','February','March','April','May','June','July','August','September','October','November','December']
    #   emit([doc.Sensor_ID, doc.Year, monthList.indexOf(doc.Month) + 1, doc.Day, doc.Time], doc.Hourly_Counts);
    # }'''
    # createView(db, "backend", "view_by_hour", mapFunction, "_stats")
    # threadSaveMethod(camera_save_list, db)

    ### save camera sensor location data
    # camera_location_list = read_json(JSON_FILE_CAMERA_LOCATION)
    # db = retrieve_couchdb(couchGiven, "camera_location_data")
    # mapFunction = '''function (doc) {
    #   emit(doc.sensor_id, [doc.sensor_description , doc.latitude, doc.longitude]);
    # }'''
    # createViewForNone(db, "backend", "camera_location", mapFunction)
    # threadSaveMethod(camera_location_list, db)

    # save business_data
    # business_save_list = read_json(JSON_FILE_BUSINESS)
    # db = retrieve_couchdb(couchGiven, "business_data")
    # threadSaveMethod(business_save_list, db)

    ### save australian postcode data
    australian_save_list = read_json_australian_post_code(JSON_FILE_AUSTRALIAN_CODE)
    print(len(australian_save_list))
    db = retrieve_couchdb(couchGiven, "postcode_to_suburb")
    mapFunction = '''function (doc) {
      emit(doc._id, doc.suburbID);
    }'''
    createViewForNone(db, "backend", "view_postcode_to_aurin", mapFunction)
    threadSaveMethod(australian_save_list, db)

    ### save all city metal data
    ### create view list
    Mental_save_list = read_json(JSON_FILE_NLP_BASE + "Mental.json")
    db = retrieve_couchdb(couchGiven, "mental_data")
    mapFunction = '''function (doc) {
      if (doc.hashtag.length !== 0){
        for (let i = 0; i < doc.hashtag.length; i++){
          if (1+ doc.rt*5 + doc.like >= 100){
           emit([doc.time, doc.hashtag[i]], 1+ doc.rt*5 + doc.like);
          }
        }
      }
    }'''
    createView(db, "backend", "view_by_hashtag", mapFunction)
    threadSaveMethod(Mental_save_list, db)

    # read sentiment relevant tweet data
    Melbourne_save_list = read_json(JSON_FILE_NLP_BASE + "Melbourne_mental_suburb.json")
    db = retrieve_couchdb(couchGiven, "melbourne_mental_data")

    # create view
    mapFunctionNameList = ['view_by_mental',
                           'view_by_objective_and_sentiment_wave1',
                           'view_by_objective_and_sentiment_wave2',
                           'view_by_objective_and_sentiment_wave3',
                           'view_by_objective_and_sentiment_wave4',
                           'view_by_suburb']
    reduceFunctionList = ['_sum' for i in range(len(mapFunctionNameList))]

    mapFunctionList = []
    mapFunctionList.append('''function (doc) {
      if (doc.hashtag.length != 0){
        var volLabel = 0
        if (doc.rt*5 + doc.like >= 50){
          volLabel = 1
        }
        for (let i = 0; i < doc.hashtag.length; i++){
          emit([volLabel, doc.sentiment_polarity, doc.sentiment_subjectivity, doc.hashtag[i]], 1);
        }
      }
    }''')

    # wave1
    mapFunctionList.append('''function (doc) {
      year = parseInt(doc.time.slice(0, 4))
      month = parseInt(doc.time.slice(-2))
      if (year == 2020 && month >= 3 && month <= 5){
        if(doc.sentiment_polarity >= 0.25){
          if(doc.sentiment_subjectivity >= 0.5){
            emit([doc.user_suburb, 3], doc.rt*5 + doc.like);
          } else if(doc.sentiment_subjectivity < 0.5){
            emit([doc.user_suburb, 2], doc.rt*5 + doc.like);
          }
        }
        else if(doc.sentiment_polarity <= -0.25){
          if(doc.sentiment_subjectivity >= 0.5){
            emit([doc.user_suburb, 1], doc.rt*5 + doc.like);
          } else if(doc.sentiment_subjectivity < 0.5){
            emit([doc.user_suburb, 0], doc.rt*5 + doc.like);
          }
        }
      }
    }''')
    # wave2
    mapFunctionList.append('''function (doc) {
      year = parseInt(doc.time.slice(0, 4))
      month = parseInt(doc.time.slice(-2))
      if (year == 2020 && month >= 6 && month <= 10){
        if(doc.sentiment_polarity >= 0.25){
          if(doc.sentiment_subjectivity >= 0.5){
            emit([doc.user_suburb, 3], doc.rt*5 + doc.like);
          } else if(doc.sentiment_subjectivity < 0.5){
            emit([doc.user_suburb, 2], doc.rt*5 + doc.like);
          }
        }
        else if(doc.sentiment_polarity <= -0.25){
          if(doc.sentiment_subjectivity >= 0.5){
            emit([doc.user_suburb, 1], doc.rt*5 + doc.like);
          } else if(doc.sentiment_subjectivity < 0.5){
            emit([doc.user_suburb, 0], doc.rt*5 + doc.like);
          }
        }
      }
    }''')
    # wave3
    mapFunctionList.append('''function (doc) {
      year = parseInt(doc.time.slice(0, 4))
      month = parseInt(doc.time.slice(-2))
      if (year == 2021 && month >= 7 && month <= 12){
        if(doc.sentiment_polarity >= 0.25){
          if(doc.sentiment_subjectivity >= 0.5){
            emit([doc.user_suburb, 3], doc.rt*5 + doc.like);
          } else if(doc.sentiment_subjectivity < 0.5){
            emit([doc.user_suburb, 2], doc.rt*5 + doc.like);
          }
        }
        else if(doc.sentiment_polarity <= -0.25){
          if(doc.sentiment_subjectivity >= 0.5){
            emit([doc.user_suburb, 1], doc.rt*5 + doc.like);
          } else if(doc.sentiment_subjectivity < 0.5){
            emit([doc.user_suburb, 0], doc.rt*5 + doc.like);
          }
        }
      }
    }''')
    # wave4
    mapFunctionList.append('''function (doc) {
      year = parseInt(doc.time.slice(0, 4))
      month = parseInt(doc.time.slice(-2))
      if (year == 2022 && month >= 1 && month <= 5){
        if(doc.sentiment_polarity >= 0.25){
          if(doc.sentiment_subjectivity >= 0.5){
            emit([doc.user_suburb, 3], doc.rt*5 + doc.like);
          } else if(doc.sentiment_subjectivity < 0.5){
            emit([doc.user_suburb, 2], doc.rt*5 + doc.like);
          }
        }
        else if(doc.sentiment_polarity <= -0.25){
          if(doc.sentiment_subjectivity >= 0.5){
            emit([doc.user_suburb, 1], doc.rt*5 + doc.like);
          } else if(doc.sentiment_subjectivity < 0.5){
            emit([doc.user_suburb, 0], doc.rt*5 + doc.like);
          }
        }
      }
    }''')
    # view_by_suburb
    mapFunctionList.append('''function (doc) {
      for (let i = 0; i < doc.hashtag.length; i++){
          emit([doc.user_suburb, doc.hashtag[i]], 1);
      }
    }''')
    # create multiple view
    createMultiViews(db, "backend", mapFunctionNameList, mapFunctionList, reduceFunctionList)
    threadSaveMethod(Melbourne_save_list, db)

    # save mental data
    saveLists = [read_aurin_file(JSON_FILE_AURIN_BASE + JSON_2014_2015),
                 read_aurin_file(JSON_FILE_AURIN_BASE + JSON_2015_2016),
                 read_aurin_file(JSON_FILE_AURIN_BASE + JSON_2016_2017),
                 read_aurin_file(JSON_FILE_AURIN_BASE + JSON_2017_2018)]

    db = retrieve_couchdb(couchGiven, "city_mental_data")
    for saveList in saveLists:
        threadSaveMethod(saveList, db)
    mapFunction = '''function (doc) {
      emit([doc.sa3_name, doc.fin_yr], doc.rt_10k);
    }'''

    createView(db, "backend", "view_city_name", mapFunction)


# save data
updateOnce(couch)
updateDaily(couch)
# delete local cache
shutil.rmtree('./dataUpload')

# run update daily onece per day
schedule.every().day.at("01:00").do(updateDaily, couch)
while True:
    schedule.run_pending()
    time.sleep(20)
