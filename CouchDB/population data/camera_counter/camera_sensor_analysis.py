
import csv
import json
import os
import couchdb
 
 # define the local location of files
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

couch_url = "http://admin:adminPass@172.26.133.126:5984/"
couch = couchdb.Server(couch_url)

jsonFilePath = 'camera_sensor.json'
csvFilePath = 'Pedestrian_Counting_System_-_Monthly__counts_per_hour_.csv'
Total_entry = 3711503

sensor_dict = {}
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath):
     
    # create a dictionary
     
    # Open a csv reader called DictReader
    with open(os.path.join(__location__, csvFilePath), encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        counter = 0
        for rows in csvReader:
            sensor_dict[counter] = rows
            counter += 1

 
make_json(csvFilePath)
print("---- Sensor dictionary Ready")

db = couch['street_sensor_data']
Continue_from = 123053
for idx in range(Continue_from, Total_entry):
    db.save(sensor_dict[idx])
    print("current index:", idx)
    print("Percent remaining:", (1 - idx/Total_entry)*100)