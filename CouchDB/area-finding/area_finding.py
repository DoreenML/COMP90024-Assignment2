import os
import json
# need to install shapely first, use: pip install shapely
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

# define the local location of files
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

JSON_FILE = 'phidu_admissions_preventable_diagnosis_vaccine_pha_2016_17-6982188917692169592.json'

def read_json(file_name):
    # load file
    file = open(os.path.join(__location__, file_name), 'r', encoding='utf-8-sig')
    data = json.load(file)
    return data

def form_area_dict():
    area_dict = {}
    data = read_json(JSON_FILE)
    for idx in range(276):
        area_dict[idx] = data["features"][idx]["geometry"]["coordinates"][0][0]
    return area_dict

area_dict = form_area_dict()

'''
This function take the chosen coordinate in the form like [143.607845,-36.882307],
then it returns the code of the area which contains this point. There are total 276
area avaible. If no area matches this point, the function will return 'OUT', which means
it's outside of the Victortia. 
'''
def find_area(cor_list):
    point = Point(cor_list)
    for idx in range(276):
        polygon = Polygon(area_dict[idx])
        if (polygon.contains(point)):
            return idx + 1
    return "OUT"

print(find_area([143.607845,-36.882307]))