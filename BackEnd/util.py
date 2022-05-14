from datetime import date, timedelta, datetime
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import logging
import json
import calendar


# quick function
def read_json(file_name):
    # load file
    file = open(file_name, 'r', encoding='utf-8-sig')
    data = json.load(file)
    return data


# post code to aurin suburb id

def form_area_dict():
    area_dict = {}
    data = read_json(
        "../CouchDB/dataUpload/phidu_admissions_preventable_diagnosis_vaccine_pha_2016_17-6982188917692169592.json")
    for idx in range(276):
        area_dict[idx] = data["features"][idx]["geometry"]["coordinates"][0][0]
    return area_dict


area_dict = form_area_dict()


def find_area(cor_list):
    point = Point(cor_list)
    for idx in range(185):
        polygon = Polygon(area_dict[idx])
        if (polygon.contains(point)):
            return idx + 1
    return -1


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
    logging.info(f"creating view {designDoc}/{viewName}")
    dbConn.save(data)


# demo for create view
# mapFunction = '''function (doc) {
#                       if( doc.type == 'word')
#                       emit(doc.word, doc);
#                     }'''
# createView( db, "DESIGN_DOC_NAME", "VIEW_NAME", mapFunction )

def getCameraLocation(couch, datasetName="camera_location_data", designName="camera_location", viewName="location"):
    db = couch[datasetName]
    view = db.view(designName + "/" + viewName)

    returnDict = {}
    for doc in view:
        returnDict[doc.key] = {
            "sensorName": doc.value[0],
            "latitude": doc.value[1],
            "longitude": doc.value[2],
        }
    return returnDict


def getHouseData(couch, datasetName="house_data", designName="backend", viewName="view_by_building_cluster"):
    db = couch[datasetName]
    view = db.view(designName + "/" + viewName, reduce=True, group=True)

    returnDict = {}

    for i, doc in enumerate(view):
        returnDict[i] = {
            "latitude": doc.key[0],
            "longitude": doc.key[1],
            "placeUsage": doc.key[2],
            "countNumber": doc.value
        }
    return returnDict


def getCovidData(couch, postCodeToAurin, datasetName="activate_covid_database", designName="backend",
                 viewName="view_by_date"):
    db = couch[datasetName]
    view = db.view(designName + "/" + viewName, reduce=True, group=True)

    returnDictOneMonth = {}
    returnDictTwoMonth = {}
    daysList = getTwoMonthDateRange()
    halfDaysList = daysList[:int(len(daysList) / 2)]
    for doc in view:
        # save each aurin as a list
        try:
            aurinCode = postCodeToAurin[str(doc['key'][1])]
            if aurinCode not in returnDictOneMonth:
                returnDictOneMonth[aurinCode] = 0
                returnDictTwoMonth[aurinCode] = 0
            returnDictTwoMonth[aurinCode] += doc['value']
            if doc['key'][0] in halfDaysList:
                returnDictOneMonth[aurinCode] += doc['value']
        except:
            pass

    return returnDictOneMonth, returnDictTwoMonth


# wave 1: 2020-03 to 2020-05
# wave 2: 2020-06 to 2020-10
# wave 3: 2021-07 to 2021-12
# wave 4: 2022-01 to present
def getWaveKey():
    keyList = []
    # demo sensor ID is 1, change dynamically
    keyList.append([[1, 2020, 0, "Sunday", "March"], [1, 2020, 0, "Sunday", "May"]])
    keyList.append([[1, 2020, 0, "Monday", "June"], [1, 2020, 0, "Thursday", "October"]])
    keyList.append([[1, 2021, 0, "Wednesday", "March"], [1, 2021, 0, "Friday", "December"]])
    keyList.append([[1, 2022, 0, "Saturday", "January"], [1, 2022, 0, "Sunday", "April"]])
    return keyList


def getCameraData(couch, datasetName="camera_data", designName="backend", viewName="view_by_hour"):
    db = couch[datasetName]

    sensorDict = getCameraLocationData(couch)
    # iterate vist wave
    for [startDate, endDate] in getWaveKey():
        for sensorID in range(1, 80):
            # specify sensor ID
            startDate[0] = sensorID
            endDate[0] = sensorID
            # get view
            view = db.view(designName + "/" + viewName, reduce=True, group=True, group_level=4, startkey=startDate, endkey=endDate)
            print(view)
    # for doc in view:
    #     [sensorID, year, time, day, month] = doc.key
    #
    #     sensorID = int(sensorID)
    #     if sensorID in range(1, 80):
    #         if time == current_hour_int and current_day_str == day:
    #             averageNumber = doc.value['sum'] / doc.value['count']
    #
    #             if current_month_str == month and year == current_year_int:
    #                 sensorDict[sensorID][labelThisMonth] = averageNumber
    #             elif last_month_str == month and year == current_year_int:
    #                 sensorDict[sensorID][labelLastMonth] = averageNumber
    #             elif current_month_str == month and year == current_year_int - 1:
    #                 sensorDict[sensorID][labelLastYear] = averageNumber
    #
    # # add ratio
    # for i in range(1, 80):
    #     if i in list(sensorDict.keys()):
    #         try:
    #             thisMonthAverage = sensorDict[i][labelThisMonth]
    #             try:
    #                 lastMonthAverage = sensorDict[i][labelLastMonth]
    #                 sensorDict[i]['Compared to month average'] = str(
    #                     ((thisMonthAverage - lastMonthAverage) / lastMonthAverage) * 100) + "%"
    #             except:
    #                 sensorDict[i]['Compared to month average'] = "data lost"
    #             try:
    #                 lastYearAverage = sensorDict[i][labelLastYear]
    #                 sensorDict[i]['Compared to year average'] = str(
    #                     ((thisMonthAverage - lastYearAverage) / lastYearAverage) * 100) + "%"
    #             except:
    #                 sensorDict[i]['Compared to year average'] = "data lost"
    #         except:
    #             sensorDict[i][labelThisMonth] = -1
    #             sensorDict[i]['Compared to year average'] = "data lost"
    #             sensorDict[i]['Compared to month average'] = "data lost"
    #
    return sensorDict


def getCameraLocationData(couch, datasetName="camera_location_data", designName="camera_location", viewName="location"):
    db = couch[datasetName]
    view = db.view(designName + "/" + viewName)
    returnDict = {}
    for doc in view:
        [description, latitude, longtitude] = doc.value
        returnDict[doc.key] = {
            "description": description,
            "latitude": latitude,
            "longtitude": longtitude
        }
    return returnDict


def getMelbourneMentalData(couch, datasetName="melbourne_mental_data", designName="backend", viewName="view_by_mental"):
    db = couch[datasetName]
    view = db.view(designName + "/" + viewName, reduce=True, group=True)
    returnList = []
    for doc in view:
        [volumnClassifier, sentiment, subjective] = doc.key
        if volumnClassifier == 1:
            volumnClassifier = "high_volumn_tweet"
        else:
            volumnClassifier = "low_volumn_tweet"
        returnList.append({
            "tweetInfluence": volumnClassifier,
            "sentiment": sentiment,
            "subjective": subjective,
            "weight": doc.value
        })
    return returnList


def getPostCodeToSuburb(couch, datasetName="postcode_to_suburb", designName="backend",
                        viewName="view_postcode_to_aurin"):
    db = couch[datasetName]
    view = db.view(designName + "/" + viewName)

    returnDict = {}
    for doc in view:
        returnDict[doc['key']] = doc['value']
    return returnDict


def getCovidList(givenCovidDict):
    returnList = []
    valueList = list(givenCovidDict.values())
    count = 0
    for i in range(1, 184):
        if i in list(givenCovidDict.keys()):
            returnList.append({
                'name': i,
                'value': givenCovidDict[i],
            })
        else:
            returnList.append({
                'name': i,
                'value': valueList[(183 + count) % len(givenCovidDict)],
            })
            count += 1
    return returnList
