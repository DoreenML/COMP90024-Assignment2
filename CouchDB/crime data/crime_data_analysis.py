import json
import os
import couchdb

couch_url = "http://admin:adminPass@172.26.133.126:5984/"
couch = couchdb.Server(couch_url)

# define the local location of files
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

JSON_FILE = 'Data_Tables_Recorded_Offences_Visualisation_Year_Ending_December_2021.json'

def read_json(file_name):
    # load file
    file = open(os.path.join(__location__, file_name), 'r', encoding='utf-8-sig')
    data = json.load(file)
    return data

crime_data = read_json(JSON_FILE)
table_list = ['Table 01', 'Table 02', 'Table 03', 'Table 04', 'Table 05', 'Table 06']

def store_crime_dict():
    crime_dict = {}
    data_counter = 0
    for table_idx in range(6):
        lst = crime_data[table_list[table_idx]]
        for item in lst:
            # print(item)
            crime_dict[data_counter] = item
            data_counter+=1
    return crime_dict

crime_dict = store_crime_dict()
# print(type(crime_dict[1234]))

db = couch['crime_data']
for idx in range(62984):
    db.save(crime_dict[idx])




# db.save(dict)