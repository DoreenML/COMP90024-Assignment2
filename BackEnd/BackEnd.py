from flask import Flask
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
CORS(app)

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
    data['polygon'] = {}
    data['polygon']['_179'] = 42
    data['polygon']['_180'] = 92

    # port for the scatter
    data['scatter'] = {}
    data['scatter']['_1'] = {}
    data['scatter']['_1']['supermarket'] = 100

    data = jsonify(data)
    return data
    

if __name__ == '__main__':
    app.run()
