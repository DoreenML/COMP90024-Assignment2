# Qi Li & 1138875 & lql4@student.unimelb.edu.au
# Yuheng Guo & 1113036 & yuhengg1@student.unimelb.edu.au
# Zhaoyang Zhang  & 1240942 & zhaoyangz1@student.unimelb.edu.au
# Zhaoyu Wei  & 1258372 & zhangyuw@student.unimelb.edu.au
# Xiaohan Ma  & 1145763 & mxm3@student.unimelb.edu.au
from datetime import date, timedelta, datetime
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import logging
import json
import math


# # quick function
def read_json(file_name):
    # load file
    file = open(file_name, 'r', encoding='utf-8-sig')
    data = json.load(file)
    return data


# # post code to aurin suburb id

def form_area_dict():
    area_dict = {}
    data = read_json(".areaData.json")
    for idx in range(276):
        area_dict[idx] = data["features"][idx]["geometry"]["coordinates"][0][0]
    return area_dict


def find_area(cor_list):
    area_dict = form_area_dict()
    point = Point(cor_list)
    for idx in range(185):
        polygon = Polygon(area_dict[idx])
        if (polygon.contains(point)):
            return idx + 1
    return -1


def suburb_name():
    return ['Essendon', 'Carlton North', 'Coburg', 'Northcote', 'Thornbury', 'Ascot Vale', 'Brunswick West',
            'Travancore', 'Burton Reserve', 'Southbank', 'South Yarra', 'Footscray', 'CBD', 'Oceania', 'Parkville',
            'Albert Park', 'Brighton', 'Port Phillip Bay', 'South Melbourne', 'St Kilda West', 'Caulfield North',
            'Windsor', 'Fairfield', 'Barlton North', 'Fitzroy', 'Burnley', 'Ashburton', 'Surrey Hills', 'Camberwell',
            'Glen Iris', 'Hawthorn', 'Kew', 'Mont Albert North', 'Donvale', 'Bulleen', 'Blackburn', 'Box Hill South',
            'Forest Hill', 'Box Hill Nouth', 'Beaumaris', 'Crighton', 'Cheltenham', 'Hampton', 'Oakleigh South',
            'Brighton East', 'Gardenvale', 'Elsternwick', 'Malvern East', 'Murrumbeena', 'Chelsea', 'Patterson Lakes',
            'City of Kingston', 'Hampton East', 'Carnegie', 'Watsonia', 'Templestowe', 'Lower Plenty', 'Macleod',
            'Ivanhoe', 'Ivanhoe East', 'Cundoora', 'Bellfield', 'Reservoir', 'Coburg North', 'Research',
            'Kinglake Central', 'Clonbinane', 'Wattle Glen', 'Bundoora', 'City of Whittlesea', 'Epping', 'Thomastown',
            'Plenty', 'Mill Park', 'Yarrambat', 'Hazeldene', 'City of Moonee Valley', 'Keilor', 'Maribyrnong',
            'Oak Park', 'Cherokee', 'Lancefield', 'Hadfield', 'Fawkner', 'Pascoe Vale', 'Glenroy', 'Sunbury',
            'Broadmeadows', 'Lalor', 'Keilar', 'Coolaroo', 'Somerton', 'Sassafras', 'Ferntree Gully', 'Scoresby',
            'Dandenong North', 'Wantirna South', 'Donvala', 'Bayswater North', 'Croydon South', 'Ringwood North',
            'Heathmont', 'Nunawading', 'Vermont South', ' Mitcham', 'Menzies Creek', 'Mount Dandenong', 'Toolangi',
            'Montrose', 'Seville East', 'Macclesfield', 'Powelltown', 'Gembrook', 'Tonimbuk', 'Heath Hill', 'Pakenham',
            'Berwack', 'Beaconsfield', 'Dandnong North', 'Hallam', 'Hellam', 'Berweck', 'Tooradin', 'Lynbrook',
            'Cranbourne South', 'Narre Warren', 'Lynbrok', 'Berwick', 'Clarinda', 'Dandenong', 'Endeavour Hills',
            'Clayton South', 'Dandenong South', 'Keysborough', 'Noble Park', 'Clarinde', 'Notting Hill',
            'Glen Waverley', 'Rowville', 'Mount Waverley', 'Brooklyn', 'St Albans', 'Cairnlea', 'Delahey', 'Kealba',
            'Burnside', 'Avondale Heights', 'Taylors Lakes', 'Keilor North', 'Willimstown', 'Altona', 'Newport',
            'Williamstown', 'Altona Meadows', 'Avondale', 'Seddon', 'Aberfeldie', 'Yarraville', 'Coimadai', 'Ravenhall',
            'Bonnie Brook', 'Long Forest', 'Deanside', 'Werribee', 'Cocoroc', 'Altona North', 'Point Cook', 'Eynesbury',
            'Little River', 'Mount Cottrell', 'Seaford', 'Frankstan', 'Frankston', 'Frankstan South', 'Langwarrin',
            'Dromana', 'Shoreham', 'Hmas Cerberus', 'Somerville', 'Frankston South', 'Portsea', 'Rosebud', 'Navigators']


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


def getWaveKey():
    keyList = [[[1, 2020, 3, "Friday", 0], [1, 2020, 5, "Wednesday", 24]],
               [[1, 2020, 6, "Friday", 0], [1, 2020, 10, "Wednesday", 24]],
               [[1, 2021, 7, "Friday", 0], [1, 2021, 12, "Wednesday", 24]],
               [[1, 2022, 1, "Friday", 0], [1, 2022, 4, "Wednesday", 24]]]
    # demo sensor ID is 1, change dynamically
    return keyList


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
            if doc['key'][0] in halfDaysList:
                returnDictOneMonth[aurinCode] += doc['value']
            else:
                returnDictTwoMonth[aurinCode] += doc['value']
        except:
            pass

    return returnDictOneMonth, returnDictTwoMonth


def getCovidListSub(couch, postCodeToAurin):
    list_60, list_30 = getCovidData(couch, postCodeToAurin)
    list_60 = getCovidList(list_60)
    list_30 = getCovidList(list_30)

    nameList = suburb_name()
    list_sub = [{'name': nameList[i], 'value': list_30[i]['value'] - list_60[i]['value']} for i in range(183)]

    return list_sub


def getCameraLocationData(couch, datasetName="camera_location_data", designName="backend", viewName="camera_location"):
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


def getCameraData(couch, datasetName="camera_data", designName="backend", viewName="view_by_hour"):
    db = couch[datasetName]

    sensorDict = getCameraLocationData(couch)
    # iterate vist wave
    nowHour = datetime.now().hour
    for wave, [startDate, endDate] in enumerate(getWaveKey()):
        commonLabel = "wave_" + str(wave) + "_hour_" + str(nowHour)
        for sensorID in range(1, 80):
            try:
                sensorDict[sensorID][commonLabel] = {}
                # specify sensor ID
                startDate[0] = sensorID
                endDate[0] = sensorID
                # get view
                view = db.view(designName + "/" + viewName, reduce=True, group=True, group_level=5, startkey=startDate,
                               endkey=endDate)
                # define day list
                dayList = ["Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"]
                sensorDict[sensorID][commonLabel]['sum'] = 0
                sensorDict[sensorID][commonLabel]['count'] = 0
                sensorDict[sensorID][commonLabel]['max'] = 0
                sensorDict[sensorID][commonLabel]['hour'] = nowHour
                for doc in view:
                    if doc.key[4] == nowHour:
                        sensorDict[sensorID][commonLabel]['sum'] += doc.value['sum']
                        sensorDict[sensorID][commonLabel]['count'] += doc.value['count']
                        sensorDict[sensorID][commonLabel]['max'] = max(doc.value['max'],
                                                                       sensorDict[sensorID][commonLabel]['max'])
                try:
                    sensorDict[sensorID][commonLabel]['avgCount'] = sensorDict[sensorID][commonLabel]['sum'] / \
                                                                    sensorDict[sensorID][commonLabel]['count']
                except:
                    pass
                del sensorDict[sensorID][commonLabel]['count']
                del sensorDict[sensorID][commonLabel]['sum']
            except:
                pass
    return sensorDict


def getMelbourneMentalData(couch, datasetName="melbourne_mental_data", designName="backend", viewName="view_by_mental"):
    db = couch[datasetName]
    view = db.view(designName + "/" + viewName, reduce=True, group=True, group_level=3)
    returnList = []

    for doc in view:
        [volumnClassifier, sentiment, subjective] = doc.key
        if volumnClassifier == 1:
            volumnClassifier = "high_volumn_tweet"
        else:
            volumnClassifier = "low_volumn_tweet"
        if {"tweetInfluence": volumnClassifier,
            "sentiment": sentiment,
            "subjective": subjective} not in returnList and (doc.value >= 5 or volumnClassifier == 1):
            returnList.append({
                "tweetInfluence": volumnClassifier,
                "sentiment": sentiment,
                "subjective": subjective
            })
    return returnList


def getMentalData(couch, datasetName="mental_data", designName="backend", viewName="view_by_hashtag"):
    db = couch[datasetName]
    view = db.view(designName + "/" + viewName, reduce=True, group=True, group_level=3)

    tagList = ['auspol', 'Australia', 'PokemonGO', 'COVID19', 'OnThisDay', 'MedTwitter', "BREAKING"]
    selectTagDictList = []
    for tag in tagList:
        saveDict = {'name': tag, "data": []}
        selectTagDictList.append(saveDict)

    tmpDateList = [[] for _ in range(len(tagList))]
    tmpValueList = [[] for _ in range(len(tagList))]
    for doc in view:
        if doc.key[1] in tagList:
            index = tagList.index(doc.key[1])
            tmpDateList[index].append(doc.key[0])
            tmpValueList[index].append(doc.value)
            # selectTagDictList[index]['tag'].append(doc.value)

    commonDate = tmpDateList[0]
    for i in range(1, len(tmpDateList)):
        commonDate = list(set(commonDate).intersection(tmpDateList[i]))
        commonDate.sort()

    for i, tagDict in enumerate(selectTagDictList):
        for dateGive in commonDate:
            index = tmpDateList[i].index(dateGive)
            selectTagDictList[i]['data'].append(tmpValueList[i][index])
    return selectTagDictList


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


def getMelbourneMentalByWave(couch, datasetName="melbourne_mental_data",
                             designName="backend",
                             wave1="view_by_objective_and_sentiment_wave1",
                             wave2="view_by_objective_and_sentiment_wave2",
                             wave3="view_by_objective_and_sentiment_wave3",
                             wave4="view_by_objective_and_sentiment_wave4"):
    db = couch[datasetName]
    # area interest in 92, 40, 10, 6, 5
    areaList = [92, 40, 10, 5]
    waveNameList = ['wave1', 'wave2', 'wave3', 'wave4']
    areaDict = {"wave1": {92: [0] * 4, 40: [0] * 4, 10: [0] * 4, 5: [0] * 4},
                "wave2": {92: [0] * 4, 40: [0] * 4, 10: [0] * 4, 5: [0] * 4},
                "wave3": {92: [0] * 4, 40: [0] * 4, 10: [0] * 4, 5: [0] * 4},
                "wave4": {92: [0] * 4, 40: [0] * 4, 10: [0] * 4, 5: [0] * 4}}
    # sentiment and objective code:
    # 3: positive/subjective,
    # 2: positive/objective,
    # 1: negative/subjective,
    # 0: negative/objective
    waveViews = [db.view(designName + "/" + wave1, reduce=True, group=True),
                 db.view(designName + "/" + wave2, reduce=True, group=True),
                 db.view(designName + "/" + wave3, reduce=True, group=True),
                 db.view(designName + "/" + wave4, reduce=True, group=True)]

    for i, waveView in enumerate(waveViews):
        for doc in waveView:
            if doc.key[0] in areaList:
                areaDict[waveNameList[i]][doc.key[0]][doc.key[1]] += round(math.log2(doc.value))

    returnList = [[] for _ in range(16)]
    for waveIndex, waveName in enumerate(waveNameList):
        for i in range(4):
            for j, suburbName in enumerate(areaList):
                returnList[waveIndex * 4 + i].append(areaDict[waveName][suburbName][i])
    return returnList


def getPostCodeToSuburb(couch, datasetName="postcode_to_suburb", designName="backend",
                        viewName="view_postcode_to_aurin"):
    db = couch[datasetName]
    view = db.view(designName + "/" + viewName)

    returnDict = {}
    for doc in view:
        returnDict[doc['key']] = doc['value']
    return returnDict
