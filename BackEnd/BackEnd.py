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
util.getCameraData(couch)
# util.getHouseData(couch)
# util.getPostCodeToSuburb(couch)


# Symptom and Depression Analysis
# print(util.getMelbourneMentalData(couch))

# Symptom and Depression Analysis


# prepare data for map visualization
# real time covid data
postCodeToAurin = util.getPostCodeToSuburb(couch)
list_60, list_30 = util.getCovidData(couch, postCodeToAurin)
list_60 = util.getCovidList(list_60)
list_30 = util.getCovidList(list_30)

list_sub = [{'name': i, 'value': list_30[i]['value'] - list_60[i]['value']} for i in range(183)]

# # melbourne depression map
melbourneMetalData = util.getMelbourneMentalData(couch)
dataForLowVol = [[dot['sentiment'], dot['subjective']] for dot in melbourneMetalData if dot['tweetInfluence'] == "low_volumn_tweet"]
dataForHighVol = [[dot['sentiment'], dot['subjective']] for dot in melbourneMetalData if dot['tweetInfluence'] == "high_volumn_tweet"]


# transfer data to front end map
@app.route("/HealthMap")
def Chart_HealthMap():
    # port for the polygon
    data = {'polygon': list_sub, 'scatter': {}}

    # port for the scatter
    data['scatter']['_1'] = {}

    data['scatter']['_1']['supermarket'] = 100

    data = jsonify(data)
    return data


# demo for front-end
@app.route("/HealthRelatedTopicTrend")
def Chart_HealthRelatedTopicTrend():
    data = jsonify({'area_1': {'vomiting': 1, 'burn': 2}})
    return data


@app.route("/covidRelatedAurin")
def Chart_HealthRelatedTopicTrend():
    data = jsonify({'area_1': {'vomiting': 1, 'burn': 2}})
    return data


if __name__ == '__main__':
    # retrieve data
    app.run()
