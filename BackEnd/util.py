from calendar import monthrange
from datetime import date, timedelta, datetime
import couchdb
import logging


# quick function
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


def getCameraData(couch, datasetName="camera_data", designName="backend", viewName="view_by_hour"):
    db = couch[datasetName]
    view = db.view(designName + "/" + viewName, reduce=True, group=True, group_level=3)

    returnDict = {}
    for doc in view:
        print(doc)
        break
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
