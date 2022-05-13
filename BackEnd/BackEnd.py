from flask import Flask
from flask_cors import CORS
from flask import jsonify
import couchdb
import util
import collections

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


postCodeToAurin = getPostCodeToSuburb(couch)
thirty_days, sixty_days = util.getCovidData(couch, postCodeToAurin)
thirty_days = collections.OrderedDict(sorted(thirty_days.items()))
sixty_days = collections.OrderedDict(sorted(sixty_days.items()))
print(thirty_days)
print('\n')
print(sixty_days)


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

@app.route("/HealthMap")
def Chart_HealthMap():
    # port for the polygon
    data = {}
    returnList = []
    for i in range(1, 183):
        returnList.append({
            'name': str(i),
            'value': i,
        })
    data['polygon'] = returnList

    # port for the scatter
    data['scatter'] = {}
    data['scatter']['_1'] = {}
    data['scatter']['_1']['supermarket'] = 100

    data = jsonify(data)
    return data

if __name__ == '__main__':
    app.run()
