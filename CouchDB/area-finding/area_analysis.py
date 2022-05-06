import os
import json
from turtle import distance
# need to install shapely first, use: pip install shapely
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import math

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

'''
This dictionary contians the area code with the corresponding polygon.
'''
area_dict = form_area_dict()

# print(area_dict[54])

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

# print(find_area([143.607845,-36.882307]))

def get_lon_lst(polygon):
    lon_lst = [] 
    for item in polygon:
        lon_lst.append(item[0])
    return lon_lst

def get_lat_lst(polygon):
    lat_lst = [] 
    for item in polygon:
        lat_lst.append(item[1])
    return lat_lst

'''
This function take the chosen area code and returns the center point of this 
area.
'''
def find_center(area_code):
    center = []
    polygon = area_dict[area_code]
    lon_lst = get_lon_lst(polygon)
    lat_lst = get_lat_lst(polygon)
    center.append(sum(lon_lst)/len(lon_lst))
    center.append(sum(lat_lst)/len(lat_lst))
    return center
    

# print(find_center(128))

'''
This function take the chosen area code from 1 to 256, and it returns the 
radius of the polygon, which is half of Euclidien distance bewteen the max 
coordinate and the min coordinate.
'''
def find_radius(area_code):
    polygon = area_dict[area_code]
    lon_lst = get_lon_lst(polygon)
    lat_lst = get_lat_lst(polygon)

    max_lon = max(lon_lst)
    min_lon = min(lon_lst)
    max_lat = max(lat_lst)
    min_lat = min(lat_lst)

    min_cor = (min_lon,min_lat)
    max_cor = (max_lon,max_lat)

    distance = math.dist(min_cor,max_cor)
    return distance/2

# print(find_radius(201))

def fill_geo_dict():
    geo_dict = {}
    for i in range(276):
        geo_dict[i] = (find_center(i)[0],find_center(i)[1],find_radius(i)*111110)
    return geo_dict

geo_dict = fill_geo_dict()
print(geo_dict)
    