from flask import Flask, jsonify
from flask_cors import CORS
import couchdb
import util

# define back_end
app = Flask(__name__)
CORS(app)

# default couch
adminName = "admin"
adminPasswd = "adminPass"
url = "172.26.130.135:5984/"
# define couch
couch_url = "http://" + adminName + ":" + adminPasswd + "@" + url
couch = couchdb.Server(couch_url)


def getPostCodeToSuburb(couch, datasetName="postcode_to_suburb", designName="backend",
                        viewName="view_postcode_to_aurin"):
    db = couch[datasetName]
    view = db.view(designName + "/" + viewName)

    returnDict = {}
    for doc in view:
        returnDict[doc['key']] = doc['value']
    return returnDict


# test function
# util.getCameraLocation(couch)
# util.getCameraData(couch)
# util.getHouseData(couch)
# util.getPostCodeToSuburb(couch)

# Hospital Resources and COVID Cases Map
# print(util.getCameraData(couch))

# Symptom and Depression Analysis
# print(util.getMelbourneMentalData(couch))

# Symptom and Depression Analysis


# preapre data for map visulization
# real time covid data
postCodeToAurin = util.getPostCodeToSuburb(couch)
list_60, list_30 = util.getCovidData(couch, postCodeToAurin)
list_60 = util.getCovidList(list_60)
list_30 = util.getCovidList(list_30)

list_sub = [{'name': i, 'value': list_30[i]['value'] - list_60[i]['value']} for i in range(183)]

# melbourne depression map
melbourneMetalData = util.getMelbourneMentalData(couch)
dataForLowVol = [[dot['sentiment'], dot['subjective']] for dot in melbourneMetalData if dot['tweetInfluence'] == "low_volumn_tweet"]
dataForHighVol = [[dot['sentiment'], dot['subjective']] for dot in melbourneMetalData if dot['tweetInfluence'] == "high_volumn_tweet"]

@app.route("/DepressionChart")
def Chart_Depression():
    data = {}
    data['high'] = dataForHighVol
    data['low'] = dataForLowVol
    
    data = jsonify(data)
    return data


# transfer data to front end map
@app.route("/HealthMap")
def Chart_HealthMap():
    # port for the polygon
    data = {}
    data['polygon'] = list_sub

    # port for the scatter
    data['scatter'] = {}
    data['scatter']['_1'] = {}

    data['scatter']['_1']['supermarket'] = 100

    data = jsonify(data)
    return data


# demo for front-end
@app.route("/HealthRelatedTopicTrend")
def Chart_HealthRelatedTopicTrend():
    data = {}
    data['area_1'] = {}
    data['area_1']['vomiting'] = 12
    data['area_1']['burn'] = 17
    data['area_1']['chill'] = 13
    data['area_1']['fever'] = 8
    data['area_1']['pimples'] = 6
    data['area_1']['fractured'] = 14
    data['area_1']['toothache'] = 7
    data['area_1']['tumor'] = 3
    data['area_1']['mood'] = 9

    data['area_2'] = {}
    data['area_2']['vomiting'] = 12
    data['area_2']['burn'] = 8
    data['area_2']['chill'] = 9
    data['area_2']['fever'] = 6
    data['area_2']['pimples'] = 2
    data['area_2']['fractured'] = 9
    data['area_2']['toothache'] = 4
    data['area_2']['tumor'] = 6
    data['area_2']['mood'] = 11

    data['area_3'] = {}
    data['area_3']['vomiting'] = 12
    data['area_3']['burn'] = 8
    data['area_3']['chill'] = 9
    data['area_3']['fever'] = 6
    data['area_3']['pimples'] = 2
    data['area_3']['fractured'] = 9
    data['area_3']['toothache'] = 4
    data['area_3']['tumor'] = 6
    data['area_3']['mood'] = 11

    data['greeting'] = "Hello from Flask"
    data = jsonify(data)
    return data


# @app.route("/covidRelatedAurin")
# def Chart_HealthRelatedTopicTrend():
#     data = jsonify({'area_1': {'vomiting': 1, 'burn': 2}})
#     return data


if __name__ == '__main__':
    # retrieve data
    app.run()
