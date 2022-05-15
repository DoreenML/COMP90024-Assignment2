from flask import Flask, jsonify
from flask_cors import CORS
import couchdb
import util
import constant

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

# real time covid data
postCodeToAurin = util.getPostCodeToSuburb(couch)
list_sub = util.getCovidListSub(couch, postCodeToAurin)

# melbourne depression map
melbourneMetalData = util.getMelbourneMentalData(couch)
dataForLowVol = [[dot['sentiment'], dot['subjective']] for dot in melbourneMetalData if dot['tweetInfluence'] == "low_volumn_tweet"]
dataForHighVol = [[dot['sentiment'], dot['subjective']] for dot in melbourneMetalData if dot['tweetInfluence'] == "high_volumn_tweet"]

@app.route("/DepressionChart")
def Chart_Depression():
    data = {}
    data['high'] = dataForHighVol
    data['low'] = dataForLowVol

    data['first_wave'] = {} 
    data['first_wave']['_1'] = 1499108
    data['first_wave']['_2'] = 478149
    data['first_wave']['_3'] = 299290
    data['first_wave']['_4'] = 273256
    data['first_wave']['_5'] = 193480
    data['first_wave']['_6'] = 193480
    data['first_wave']['_7'] = 91315
    data['first_wave']['_8'] = 80478
    data['first_wave']['_9'] = 78880
    data['first_wave']['_10'] = 54687

    data['second_wave'] = {} 
    data['second_wave']['_1'] = 1465705
    data['second_wave']['_2'] = 617975
    data['second_wave']['_3'] = 508395
    data['second_wave']['_4'] = 337720
    data['second_wave']['_5'] = 238320
    data['second_wave']['_6'] = 204560
    data['second_wave']['_7'] = 204230
    data['second_wave']['_8'] = 197457
    data['second_wave']['_9'] = 169600
    data['second_wave']['_10'] = 158375

    data['third_wave'] = {} 
    data['third_wave']['_1'] =3747280
    data['third_wave']['_2'] =1696185
    data['third_wave']['_3'] =1681301
    data['third_wave']['_4'] =1345710
    data['third_wave']['_5'] =823670
    data['third_wave']['_6'] =500110
    data['third_wave']['_7'] =423230
    data['third_wave']['_8'] =339445
    data['third_wave']['_9'] =201490
    data['third_wave']['_10'] =194035

    data['fourth_wave'] = {} 
    data['fourth_wave']['_1'] =2205335
    data['fourth_wave']['_2'] =1799435
    data['fourth_wave']['_3'] =1272200
    data['fourth_wave']['_4'] =1035780
    data['fourth_wave']['_5'] =882610
    data['fourth_wave']['_6'] =714680
    data['fourth_wave']['_7'] =693805
    data['fourth_wave']['_8'] =690750
    data['fourth_wave']['_9'] =680140
    data['fourth_wave']['_10'] =658520

    
    data = jsonify(data)
    return data


sensorWaveFrontEnd = []
# get front end data format
for _, value in constant.returnSensorWaveData().items():
    try:
        saveSensorData = {}
        wave1 = value[list(value.keys())[3]]
        wave2 = value[list(value.keys())[4]]
        wave3 = value[list(value.keys())[5]]
        wave4 = value[list(value.keys())[6]]

        saveSensorData['value'] = [value['longtitude'], value['latitude']]
        strTab = '<br/>'
        saveSensorData['name'] = \
            "sensor name: " + value['description'] + strTab \
            + list(value.keys())[3] + "average count: " + str(int(wave1['avgCount'])) + strTab \
            + list(value.keys())[4] + "average count: " + str(int(wave2['avgCount'])) + strTab \
            + list(value.keys())[5] + "average count: " + str(int(wave3['avgCount'])) + strTab \
            + list(value.keys())[6] + "average count: " + str(int(wave4['avgCount'])) + strTab
        sensorWaveFrontEnd.append(saveSensorData)
    except:
        pass

# print(sensorWaveFrontEnd)

# transfer data to front end map
@app.route("/HealthMap")
def Chart_HealthMap():
    # port for the polygon
    data = {}
    data['polygon'] = list_sub

    # port for the scatter
    data['scatter'] = {}
    data['scatter']['info'] = sensorWaveFrontEnd

    data = jsonify(data)
    return data

data_mental_timeline = util.getMentalData(couch)
# demo for front-end
@app.route("/MentalTimeLine")
def Chart_MentalTimeline():
    data = {}
    dictList = data_mental_timeline
    data['mental'] = {}
    data['mental']['_0'] = dictList[0]['data']
    data['mental']['_1'] = dictList[1]['data']
    data['mental']['_2'] = dictList[2]['data']
    data['mental']['_3'] = dictList[3]['data']
    data['mental']['_4'] = dictList[4]['data']
    data['mental']['_5'] = dictList[5]['data']
    data['mental']['_6'] = dictList[6]['data']
    data = jsonify(data)
    return data

wave_info = util.getMelbourneMentalByWave(couch)
@app.route("/SentimentWave")
def Chart_SentimentWave():
    data = {}
    temp = wave_info
    data['w_1'] = {}
    data['w_1']['_0'] = temp[0]
    data['w_1']['_1'] = temp[1]
    data['w_1']['_2'] = temp[2]
    data['w_1']['_3'] = temp[3]

    data['w_2'] = {}
    data['w_2']['_0'] = temp[4]
    data['w_2']['_1'] = temp[5]
    data['w_2']['_2'] = temp[6]
    data['w_2']['_3'] = temp[7]

    data['w_3'] = {}
    data['w_3']['_0'] = temp[8]
    data['w_3']['_1'] = temp[9]
    data['w_3']['_2'] = temp[10]
    data['w_3']['_3'] = temp[11]

    data['w_4'] = {}
    data['w_4']['_0'] = temp[12]
    data['w_4']['_1'] = temp[13]
    data['w_4']['_2'] = temp[14]
    data['w_4']['_3'] = temp[15]

    data = jsonify(data)
    return data


if __name__ == '__main__':
    # retrieve data
    app.run()
