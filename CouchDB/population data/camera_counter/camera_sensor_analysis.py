
import csv
import json
import os 
 
 # define the local location of files
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

jsonFilePath = 'camera_sensor.json'
csvFilePath = 'Pedestrian_Counting_System_-_Monthly__counts_per_hour_.csv'

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
     
    # Open a csv reader called DictReader
    with open(os.path.join(__location__, csvFilePath), encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        counter = 0
        for rows in csvReader:
            data = {}
            data[counter] = rows
            counter += 1
            print("Converting remaining:", (1 - (counter/4220000))*100)
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(os.path.join(__location__, jsonFilePath), 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
         
# Driver Code
 
# Call the make_json function
make_json(csvFilePath, jsonFilePath)