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


postCodeToAurin = getPostCodeToSuburb(couch)
a, b = util.getCovidData(couch, postCodeToAurin)
print(len(a))

print(len(b))

# demo for front-end
# @app.route("/HealthRelatedTopicTrend")
# def Chart_HealthRelatedTopicTrend():
#     data = jsonify({'area_1': {'vomiting': 1, 'burn': 2}})
#     return data

#
# @app.route("/covidRelatedAurin")
# def Chart_HealthRelatedTopicTrend():
#     data = jsonify({'area_1': {'vomiting': 1, 'burn': 2}})
#     return data
#
# if __name__ == '__main__':
#     # retrieve data
#     app.run()
